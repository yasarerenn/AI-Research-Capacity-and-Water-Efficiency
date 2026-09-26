# Code

This directory will contain the scripts used to reproduce the analytical workflow reported in the manuscript.

## Planned workflow

The scripts will be organized in execution order:

1. `01_data_preparation` — import, harmonize, transform, and merge the source datasets.
2. `02_main_models` — estimate the main Mundlak within-between models for total economic WUE.
3. `03_sectoral_models` — estimate agricultural, industrial, and services WUE models.
4. `04_robustness_checks` — reproduce alternative samples, alternative controls, and measurement-sensitivity analyses.
5. `05_figures` — reproduce the marginal-relationship and sectoral-heterogeneity figures.

Exact file extensions and software requirements will be added when the original analysis scripts are deposited.

## Estimation details

The main models:

- decompose time-varying explanatory variables into within-country and between-country components;
- include year fixed effects;
- use robust standard errors clustered by country;
- mean center baseline water stress before constructing the interaction terms;
- report marginal relationships with 95% confidence intervals for the moderation analysis.

## Reproduction order

Once the scripts are uploaded, this file will specify the exact command order and the expected input/output files for each step.
