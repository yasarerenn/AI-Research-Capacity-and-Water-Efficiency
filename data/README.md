# Data

This directory documents the source data used in the study and will contain replication-ready processed files where redistribution is permitted.

## Source datasets

### 1. FAO SDG Indicator 6.4.1

**Indicator:** Change in water-use efficiency over time  
**Use in the study:** total economic WUE and agricultural, industrial, and services WUE  
**Study period:** 2016–2023  
**Official source:**  
https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/641-change-in-water-use-efficiency-over-time/

The WUE measures are transformed using the natural logarithm in the regression models.

### 2. Country AI Activity Metrics, v1.12.0

**Provider:** Emerging Technology Observatory / Center for Security and Emerging Technology  
**Version:** 1.12.0  
**Zenodo record:** https://doi.org/10.5281/zenodo.22772306  
**Documentation:** https://eto.tech/dataset-docs/country-ai-activity-metrics/

The main AI measure is the annual number of AI-related scientific articles per million people. The analysis uses the general AI category and retains years marked as complete in the source data. The transformed measure is `ln(1+x)`.

### 3. WRI Aqueduct 4.0

**Variable:** Baseline Water Stress  
**Use in the study:** structural water-stress context and interaction term  
**Source:**  
https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators

The country-level indicator is treated as time invariant over the study period and is mean centered before interaction with the within- and between-country AI components.

### 4. World Development Indicators

**Provider:** World Bank  
**Source:**  
https://databank.worldbank.org/source/world-development-indicators

Variables used include population, GDP per capita, agriculture and industry shares of GDP, urbanization, internet use, trade openness, R&D expenditure, researcher intensity, and renewable internal freshwater resources per capita.

## Analytical samples

- AI-WUE matched sample: **1,336 observations, 167 countries**
- Main estimation sample: **1,156 observations, 151 countries**
- Moderation sample with valid baseline water stress: **1,086 observations, 142 countries**
- Balanced moderation sample used in robustness checks: **1,016 observations, 127 countries**

## Redistribution

Raw third-party files are not automatically included in this repository. Before any source file is uploaded, its redistribution terms should be checked. Where redistribution is restricted or unclear, this repository will provide reconstruction instructions rather than republishing the original file.

## Planned processed files

The final replication package may include processed analytical files created from the source datasets, subject to applicable terms of use. Each processed file will be accompanied by a variable dictionary and provenance notes.
