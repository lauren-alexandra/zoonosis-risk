# Zoonosis Risk

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15225925.svg)](https://doi.org/10.5281/zenodo.15225925)

<img src="images/black-necked_stilts_ca_rice_commission.png" alt="Black-necked stilts forage in wet rice fields" width="760" height="500" longdesc="https://www.ucdavis.edu/sites/default/files/media/images/9127201758-024b4c82d0-o.jpg" />

## Overview

How do natural sources of highly pathogenic avian influenza (HPAI) at the wildlife–agriculture interface influence spillover risk in California's Central Valley?

With each animal that is infected, there is another chance for the influenza to evolve into a virus fit for human-to-human transmission. Creating early warning systems built on a One Health framework–integrating human, animal, and environmental health–are a wise investment to support state biosecurity. One Health surveillance systems can be incorporated into conservation strategies for timely interventions that safeguard human and animal health. 

This project will explore the county in the valley with the highest HPAI detection in wild birds which is Yolo County. Two sources of pathogen transmission will be studied: maintenance hosts (natural reservoirs of the virus) and bridge hosts (birds linking maintenance hosts to target populations). The data will encompass features ranging from seasonal waterfowl migration drivers (land surface temperature and vegetation) to a key agent affecting virus infectivity (surface water temperature). The temporal scope will be isolated to the wintering period for maintenance hosts (mid-October through January). Given characteristics associated with host presence and high infectivity in addition to host daily range, a risk score will be calculated for raster cells based on either similarity or proximity to hosts, resulting in a composite risk raster for the county indicating seasonal spillover risk from a prominent waterfowl habitat. 

<img width="672" alt="yolo_county_and_bypass" src="https://github.com/user-attachments/assets/d80edea3-df9a-46a1-8d2b-df4b60c66611" />

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
