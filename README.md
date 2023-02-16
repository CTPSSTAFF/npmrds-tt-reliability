# npmrds-tt-reliability
Repository for tools to calculate NPMRDS level of travel-time reliability (LOTTR) metric for all TMCs in the Boston MPO region.
This repository contains:
* a Jupyter notebook to calcuate the LOTTR metric for all vehicles
* a Jupyter notebeook to calculate the LOTTR metric for trucks

## All vehicles
The methodology for calculating the level of travel-time reliabililty (LOTTR) metric for all vehicles from NPMRDS data is documented in the FHWA document  
[National Performance Measures for Congestions, Reliability, and Freight, and CMAQ Traffic Congestion](https://www.fhwa.dot.gov/tpm/guidance/hif18040.pdf).

In summary, we:
1. Calculate the LOTTR metric for each TMC for each of the four National Highway Performance (time) Periods for all vehicles, and then
2. Caclulate the single MPO region-wide LOTTR metric from \(1\).

The 4 National Highway Performance Program time periods for "all vehicles" are:
* Weekdays 6 AM to 10 AM
* Weekdays 10 AM to 4 PM
* Weedkays 4 PM to 8 PM
* Weekends 6 AM to 8 PM

### Inputs
#### Required input 1: speed and travel-time data
This notebook uses travel-time data downloaded from the NPMRDS Analytics Probe Data Analytics Portal in [RITIS](https://ritis.org).  

The specification of the data to download from RITS is as follows:
* All NPMRDS TMCs in the Boston Region MPO area. This list of TMCs is found in the file __brmpo\_npmrds\_tmcs\_2019.txt__.
* January 1, 2019 through December 31, 2019, from 6:00 AM to 8:00 PM
* With data aggregated in 15 minute units

The user needs to have downloaded this data from RITIS and extracted the CSV file containing speed and travel-time data from teh ZIP archive delivered by the npmrds-analytics email system.  

The location of this CSV file is specified by the variable __ritis\_data\_csv__.

#### Required input 2: DBF file containing attribute table for NPMRDS shapefile
The location of this input is given by the variable __tmc\_attr\_table\_dbf__.

### Formula
This single regional LOTTR metric for all vehicles is given by the formula:
$$
{NHPP\_Reliability\_Measure} = \frac{\sum \limits _{r=1} ^{R} {SL}_{i} * {AV}_{i} * {OF}_{j}} {\sum \limits _{t=1} ^{T} {SL}_{i} * {AV}_{i} * {OF}_{j}}
$$

Where:  
${SL}_{i}$ = the segment length of the reporting segment _i_ \(nearest thousandth\) for the highway system considered.  
$ {AV}_{i}$ = annual traffic volume of reporting segment _i_. \(See below.\)  
$ {OF}_{j}$ = occupancy factor for vehicles on the NHS with a specific geographic area _j_ within the State / Metropolitan planning area. \(This value is 1.7 for Massachusetts.\)  
__R__ = total number of Interstate and non-Interstate reporting segments exhibiting an LOTTR below 1.50 for all 4 time periods.  
__T__ = total number of Interstate and non-Interstate reporting segments.

And,  
$ {AV}_{j}$ = AADT * Directional_Factor * 365  

Where:
Directional_Factor is 0.5 if the _faciltype_ of the TMC is 2 or 6, and is 1 if the _faciltype_ of the TMC is 1. 

## Trucks
