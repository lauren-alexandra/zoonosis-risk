# Zoonosis Risk

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15225925.svg)](https://doi.org/10.5281/zenodo.15225925)

<img src="images/black-necked_stilts_ca_rice_commission.png" alt="Black-necked stilts forage in wet rice fields" width="800" height="500" longdesc="https://www.ucdavis.edu/sites/default/files/media/images/9127201758-024b4c82d0-o.jpg" />

#### Overview

How do natural sources of highly pathogenic avian influenza (HPAI) at the wildlife–agriculture interface influence spillover risk in California's Central Valley?

During late 2021, the HPAI outbreak commenced in North America and circulated among 165 wild bird species with a broader host range than the 2014-2015 outbreak. Waterfowl have consistently tested positive for the influenza in addition to [new hosts](https://www.usgs.gov/media/files/nwhc-wildlife-health-bulletin-avian-influenza-update): previously unaffected wild birds, wild and domestic mammals, and humans. The HPAI H5N1 virus has demonstrated some mammalian mutations and been found in over 1,600 poultry operations in every U.S. state and Puerto Rico, almost 1,000 dairy farms in 17 states, and 70 humans. In the state of California, occupational exposure to dairy cows and poultry with suspected HPAI increases the individual risk of infection. The first [human case of HPAI](http://dx.doi.org/10.15585/mmwr.mm7408a1) in the state was identified in September 2024 by monitoring workers on farms with infected cows. From September 30–December 24, 2024, 38 persons tested positive for HPAI A(H5N1); of those individuals, 37 worked on a dairy farm and one was a child with an unknown exposure, marking the first pediatric case in the U.S. 

On December 18, 2024, California Governor Gavin Newsom declared a [State of Emergency](https://www.gov.ca.gov/wp-content/uploads/2024/12/CORRECT-ATTESTED.pdf) for H5N1. The state has recruited local, state, and federal technical and operational expertise to facilitate a robust response to the virus including the U.S. Food and Drug Administration, U.S. Department of Agriculture, Centers for Disease Control, and California Department of Public Health. With each animal that is infected by avian influenza, there is another chance for the virus to evolve into a pathogen fit for human-to-human transmission. Creating early warning systems built on a [One Health](https://ohi.vetmed.ucdavis.edu/about/one-health) framework–integrating human, animal, and environmental health–are a wise investment to support state biosecurity. 

Since 2006, the USDA National [Wildlife Disease Program](https://www.cdfa.ca.gov/AHFSS/animal_health/Wildlife_Services.html#:~:text=The%20Wildlife%20Services%20Program%20is%20a%20partnership,breaks%20or%20the%20compromise%20of%20other%20infrastructure**) (NWDP) in partnership with the California Department of Food and Agriculture has established a surveillance framework sampling wild birds for HPAI and other pathogens that may impact domestic poultry, wild bird species, and humans. NWDP wildlife disease biologists serve as sentinels in the program’s Surveillance and Emergency Response System (SERS) and have collected over 500,000 samples to date. Existing disease surveillance frameworks like SERS can be bolstered to account for environmental conditions, host behavior, and community dynamics, informing conservation strategies for timely interventions that safeguard human and animal health.

Central Valley

[California's Central Valley](https://ca.water.usgs.gov/projects/central-valley/about-central-valley.html) is bifurcated into two valleys: Sacramento Valley and San Joaquin Valley. Every year approximately 1 billion wild birds migrate through them on the [Pacific Flyway](https://www.sacramentoaudubon.org/pacific-flyway-conservation). The flyway encompasses a system of wetlands ranging from Alaska and western Canada to the western U.S. and Mexico to Central America and South America. Wetlands, ecosystems that are transitional between the terrestrial and the aquatic, within the Central Valley provide wintering habitat for nearly 60 percent of migratory waterfowl (Garone, 2020).

HPAI Hosts

Wild birds in the Orders Anseriformes (ducks and geese) and Charadriiformes (shorebirds) are the primary hosts of avian influenza viruses, however they can also disseminate the virus to intermediate hosts. For a species to be considered a bridge host, it must: overlap in time and space with maintenance hosts, either replicate a given pathogen within the body or transport the pathogen on its body surface, and lack the capacity to persist a virus without first being infected by a maintenance host (Owen et al., 2021). Thus, assessing species use of habitat, contact rate, and behavior across spatial and temporal scales is necessary for a bridge host designation. A potential bridge host may [spread the virus to poultry and cows](https://www.nature.com/articles/srep36237) by entering farms through building breaches and vents, periods of open doors, or open-air environments, contaminating the feed and water. 

Project Objective

The project will explore the county in Central Valley with the highest HPAI detection in wild birds which is Yolo County, nested within the smaller Sacramento Valley. Two sources of pathogen transmission will be studied in synanthropic wild birds: maintenance hosts (natural reservoirs of the virus) and bridge hosts (birds linking maintenance hosts to target populations). The data will encompass features ranging from vegetation to a key agent affecting virus infectivity (surface water temperature). The temporal scope will be isolated to the wintering period for maintenance hosts (mid-October through January). Given characteristics associated with host presence and high infectivity in addition to host daily range, a risk score will be calculated for raster cells based on either similarity or proximity to hosts, resulting in a composite risk raster for the county indicating seasonal spillover risk from a prominent [waterfowl habitat](https://wildlife.ca.gov/Lands/Places-to-Visit/Yolo-Bypass-WA).

<img width="672" alt="yolo_county_and_bypass" src="https://github.com/user-attachments/assets/d80edea3-df9a-46a1-8d2b-df4b60c66611" />

#### Data Description

[GBIF Occurrence](https://doi.org/10.15468/dl.jqrwjf) data was retrived from the Global Biodiversity Information Facility Occurrence Store and scoped to the wintering period and habitat. There are 105 occurrences across seven species.

[U.S. Geological Survey Daily Values Service](https://waterservices.usgs.gov/docs/dv-service/daily-values-service-details) maintains current and historical data from time-series equipment at monitoring water sites. [CACHE C OUTFLOW FROM SETTLING BASIN NR WOODLAND CA](https://waterdata.usgs.gov/monitoring-location/11452900) site was selected to obtain daily water temperature (°C) values provided in 30 minute intervals.

Yolo County and Yolo Bypass Wildlife Area boundaries were retrieved from the California State Geoportal. [California County Boundaries](https://gis.data.ca.gov/datasets/8713ced9b78a4abb97dc130a691a8695_0/explore?location=36.651235%2C-119.002032%2C6.22) is a GIS layer hosted by the California Department of Forestry and Fire Protection. [CDFW Public Access Lands](https://gis.data.ca.gov/datasets/b3b6dd29b34247dbb2dd773ea17cc82d_0/explore?location=38.549943%2C-121.691363%2C11.00) dataset offers locations which are publicly accessible lands owned or operated by the California Department of Fish and Wildlife.

#### Data Citation

California State Geoportal. (2024). *California County Boundaries* [Data set]. https://gis.data.ca.gov/datasets/CALFIRE-Forestry::california-county-boundaries

California State Geoportal. (2025). *CDFW Public Access Lands* [Data set]. https://gis.data.ca.gov/datasets/CDFW::cdfw-public-access-lands-ds3077

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: House Sparrow* [Data set]. https://doi.org/10.15468/dl.m5wyf6

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Killdeer* [Data set]. https://doi.org/10.15468/dl.ju8c56

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Mallard* [Data set]. https://doi.org/10.15468/dl.zu2sa4

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Red-winged Blackbird* [Data set]. https://doi.org/10.15468/dl.nmukt7

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Rock Pigeon* [Data set]. https://doi.org/10.15468/dl.ac99st

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Savannah Sparrow* [Data set]. https://doi.org/10.15468/dl.hekvd4

Global Biodiversity Information Facility. (2025). *GBIF Occurrence Download: Snow Goose* [Data set]. https://doi.org/10.15468/dl.kdaytc

USGS Daily Values Service. (2025). *CACHE C OUTFLOW FROM SETTLING BASIN NR WOODLAND CA* [Data set]. https://waterdata.usgs.gov/monitoring-location/11452900

#### Methods

The most recent wintering period for migratory waterfowl (10/20/2024-01/31/2025) was studied using the [USGS Daily Values Service](https://waterservices.usgs.gov/docs/dv-service/daily-values-service-details), querying for surface water temperature from a [main habitat inlet](https://waterdata.usgs.gov/monitoring-location/11452900). Daily mean, minimum, and maxium temperature values were calculated and displayed concurrently with holoviews. 

The species occurrences data was accessed by the Python client for the [GBIF API](https://techdocs.gbif.org/en/openapi/v1/occurrence#/) and subset for the temporal scope, species of interest, and habitat coordinates. Each occurrences CSV file was ingested using the [pandas](https://pandas.pydata.org/) library. Species occurrence was normalized by month for the sampling effort and reduced to four species: *Agelaius phoeniceus*, *Anser caerulescens*, *Charadrius vociferus*, and *Passerculus sandwichensis*. Both daily and monthly observations for the four species were plotted over the winter period.

#### Discussion

Seasonal patterns of HPAI spillover risk will be complicated by changes in climate and loss of suitable overwintering habitat. The reduction of wetlands due to extended drought will relocate significant concentrations of waterfowl toward constructed refuges and flooded agricultural lands, resulting in the emergence of more frequent and larger outbreaks of avian disease. In the non-breeding season, changes in environmental conditions may support increased contact between wild birds and domestic birds in agricultural areas, generating opportunity for viral reassortment and subsequently, new host species (Morin et al., 2018). At present the Yolo Bypass Wildlife Area inlet offers favorable conditions for a high HPAI infectivity rate from late November to February, comprising the majority of the migratory wintering period. However, warming could lessen the duration of infectivity for cold-adapted pathogens both in breeding and non-breeding waters, leading transmission to be influenced more by co-occurrence with shedding waterfowl (Hill et al., 2016). The timing and patterns of migration as well as the availability of food resources will also adjust with warming and produce overwintering sites with greater densities of waterfowl, still vulnerable to substantial outbreaks. 

Synanthropic species associated with agricultural environments in North America (Owen et al., 2021) and [observed in Yolo Bypass Wildlife Area](https://ebird.org/hotspot/L443535/bird-list), encompassing species in the Orders Charadriiformes (shorebirds), Anseriformes (ducks and geese), Columbiformes (pigeons and doves), and Passeriformes (perching birds), were targeted for the county. After the data were normalized, the species scope was reduced to the following: Snow Goose, Savannah Sparrow (passerine), Red-winged Blackbird (passerine), and Killdeer (shorebird). In the Sacramento Valley and in the greater Central Valley, Northern Shovelers (ducks) have demonstrated the highest avian influenza prevalence and have been identified as a key species to target for future sampling (Bianchini et al., 2021). The structure of HPAI transmission requires a more expansive surveillance however that goes beyond maintenance hosts to encompass bridge hosts. Sampling of peridomestic species such as passerines has occurred in natural settings and settings for resident maintenance hosts, but there have been few instances of sampling in areas either regularly visited by waterfowl or adjacent to or on poultry and dairy farms (Shriner et al., 2016). The identification of bridge hosts within a given area requires simultaneously testing both on wetlands and nearby farms. The presence and use of agricultural operations by wild birds is not as well studied in the Americas as in other regions, and consequently, a framework for HPAI transmissions in such operations is diminished (Owen et al., 2021). Bridge hosts can amplify the speed and severity of infections; one study of wild birds on farms and wetlands (Caron et al., 2014) found that maintenance hosts and target populations were 20 times more likely to connect through bridge hosts than direct contact. Another study (Gaukler et al., 2012) surveyed the behavior of a synanthropic passerine species and noted that there is an additional risk posed by them: potential bridge hosts may frequent multiple farms rather than targeting just one for resources, thereby accelerating pathogen dispersal and the chances of a wider outbreak. More species-specific studies of likely bridge hosts and their use of farms are required for a stronger understanding of spatial and temporal dynamics regarding between-host processes and HPAI transmission in California's Central Valley. Evidenced by these findings, the project will concentrate future analysis and modeling on these elements: 1) Cultivating a deeper understanding of bridge host behavior in Yolo County and across the Central Valley; 2) Analyzing the impact of changes in vegetation on host foraging; 3) Incorporating climate projections for the county to inform the risk assessment and conservation planning; and 4) Developing monthly risk assessments for target species in the wintering season to better track HPAI transmission between the county community.

#### References

Bianchini, E. A., Bogiatto, R. J., Donatello, R. A., Casazza, M. L., Ackerman, J. T., De La Cruz, S. E. W., … Cline, T. D. (2021). Host correlates of avian influenza virus infection in wild waterfowl of the Sacramento Valley, California. *Avian Diseases, 66*(1), 20-28. https://doi.org/10.1637/aviandiseases-D-21-00071

Brown, J. D., Goekjian, G., Poulson, R., Valeika, S., & Stallknecht, D. E. (2009). Avian influenza virus in water: Infectivity is dependent on pH, salinity and temperature. *Veterinary Microbiology, 136*(1-2), 20-26. https://doi.org/10.1016/j.vetmic.2008.10.027

California Department of Food and Agriculture. (n.d.). *Wildlife Services Program*. https://www.cdfa.ca.gov/AHFSS/animal_health/Wildlife_Services.html

California Department of Public Health. (n.d.). *Bird flu*. https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/Bird-Flu.aspx

California Water Science Center. (n.d.). *California's Central Valley*. USGS. https://ca.water.usgs.gov/projects/central-valley/about-central-valley.html 

Caron, A., Grosbois, V., Etter, E., Gaidet, N., & de Garine-Wichatitsky, M. (2014). Bridge hosts for avian influenza viruses at the wildlife/domestic interface: an eco-epidemiological framework implemented in southern Africa. *Preventive Veterinary Medicine, 117*(3-4), 590-600. https://doi.org/10.1016/j.prevetmed.2014.09.014

Chamberlain, S. (2024). *pygbif* (Version 0.6.4) [Computer software]. GitHub. https://github.com/gbif/pygbif/releases/tag/v0.6.4

Cornell Lab of Ornithology (n.d.). *Yolo Bypass Wildlife Area*. eBird. https://ebird.org/hotspot/L443535/bird-list 

Executive Department State of California. (2024, December 18). *Proclamation of a State of Emergency*. Governor Gavin Newsom. https://www.gov.ca.gov/wp-content/uploads/2024/12/CORRECT-ATTESTED.pdf 

Garone, P. (2020). *The fall and rise of the wetlands of California's great Central Valley*. University of California Press.

Gaukler, S. M., Homan, J. H., Linz, G. M., & Bleier, W. J. (2012). Using radio-telemetry to assess the risk European Starlings pose in pathogen transmission among feedlots. *Human–Wildlife Interactions, 6*(1), 30-37. https://doi.org/10.26077/mtpq-ht61

Hill, N. J., Ma, E. J., Meixell, B. W., Lindberg, M. S., Boyce, W. M., & Runstadler, J. A. (2016). Transmission of influenza reflects seasonality of wild birds across the annual cycle. *Ecology Letters, 19*, 915–925. https://doi.org/10.1111/ele.12629

Jordahl, K., Van den Bossche, J., Fleischmann, M., Wasserman, J., McBride, J., Gerard, J., … Leblanc, F. (2024). *geopandas/geopandas: v1.0.1* (Version 1.0.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.12625316 

Met Office. (2024). *Cartopy: a cartographic python library with a Matplotlib interface* (Version 0.24.1) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.13905945

Morin, C. W.., Stoner-Duncan, B., Winker, K., Scotch, M., Hess, J. J., Meschke, J. S., … Rabinowitz, P. M. (2018). Avian influenza virus ecology and evolution through a climatic lens. *Environment International, 119*, 241-249. https://doi.org/10.1016/j.envint.2018.06.018

One Health Institute. (n.d.). *What is One Health?*. University of California Davis School of Veterinary Medicine. https://ohi.vetmed.ucdavis.edu/about/one-health

Owen, J. C., Hawley, D. M., & Huyvaert, K. P. (Eds.). (2021). *Infectious disease ecology in wild birds.* Oxford University Press.

Python Software Foundation. (2024). *Python* (Version 3.13.2) [Computer software]. https://docs.python.org/release/3.12.6 

Sacramento Audubon Society. (n.d.). *Pacific Flyway conservation*. https://www.sacramentoaudubon.org/pacific-flyway-conservation

Shriner, S. A., Root, J. J., Lutman, M. W., Kloft, J. M., VanDalen, K. K., Sullivan, H. J., … DeLiberto, T. J. (2016). Surveillance for highly pathogenic  H5 avian influenza virus in  synanthropic wildlife associated  with poultry farms during an acute  outbreak. *Scientific Reports, 6*, 1-11. https://doi.org/10.1038/srep36237

Rudiger, P., Liquet, M., Signell, J., Hansen, S. H., Bednar, J. A., Madsen, M. S., … Hilton, T. W. (2024). *holoviz/hvplot: Version 0.11.2* (Version 0.11.2) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.13851295 

The pandas development team. (2024). *pandas-dev/pandas: Pandas* (Version 2.2.3) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.3509134

White, L. (2025, March 18). *Winter 2025 update on highly pathogenic avian influenza H5*. USGS. https://www.usgs.gov/media/files/nwhc-wildlife-health-bulletin-avian-influenza-update

Yolo County Resource Conservation District. (n.d.). *Yolo Bypass Wildlife Area*. https://yolorcd.org/what-we-do/yolo-bypass-wildlife-area 

Zhu, S., Harriman, K., Liu, C., Kraushaar, V., Hoover, C., Shim, K., … California Department of Public Health H5 Laboratory Response Team (2025). Human cases of highly pathogenic avian influenza A(H5N1) — California, September–December 2024. *MMWR and Morbidity and Mortality Weekly Report, 74*, 127-133. http://dx.doi.org/10.15585/mmwr.mm7408a1


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
