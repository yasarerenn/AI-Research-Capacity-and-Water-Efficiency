# Code

The scripts in this folder reproduce the descriptive statistics, main models, sectoral models, robustness checks, measurement-sensitivity analyses, and figures reported in the manuscript.

## Files

- `model_utils.py` — shared functions for loading the replication data, constructing within- and between-country components, estimating the Mundlak specifications, and writing output files.
- `01_descriptives.py` — Table 2 descriptive statistics and variance inflation factors.
- `02_main_models.py` — the three main total-WUE models and the Mundlak joint test.
- `03_sectoral_models.py` — total, agricultural, industrial, and services WUE moderation models.
- `04_robustness.py` — sample, control, regional, zero-coding, and measurement-sensitivity checks.
- `05_figures.py` — Figures 1–3.
- `../run_all.py` — runs the scripts in order.

## Software

The scripts use Python 3 and the packages listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## Reproduction

Place `analysis_data.csv` in the `data/` folder and run from the repository root:

```bash
python run_all.py
```

The scripts write regression tables and diagnostics to `output/` and figures to `figures/`.

## Model specification

The main specification:

- separates each time-varying regressor into within-country and between-country components;
- includes year fixed effects with 2016 as the reference year;
- uses OLS with standard errors clustered by country;
- centers baseline water stress at the estimation-sample mean;
- interacts centered water stress separately with the within- and between-country AI components.

The baseline controls are log GDP per capita, agriculture share of GDP, industry share of GDP, urbanization, internet use, and trade openness. The robustness script adds the alternative controls and sample restrictions described in the manuscript.
