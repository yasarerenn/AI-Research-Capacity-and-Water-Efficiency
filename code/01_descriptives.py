from pathlib import Path
import math

import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

from model_utils import load_data, write_csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "analysis_data.csv"
OUT = ROOT / "output"

rows = [r for r in load_data(DATA) if r["main_moderation_sample"] == 1]

variables = [
    ("ln(Economic WUE)", lambda r: r["ln_wue_total"]),
    ("ln(1 + AI articles per million)", lambda r: r["ln_ai_articles_pm"]),
    ("Baseline water stress", lambda r: r["water_stress_score_clean"]),
    ("ln(GDP per capita)", lambda r: math.log(r["gdp_pc"])),
    ("Agriculture share of GDP (%)", lambda r: r["agri_share"]),
    ("Industry share of GDP (%)", lambda r: r["industry_share"]),
    ("Urbanization (%)", lambda r: r["urban_share"]),
    ("Internet use (%)", lambda r: r["internet_share"]),
    ("Trade openness (%)", lambda r: r["trade_share"]),
]

summary = []
for label, getter in variables:
    values = np.asarray([getter(r) for r in rows], dtype=float)
    summary.append([
        label,
        len(values),
        values.mean(),
        values.std(ddof=1),
        values.min(),
        values.max(),
    ])

write_csv(
    OUT / "table2_descriptive_statistics.csv",
    ["Variable", "N", "Mean", "SD", "Minimum", "Maximum"],
    summary,
)

X = np.asarray([
    [
        r["ln_ai_articles_pm"],
        math.log(r["gdp_pc"]),
        r["agri_share"],
        r["industry_share"],
        r["urban_share"],
        r["internet_share"],
        r["trade_share"],
    ]
    for r in rows
], dtype=float)
X = np.column_stack([np.ones(len(X)), X])

vif_names = [
    "ln_ai_articles_pm", "ln_gdp_pc", "agri_share", "industry_share",
    "urban_share", "internet_share", "trade_share",
]
vifs = [[name, variance_inflation_factor(X, i + 1)] for i, name in enumerate(vif_names)]
write_csv(OUT / "diagnostic_vif.csv", ["Variable", "VIF"], vifs)

print(f"Descriptive statistics: N={len(rows)}")
print(f"VIF range: {min(x[1] for x in vifs):.2f} to {max(x[1] for x in vifs):.2f}")
