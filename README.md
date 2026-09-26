# AI Research Capacity and Water Efficiency

This repository contains replication materials for the manuscript:

**Artificial Intelligence Research Capacity and Economic Water Use Efficiency: Associations Within and Between Countries under Structural Water Stress**

The study examines whether national artificial intelligence (AI) research capacity is associated with economic water-use efficiency (WUE), and whether this relationship varies with structural water stress. The analysis covers 2016–2023, distinguishes within-country changes from between-country differences using a Mundlak specification, and also examines sectoral heterogeneity in agricultural, industrial, and services WUE.

## Study design

- **Period:** 2016–2023
- **Unit of analysis:** country-year
- **Main outcome:** economic water-use efficiency based on FAO SDG Indicator 6.4.1
- **Main explanatory variable:** AI-related scientific publications per million people
- **Contextual variable:** WRI Aqueduct 4.0 Baseline Water Stress
- **Estimation strategy:** Mundlak within-between decomposition with country-clustered robust standard errors
- **Additional analyses:** sectoral WUE models, alternative samples, alternative AI indicators, and robustness checks

The main estimation sample contains **1,156 observations from 151 countries**. The water-stress moderation sample contains **1,086 observations from 142 countries**.

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── code/
│   └── README.md
├── data/
│   ├── README.md
│   └── Final_Data.xlsx
├── figures/
│   └── README.md
└── output/
    └── README.md
```

- **data/** contains the replication workbook and documentation for the data sources, variables, country coverage, analytical panel, and sample construction.
- **code/** will contain the scripts used for the main, sectoral, robustness, and figure analyses.
- **figures/** will contain the figures reproduced from the analysis workflow.
- **output/** will contain reproducible regression tables, diagnostics, and related model output.

## Replication data

The main replication workbook is **Final_Data.xlsx**. It contains the source extracts used in the study, variable documentation, country identifiers, the merged analytical panel, and a concise record of sample construction.

The workbook is organized into the following sheets:

- **README** — short description of the workbook
- **Sources** — source and version information
- **Variables** — variable names, definitions, units, and transformations
- **Countries** — country names and ISO3 identifiers
- **FAO_WUE** — total and sectoral water-use efficiency data
- **AI_Metrics** — AI research and related activity measures
- **Water_Stress** — WRI Aqueduct baseline water-stress data
- **WDI_Controls** — World Development Indicators used as controls
- **WDI_Research** — research-capacity indicators from WDI
- **WDI_Metadata** — WDI indicator metadata
- **Analysis_Data** — merged country-year panel used to construct the estimation samples
- **Sample_Summary** — sample-construction counts and country coverage

## Data sources

### FAO SDG Indicator 6.4.1

The study uses FAO data on **Change in water-use efficiency over time (SDG Indicator 6.4.1)** for total, agricultural, industrial, and services WUE.

https://www.fao.org/sustainable-development-goals-data-portal/data/indicators/641-change-in-water-use-efficiency-over-time/

### Country AI Activity Metrics

AI research capacity is measured using the **Country AI Activity Metrics, Version 1.12.0**, produced by the Emerging Technology Observatory / Center for Security and Emerging Technology.

Documentation:  
https://eto.tech/dataset-docs/country-ai-activity-metrics/

Zenodo record:  
https://doi.org/10.5281/zenodo.22772306

### WRI Aqueduct 4.0

Structural water stress is measured using the **Baseline Water Stress** indicator from **WRI Aqueduct 4.0**.

https://www.wri.org/research/aqueduct-40-updated-decision-relevant-global-water-risk-indicators

### World Development Indicators

Control variables are drawn from the **World Bank World Development Indicators (WDI)**.

https://databank.worldbank.org/source/world-development-indicators

## Reproducibility

The replication materials are being organized so that the analytical sample, reported models, and figures can be reconstructed from the documented data and code. Source files are redistributed only where their terms of use allow it; otherwise, the official source and reconstruction information are documented in the data folder.

## Planned reproducible outputs

The completed package is intended to reproduce:

- **Figure 1:** Sample Construction and Data Matching Process
- **Figure 2:** Conditional Between-Country Relationship Between AI Research Capacity and Total Economic WUE Across Levels of Baseline Water Stress
- **Figure 3:** Sectoral Heterogeneity in the Interaction Between AI Research Capacity and Baseline Water Stress
- main regression tables
- sectoral regression tables
- robustness analyses
- diagnostic outputs

## Author

**Yaşar Eren**  
Tarsus University, School of Graduate Studies, Department of Business Administration  
ORCID: https://orcid.org/0009-0004-7795-0001

## Citation

A formal article citation will be added after publication. Repository citation metadata are provided in `CITATION.cff`.

## Contact

244107010@tarsus.edu.tr
