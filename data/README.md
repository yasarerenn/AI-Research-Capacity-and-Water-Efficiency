# Data

Two versions of the replication data are used in this project:

- **Final_Data.xlsx** — human-readable workbook containing source documentation, variables, source extracts, the merged country-year panel, and sample-construction information.
- **analysis_data.csv** — machine-readable export of the `Analysis_Data` sheet used directly by the Python scripts.

The small files **variables.csv** and **sample_summary.csv** are convenience exports of the corresponding workbook sheets.

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

- Matched country-year grid: **1,464 observations, 183 countries**
- Total WUE available: **1,336 observations, 167 countries**
- Baseline estimation sample: **1,156 observations, 151 countries**
- Water-stress moderation sample: **1,086 observations, 142 countries**
- Balanced baseline sample: **1,072 observations, 134 countries**
- Balanced moderation sample used in robustness checks: **1,016 observations, 127 countries**

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

The main AI measure is the annual number of AI-related scientific articles per million people. The model uses `ln(1+x)`.

For measurement sensitivity, private AI investment and AI patent applications are divided by population in millions and transformed as `ln(1+x)`.

### WRI Aqueduct 4.0

**Variable:** Baseline Water Stress  
**Use in the study:** structural water-stress context and interaction term  
**Source:**  
https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators

The country-level score is treated as time invariant and centered at the estimation-sample mean before interaction.

### World Development Indicators

**Provider:** World Bank  
**Source:**  
https://databank.worldbank.org/source/world-development-indicators

Variables include population, GDP per capita, agriculture and industry shares of GDP, urbanization, internet use, trade openness, scientific publications, R&D expenditure, researcher intensity, and renewable internal freshwater resources per capita.

The alternative freshwater specification uses `ln(1 + renewable internal freshwater resources per capita)`, which retains valid zero values.

## Notes on redistribution

The workbook documents the original sources and transformations used in the study. Original third-party source files should only be redistributed where their terms of use permit it. When redistribution is restricted or unnecessary, users can reconstruct the relevant inputs from the source information reported in the workbook and this README.
