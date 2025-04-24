# Zoonosis Risk

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15225925.svg)](https://doi.org/10.5281/zenodo.15225925)

<img src="images/black-necked_stilts_ca_rice_commission.png" alt="Black-necked stilts forage in wet rice fields" width="760" height="500" longdesc="https://www.ucdavis.edu/sites/default/files/media/images/9127201758-024b4c82d0-o.jpg" />

## Overview

**How do natural sources of highly pathogenic avian influenza (HPAI) at the wildlife–agriculture interface influence spillover risk in California's Central Valley?**

With each animal that is infected by avian influenza, there is another chance for the virus to evolve into a pathogen fit for human-to-human transmission. Creating early warning systems built on a One Health framework–integrating human, animal, and environmental health–are a wise investment to support state biosecurity. 

Since 2006, the USDA National [Wildlife Disease Program](https://www.cdfa.ca.gov/AHFSS/animal_health/Wildlife_Services.html#:~:text=The%20Wildlife%20Services%20Program%20is%20a%20partnership,breaks%20or%20the%20compromise%20of%20other%20infrastructure**) (NWDP) in partnership with the California Department of Food and Agriculture has established a surveillance framework sampling wild birds for HPAI and other pathogens that may impact domestic poultry, wild bird species, and humans. NWDP wildlife disease biologists serve as sentinels in the program’s Surveillance and Emergency Response System (SERS) and have collected over 500,000 samples to date. Existing disease surveillance frameworks like SERS can be bolstered to account for environmental factors and host behavior, informing conservation strategies for timely interventions that safeguard human and animal health. 

This project will explore the county in Central Valley with the highest HPAI detection in wild birds which is [Yolo County](https://www.yolocounty.gov). Two sources of pathogen transmission will be studied: maintenance hosts (natural reservoirs of the virus) and bridge hosts (birds linking maintenance hosts to target populations). The data will encompass features ranging from seasonal waterfowl migration drivers (land surface temperature and vegetation) to a key agent affecting virus infectivity (surface water temperature). The temporal scope will be isolated to the wintering period for maintenance hosts (mid-October through January). Given characteristics associated with host presence and high infectivity in addition to host daily range, a risk score will be calculated for raster cells based on either similarity or proximity to hosts, resulting in a composite risk raster for the county indicating seasonal spillover risk from a prominent [waterfowl habitat](https://wildlife.ca.gov/Lands/Places-to-Visit/Yolo-Bypass-WA).

<img width="672" alt="yolo_county_and_bypass" src="https://github.com/user-attachments/assets/d80edea3-df9a-46a1-8d2b-df4b60c66611" />

## Data Description

[U.S. Geological Survey Daily Values Service](https://waterservices.usgs.gov/docs/dv-service/daily-values-service-details) maintains current and historical data from time-series equipment at monitoring water sites. [CACHE C OUTFLOW FROM SETTLING BASIN NR WOODLAND CA](https://waterdata.usgs.gov/monitoring-location/11452900) site was selected to obtain daily water temperature (°C) values provided in 30 minute intervals. 

[GBIF Occurrence](https://doi.org/10.15468/dl.jqrwjf) data was retrived from the Global Biodiversity Information Facility Occurrence Store and scoped to the wintering period and habitat. There are 105 occurrences across seven species.

## Data Citation

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: House Sparrow* [Data set]. https://doi.org/10.15468/dl.m5wyf6

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Killdeer* [Data set]. https://doi.org/10.15468/dl.ju8c56

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Mallard* [Data set]. https://doi.org/10.15468/dl.zu2sa4

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Red-winged Blackbird* [Data set]. https://doi.org/10.15468/dl.nmukt7

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Rock Pigeon* [Data set]. https://doi.org/10.15468/dl.ac99st

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Savannah Sparrow* [Data set]. https://doi.org/10.15468/dl.hekvd4

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Snow Goose* [Data set]. https://doi.org/10.15468/dl.kdaytc

USGS Daily Values Service. (2025). *CACHE C OUTFLOW FROM SETTLING BASIN NR WOODLAND CA* [Data set]. https://waterdata.usgs.gov/monitoring-location/11452900

## Methods

The most recent wintering period for migratory waterfowl (10/20/2024-01/31/2025) was studied using the [USGS Daily Values Service](https://waterservices.usgs.gov/docs/dv-service/daily-values-service-details), querying for surface water temperature from a [main habitat inlet](https://waterdata.usgs.gov/monitoring-location/11452900). Daily mean, minimum, and maxium temperature values were calculated and displayed concurrently with holoviews. 

Synanthropic species associated with agricultural environments in North America (Owen et al., 2021) and [observed in Yolo Bypass Wildlife Area](https://ebird.org/hotspot/L443535/bird-list), encompassing species in the orders Charadriiformes (shorebirds), Anseriformes (ducks and geese), Columbiformes (pigeons and doves), and Passeriformes (perching birds), were targeted for the county. The species occurrences data was accessed by the Python client for the [GBIF API](https://techdocs.gbif.org/en/openapi/v1/occurrence#/) and subset for the temporal scope, species of interest, and habitat coordinates. Each occurrences CSV file was ingested using the [pandas](https://pandas.pydata.org/) library. Species occurrence was normalized by month for the sampling effort and reduced to four species: *Agelaius phoeniceus*, *Anser caerulescens*, *Charadrius vociferus*, and *Passerculus sandwichensis*. Both daily and monthly observations for the four species were plotted over the winter period.


Run locally
----

### Download/Clone Git Repository

    $cd <replace with desired location of project folder>
    $git clone https://github.com/lauren-alexandra/zoonosis-risk.git
    $cd zoonosis-risk

### Create Environment

    $conda create -n myenv python=3.13.2
    $conda activate myenv

### Install required packages

    $conda install pip conda-forge::dask conda-forge::ipywidgets
    $pip install -r requirements.txt

### Set up Jupyter Notebook Kernel

    $pip install --user ipykernel
    $python -m ipykernel install --user --name=myenv

### Launch Jupyter Notebook

    (in git bash or other conda environment)
    $jupyter notebook
