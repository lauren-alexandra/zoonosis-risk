import os
import time
import zipfile
from glob import glob
import pandas as pd
import pygbif.occurrences as occ

### Data Wrangling ###

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
