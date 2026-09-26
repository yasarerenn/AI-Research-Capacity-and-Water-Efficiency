# Data

The replication workbook used for this project is **Final_Data.xlsx**. It brings together the data documentation, source extracts, merged analytical panel, and sample-construction information used in the manuscript.

## Workbook contents

| Sheet | Contents |
|---|---|
| `README` | Short description of the workbook and its organization |
| `Sources` | Source names, versions, coverage, and source links |
| `Variables` | Variable definitions, units, transformations, and notes |
| `Countries` | Country names and ISO3 identifiers |
| `FAO_WUE` | Total, agricultural, industrial, and services water-use efficiency |
| `AI_Metrics` | AI publication and related activity measures |
| `Water_Stress` | WRI Aqueduct 4.0 baseline water-stress measures |
| `WDI_Controls` | World Development Indicators used as model controls |
| `WDI_Research` | Research-capacity indicators used in robustness analyses |
| `WDI_Metadata` | WDI series names, codes, and metadata |
| `Analysis_Data` | Merged country-year analytical panel |
| `Sample_Summary` | Sample-construction counts and countries without total WUE observations |

## Sample construction

The workbook records the following sequence:

- Matched country-year grid: **1,464 observations, 183 countries**
- Total WUE available: **1,336 observations, 167 countries**
- Baseline estimation sample: **1,156 observations, 151 countries**
- Water-stress moderation sample: **1,086 observations, 142 countries**
- Balanced baseline sample: **1,072 observations, 134 countries**

## Source datasets

### FAO SDG Indicator 6.4.1

**Indicator:** Change in water-use efficiency over time  
**Use in the study:** total economic WUE and agricultural, industrial, and services WUE  
**Study period:** 2016–2023  
**Official source:**  
https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/641-change-in-water-use-efficiency-over-time/

The WUE measures are transformed using the natural logarithm in the regression models.

### Country AI Activity Metrics, v1.12.0

**Provider:** Emerging Technology Observatory / Center for Security and Emerging Technology  
**Version:** 1.12.0  
**Zenodo record:** https://doi.org/10.5281/zenodo.22772306  
**Documentation:** https://eto.tech/dataset-docs/country-ai-activity-metrics/

The main AI measure is the annual number of AI-related scientific articles per million people. The transformed measure used in the models is `ln(1+x)`.

### WRI Aqueduct 4.0

**Variable:** Baseline Water Stress  
**Use in the study:** structural water-stress context and interaction term  
**Source:**  
https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators

The country-level indicator is treated as time invariant over the study period and is mean centered before interaction with the within- and between-country AI components.

### World Development Indicators

**Provider:** World Bank  
**Source:**  
https://databank.worldbank.org/source/world-development-indicators

Variables include population, GDP per capita, agriculture and industry shares of GDP, urbanization, internet use, trade openness, R&D expenditure, researcher intensity, and renewable internal freshwater resources per capita.

## Notes on redistribution

The workbook documents the original sources and the transformations used in the study. Original third-party source files should only be redistributed where their terms of use permit it. When redistribution is restricted or unnecessary, users can reconstruct the relevant inputs from the source information reported in the workbook and this README.
