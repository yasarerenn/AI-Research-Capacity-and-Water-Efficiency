# AI Research Capacity and Water Efficiency

This repository contains replication materials for the manuscript:

**Artificial Intelligence Research Capacity and Economic Water Use Efficiency: Associations Within and Between Countries under Structural Water Stress**

The study examines whether national artificial intelligence (AI) research capacity is associated with economic water-use efficiency (WUE), and whether this relationship varies with structural water stress. The analysis covers 2016–2023, distinguishes within-country changes from between-country differences using a Mundlak specification, and examines sectoral heterogeneity in agricultural, industrial, and services WUE.

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
├── DATA_SOURCES_AND_LICENSES.md
├── LICENSE-CODE.md
├── requirements.txt
├── run_all.py
├── code/
│   ├── README.md
│   ├── model_utils.py
│   ├── 01_descriptives.py
│   ├── 02_main_models.py
│   ├── 03_sectoral_models.py
│   ├── 04_robustness.py
│   └── 05_figures.py
├── data/
│   ├── README.md
│   ├── Final_Data.xlsx
│   ├── analysis_data.csv
│   ├── variables.csv
│   └── sample_summary.csv
├── figures/
│   ├── README.md
│   ├── Figure_1_sample_construction.png
│   ├── Figure_2_marginal_relationship.png
│   └── Figure_3_sectoral_heterogeneity.png
└── output/
    ├── README.md
    ├── diagnostic_vif.csv
    ├── measurement_sensitivity.csv
    ├── mundlak_joint_test.csv
    ├── table2_descriptive_statistics.csv
    ├── table3_main_models.csv
    ├── table4_sectoral_models.csv
    └── table5_robustness.csv
```

## Replication workflow

The analysis scripts are written in Python. They start from the released analytical dataset, `data/analysis_data.csv`. They do **not** automatically re-download the original FAO, ETO/CSET, WRI, or World Bank source datasets or rebuild the merged analytical file from those raw sources.

Install the tested package versions:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python run_all.py
```

The scripts reproduce the descriptive statistics, the three main Mundlak models, sectoral models, robustness checks, measurement-sensitivity analyses, and the analytical content underlying Figures 1–3. Tables and diagnostic output are written to `output/`. The PNG files in `figures/` are the final manuscript versions; `code/05_figures.py` generates equivalent analytical figures as SVG files.

The current workflow has been checked against the manuscript results. In particular, it reproduces the main between-country AI research capacity × water stress interaction for total WUE (β ≈ 0.085, SE ≈ 0.029) and industrial WUE (β ≈ 0.156, SE ≈ 0.042), together with the reported sample sizes and R² values.

**Tested environment:** Python 3.13.5, NumPy 2.3.5, statsmodels 0.14.6, and Matplotlib 3.10.8.

## Replication data

**Final_Data.xlsx** is the human-readable replication workbook. **analysis_data.csv** is the machine-readable version of its `Analysis_Data` sheet used directly by the scripts. The workbook also contains source notes, variable definitions, country identifiers, source extracts, and sample-construction information.

See `data/README.md` for details.

## Data sources and licensing

The project combines:

- FAO SDG Indicator 6.4.1 water-use efficiency data;
- ETO/CSET Country AI Activity Metrics, Version 1.12.0;
- WRI Aqueduct 4.0 Baseline Water Stress;
- World Bank World Development Indicators.

The repository does not relicense third-party data. Source-specific terms and attribution requirements remain applicable. See `DATA_SOURCES_AND_LICENSES.md` for details.

The analysis code is released under the MIT License as described in `LICENSE-CODE.md`.

## Author

**Yaşar Eren**  
Tarsus University, School of Graduate Studies, Department of Business Administration  
ORCID: https://orcid.org/0009-0004-7795-0001

## Citation

A formal article citation will be added after publication. Repository citation metadata are provided in `CITATION.cff`.

## Contact

244107010@tarsus.edu.tr
