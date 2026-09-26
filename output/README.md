# Output

This folder contains the numerical output reproduced from the replication scripts.

Current files:

- `table2_descriptive_statistics.csv` — descriptive statistics for the main moderation sample.
- `diagnostic_vif.csv` — variance inflation factors for the transformed main regressors.
- `mundlak_joint_test.csv` — joint test of equality between the within- and between-country coefficients for the seven time-varying regressors.
- `table3_main_models.csv` — the three main total-WUE models.
- `table4_sectoral_models.csv` — total, agricultural, industrial, and services WUE moderation models.
- `table5_robustness.csv` — sample, regional, control, and zero-coding robustness checks.
- `measurement_sensitivity.csv` — private AI investment, AI patent, and freshwater-context sensitivity estimates.

Running `python run_all.py` recreates these files from `data/analysis_data.csv`.
