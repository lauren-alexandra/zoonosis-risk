import os
import re
import pickle
from glob import glob
from math import floor, ceil
import tqdm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import rioxarray as rxr
from rioxarray.merge import merge_arrays
import xarray as xr
from shapely.geometry import Polygon
import earthaccess
from earthaccess import results
import earthpy as et


def cached(func_key, override=False):
    """
    A decorator to cache function results
    
    Parameters
    ==========
    key: str
      File basename used to save pickled results
    override: bool
      When True, re-compute even if the results are already stored
    """
    def compute_and_cache_decorator(compute_function):
        """
        Wrap the caching function
        
        Parameters
        ==========
        compute_function: function
          The function to run and cache results
        """
        def compute_and_cache(*args, **kwargs):
            """
            Perform a computation and cache, or load cached result.
            
            Parameters
            ==========
            args
              Positional arguments for the compute function
            kwargs
              Keyword arguments for the compute function
            """
            # Add an identifier from the particular function call
            if 'cache_key' in kwargs:
                key = '_'.join((func_key, kwargs['cache_key']))
            else:
                key = func_key

            path = os.path.join(
                et.io.HOME, et.io.DATA_NAME, 'jars', f'{key}.pickle')
            
            # Check if the cache exists already or override caching
            if not os.path.exists(path) or override:
                # Make jars directory if needed
                os.makedirs(os.path.dirname(path), exist_ok=True)
                
                # Run the compute function as the user did
                result = compute_function(*args, **kwargs)
                
                # Pickle the object
                with open(path, 'wb') as file:
                    pickle.dump(result, file)
            else:
                # Unpickle the object
                with open(path, 'rb') as file:
                    result = pickle.load(file)
                    
            return result
        
        return compute_and_cache
    
    return compute_and_cache_decorator

### Data Wrangling ###

def export_raster(da, raster_path, data_dir):
    """
    Export raster DataArray to a raster file.
    
    Args:
    raster (xarray.DataArray): Input raster layer.
    raster_path (str): Output raster directory.
    data_dir (str): Path of data directory.

    Returns: None
    """
    
    output_file = os.path.join(data_dir, os.path.basename(raster_path))
    da.rio.to_raster(output_file)

@cached('granule_metadata', override=False)
def build_granule_metadata(hls_results):
    """
    Collect granule metadata from HLS tiles.

    Args:
    hls_results (List[DataGranule]): HLS search results list.

    Returns:
    granule_metadata (list): List of granule metadata dictionaries.
    """

    # Find all the metadata in the file
    granule_metadata = [] 

    # Loop through each granule
    for result in tqdm(hls_results):

        # Granule ID
        granule_id = result['umm']['GranuleUR']

        # Get datetime 
        temporal_coverage = results.DataCollection.get_umm(
            result, 'TemporalExtent')
        granule_date = (pd.to_datetime(
            temporal_coverage['RangeDateTime']['BeginningDateTime']
        ).strftime('%Y-%m-%d'))

        print(f'Processing date {granule_date}. Granule ID: {granule_id}.')

        # Assemble granule polygon 
        spatial_ext = results.DataCollection.get_umm(result, 'SpatialExtent')
        granule_geo = spatial_ext['HorizontalSpatialDomain']['Geometry']
        granule_points = granule_geo['GPolygons'][0]['Boundary']['Points']
        granule_coords = [tuple(point.values()) for point in granule_points]
        granule_polygon = Polygon(granule_coords)

        # Open granule files
        granule_files = earthaccess.open([result])

        # Use () to select the desired name and only output that name
        uri_re = re.compile(
            r"v2.0/(HLS.L30.*.tif)"
        )

        # Select unique tiles
        tile_id_re = re.compile(
            r"HLSL30.020/(HLS.L30..*.v2.0)/HLS"
        )

        # Grab band IDs
        band_id_re = re.compile(
            r"HLS.L30..*v2.0.(\D{1}.*).tif"
        )

        # Collect file metadata
        for uri in granule_files:

            # Make sure uri has full_name property first
            if (hasattr(uri, 'full_name')):
                file_name = uri_re.findall(uri.full_name)[0]
                tile_id = tile_id_re.findall(uri.full_name)[0]
                band_id = band_id_re.findall(uri.full_name)[0]

                # Only keep spectral bands and cloud Fmask
                # Exclude sun and view angles
                exclude_files = ['SAA', 'SZA', 'VAA', 'VZA']

                if band_id not in exclude_files:
                    granule_metadata.append({
                        'filename': file_name,
                        'tile_id': tile_id,
                        'band_id': band_id,
                        'granule_id': granule_id,
                        'granule_date': granule_date,
                        'granule_polygon': granule_polygon,
                        'uri': uri
                    })

    # Concatenate granule metadata 
    granule_metadata_df = pd.DataFrame(
        data=granule_metadata, columns=[
            'filename', 'tile_id', 'band_id', 'granule_id', 
            'granule_date', 'granule_polygon', 'uri'])

    granule_results_gdf = gpd.GeoDataFrame(
            granule_metadata_df, 
            geometry=granule_metadata_df['granule_polygon'], 
            crs="EPSG:4326")

    return granule_results_gdf

### Visualization ###

def plot_site(site_da, site_gdf, plots_dir, site_fig_name, plot_title, 
              bar_label, plot_cmap, boundary_clr, tif_file=False):
    """
    Create custom site plot.
    
    Args:
    site_da (xarray.DataArray): Input site raster.
    site_gdf (geopandas.GeoDataFrame): Input site GeoDataFrame.
    plots_dir (str): Path of plots directory.
    site_fig_name (str): Site figure name.
    plot_title (str): Plot title. 
    bar_label (str): Plot bar variable name.
    plot_cmap (str): Plot colormap name.
    boundary_clr (str): Plot site boundary color.
    tif_file (bool): Indicates a site file.

    Returns:
    matplotlib.pyplot.plot: A plot of site values.
    """
    
    fig = plt.figure(figsize=(8, 6)) 
    ax = plt.axes()

    if tif_file:
        site_da = rxr.open_rasterio(site_da, masked=True)

    # Plot DataArray values
    site_plot = site_da.plot(
                            cmap=plot_cmap, 
                            cbar_kwargs={'label': bar_label}
                        )

    # Plot site boundary
    site_gdf.boundary.plot(ax=plt.gca(), color=boundary_clr)

    plt.title(f'{plot_title}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    fig.savefig(f"{plots_dir}/{site_fig_name}.png") 

    return site_plot
