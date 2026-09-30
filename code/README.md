# Code

The scripts in this folder reproduce the descriptive statistics, main models, sectoral models, robustness checks, measurement-sensitivity analyses, and the analytical content underlying the manuscript figures.

## Files

- `model_utils.py` — shared functions for loading the replication data, constructing the within and between components, estimating the Mundlak specifications, and writing output files.
- `01_descriptives.py` — Table 2 descriptive statistics and variance inflation factors.
- `02_main_models.py` — the three main total-WUE models and the Mundlak joint test.
- `03_sectoral_models.py` — total, agricultural, industrial, and services WUE moderation models.
- `04_robustness.py` — sample, control, regional, zero-coding, and measurement-sensitivity checks.
- `05_figures.py` — reproducible analytical versions of Figures 1–3.
- `../run_all.py` — runs the scripts in order.

## Software

The workflow was tested with:

- Python 3.13.5
- NumPy 2.3.5
- statsmodels 0.14.6
- Matplotlib 3.10.8

Install the tested package versions with:

```bash
python -m pip install -r requirements.txt
```

## Reproduction

The scripts start from `data/analysis_data.csv`, which is the released analytical dataset. Source-data acquisition and reconstruction of the merged panel from the original FAO, ETO/CSET, WRI, and World Bank files are documented in the workbook and data README but are not automated by these scripts.

From the repository root, run:

```bash
python run_all.py
```

The scripts write regression tables and diagnostics to `output/` and generate SVG versions of the figures in `figures/`.

## Model specification

The main specification:

- separates each time-varying regressor into within and between components;
- includes year fixed effects with 2016 as the reference year;
- uses OLS with standard errors clustered by country;
- centers baseline water stress at the estimation-sample mean;
- interacts centered water stress separately with the within and between components of AI research capacity.

The baseline controls are log GDP per capita, agriculture share of GDP, industry share of GDP, urbanization, internet use, and trade openness. The robustness script adds the alternative controls and sample restrictions described in the manuscript.
