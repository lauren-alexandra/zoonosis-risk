import os
import re
import pickle
import time
import zipfile
from glob import glob
from math import floor, ceil
from tqdm.notebook import tqdm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import rioxarray as rxr
import rioxarray.merge as rxrmerge
import xarray as xr
from shapely.geometry import Polygon

import earthaccess
from earthaccess import results
import earthpy as et
import pygbif.occurrences as occ


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

@cached('yolo_granule_metadata', override=False)
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

def process_image(uri, bounds_gdf, masked=True, scale=1):
    """
    Load, crop, and scale a raster image

    Parameters
    ----------
    uri: file-like or path-like
      File accessor 
    bounds_gdf: gpd.GeoDataFrame
      Area of interest 

    Returns
    -------
    cropped_da: rxr.DataArray
      Processed raster
    """
    # Load and scale
    da = rxr.open_rasterio(uri, masked=masked).squeeze() * scale

    # Obtain crs from raster
    raster_crs = da.rio.crs

    # Match coordinate reference systems
    bounds_gdf = bounds_gdf.to_crs(raster_crs)

    # Crop to site boundaries
    cropped_da = da.rio.clip_box(*bounds_gdf.total_bounds)

    return cropped_da

def process_mask(da):
    """
    Load a DataArray and process to a boolean mask

    Parameters
    ----------
    da: DataArray
      The input DataArray

    Returns
    -------
    mask: np.array
      Boolean mask
    """
    # HLS Quality Assessment layer bits
    bits_to_mask = [
        1, # Cloud
        2, # Adjacent to cloud/shadow
        3  # Cloud shadow
    ]

    # Get the mask as bits
    bits = (
        np.unpackbits(
            (
                # Get the mask as an array
                da.values
                # of 8-bit integers
                .astype('uint8')
                # with an extra axis to unpack the bits into
                .reshape(da.shape + (-1,))
            ), 
            # List the least significant bit first to match the user guide
            bitorder='little',
            # Expand the array in a new dimension
            axis=-1)
    )
    
    # Calculate the product of the mask and bits to mask
    mask = np.prod(
        # Multiply bits and check if flagged
        bits[..., bits_to_mask]==0,
        # From the last to the first axis
        axis=-1
    )

    return mask

@cached('yolo_reflectance_da_df', override=False)
def compute_reflectance_da(file_df, boundary_gdf):
    """
    Connect to files over VSI (Virtual Filesystem Interface), 
    crop, cloud mask, and wrangle data.
    
    Returns a reflectance DataArray within file DataFrame.
    
    Parameters
    ==========
    file_df : pd.DataFrame
        File connection and metadata 
    boundary_gdf : gpd.GeoDataFrame
        Boundary use to crop the data
    """
    granule_da_rows= []

    # unique dated data granules
    tile_groups = file_df.groupby(['granule_date', 'tile_id'])

    for (granule_date, tile_id), tile_df in tqdm(tile_groups):
        print(f'Processing granule {tile_id} {granule_date}')

        # Grab Fmask row from tile group
        Fmask_row = tile_df.loc[tile_df['band_id'] == 'Fmask']
        # Load cloud path
        cloud_path = Fmask_row.uri.values[0]
        cloud_da = process_image(cloud_path, boundary_gdf, masked=False)
        # Compute cloud mask
        cloud_mask = process_mask(cloud_da)

        # Load spectral bands
        band_groups = tile_df.groupby('band_id')

        for band_name, band_df in band_groups:
            for index, row in band_df.iterrows():
                # Process band and retain band scale
                cropped_da = process_image(row.uri, boundary_gdf, scale=0.0001)
                cropped_da.name = band_name

                # Apply mask on band to remove unwanted cloud data
                row['da'] = cropped_da.where(~cropped_da.isin(cloud_mask))

                # Store the resulting DataArray
                granule_da_rows.append(row.to_frame().T)

    # Reassemble the metadata DataFrame
    return pd.concat(granule_da_rows)

@cached('yolo_reflectance_da', override=False)
def create_composite_da(granule_da_df):
    """
    Create a composite DataArray from a DataFrame containing granule
    metadata and corresponding DataArrays.

    Args:
    granule_da_df (pandas.DataFrame): Granule metadata DataFrame. 

    Returns:
    xarray.DataArray: Composite granule DataArray. 
    """
    composite_das = []

    for band, band_df in tqdm(granule_da_df.groupby('band_id')):
        merged_das = []

        if (band != 'Fmask'):
            for granule_date, date_df in tqdm(band_df.groupby('granule_date')):

                # For each date merge granule DataArrays
                merged_da = rxrmerge.merge_arrays(list(date_df.da))

                # Mask all negative values
                merged_da = merged_da.where(merged_da > 0)
                merged_das.append(merged_da)

            # Create composite images across dates (by median date) 
            # to fill cloud gaps
            composite_da = xr.concat(
                merged_das, dim='granule_date').median('granule_date')

            # Add the band as a dimension
            composite_da['band'] = int(band[1:])
            
            # Name the composite DataArray
            composite_da.name = 'reflectance'

            composite_das.append(composite_da)

    # Concatenate on the band dimension
    return xr.concat(composite_das, dim='band')

def normalize_occurrences(df):
    """
    Normalize occurrence data for given species.

    Args:
    occ_df (pandas.DataFrame): DataFrame of species occurrence.

    Returns:
    norm_occ_df (pandas.DataFrame): DataFrame of normalized species occurrence.
    """
    
    occ_df = (
        df
        # For each month
        .groupby(['host_name', 'month'])
        # count the number of occurrences
        .agg(occurrences=('host_name', 'count'))
    )

    # Drop rare observations (possible misidentification)
    occ_df = occ_df[occ_df["occurrences"] > 1]

    # Take the mean by month
    mean_occurrences_by_month = (
        occ_df
        .groupby(['month'])
        .mean()
    )

    occ_df['norm_occurrences'] = (
        occ_df
        / mean_occurrences_by_month
    )

    return occ_df 

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

### Load Data ### 

def load_gbif(gbif_csv):
    """
    Load occurrence data from GBIF CSV.

    Args:
    gbif_csv (str): A path to downloaded species CSV.

    Returns:
    (pandas.DataFrame): A species occurrence DataFrame.
    """
    return pd.read_csv(
        gbif_csv, 
        delimiter='\t',
        index_col='gbifID',
        on_bad_lines='skip',
        usecols=['gbifID', 'order', 'species', 'month', 'day', 'year', 
                 'decimalLatitude', 'decimalLongitude']
    )

### Download Data ### 

def download_gbif(species, gbif_credentials, species_dict, 
                  period, site_bounds):
    """
    Download occurrence data for given species.

    Args:
    species (str): Input host species name. 
    gbif_credentials (dict): GBIF API credentials.
    species_dict (dict): Host species GBIF metadata.
    period (str): Temporal range of observations.
    site_bounds (list): Site boundary coordinates.

    Returns:
    gbif_path (str): A path to downloaded species CSV.
    """
    
    gbif_dir = species_dict[species]['DATA PATH']
    species_key = species_dict[species]['GBIF SPECIES']
    species_download_key = species_dict[species]['GBIF DOWNLOAD']
    site_latitude = f'{site_bounds[1]},{site_bounds[3]}'
    site_longitude = f'{site_bounds[0]},{site_bounds[2]}'
    
    # Only download once
    gbif_pattern = os.path.join(gbif_dir, '*.csv')
    if not glob(gbif_pattern):
        # Submit query to GBIF
        gbif_query = occ.download([
            f"speciesKey = {species_key}",
            f"eventDate = {period}",
            f"decimalLatitude = {site_latitude}",
            f"decimalLongitude = {site_longitude}",
            "hasCoordinate = TRUE",
        ],
        user=gbif_credentials['GBIF_USER'][1], 
        pwd=gbif_credentials['GBIF_PWD'][1], 
        email=gbif_credentials['GBIF_EMAIL'][1])

        # Only download once
        if not species_download_key in os.environ:
            os.environ[species_download_key] = gbif_query[0]

            # Wait for the download to build
            wait = occ.download_meta(
                    os.environ[species_download_key])['status'] 
            while not wait=='SUCCEEDED':
                wait = occ.download_meta(
                        os.environ[species_download_key])['status'] 
                time.sleep(5)

            # Download GBIF data
            download_info = occ.download_get(
                os.environ[species_download_key], 
                path=gbif_dir)

            # Unzip GBIF data
            with zipfile.ZipFile(download_info['path']) as download_zip:
                download_zip.extractall(path=gbif_dir)

    # Find the extracted .csv file path
    gbif_path = glob(gbif_pattern)[0]
    
    return gbif_path
