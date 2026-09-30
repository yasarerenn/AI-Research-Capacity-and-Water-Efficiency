from pathlib import Path
import numpy as np

from model_utils import fit_mundlak, load_data, term, write_csv

ROOT = Path(__file__).resolve().parents[1]
rows = load_data(ROOT / "data" / "analysis_data.csv")

m1 = fit_mundlak(
    rows, outcome="wue_total", flag="baseline_complete",
    include_controls=False, include_interactions=False,
)
m2 = fit_mundlak(
    rows, outcome="wue_total", flag="baseline_complete",
    include_controls=True, include_interactions=False,
)
m3 = fit_mundlak(
    rows, outcome="wue_total", flag="main_moderation_sample",
    include_controls=True, include_interactions=True,
)

terms = [
    ("AI research capacity, within component", "ln_ai_articles_pm_within"),
    ("AI research capacity, between component", "ln_ai_articles_pm_between"),
    ("Baseline water stress", "moderator_c"),
    ("AI within component and water stress interaction", "ai_within_x_mod"),
    ("AI between component and water stress interaction", "ai_between_x_mod"),
]

out = []
for label, key in terms:
    row = [label]
    for model in (m1, m2, m3):
        if key in model["index"]:
            value = term(model, key)
            row += [value["coef"], value["se"], value["p"]]
        else:
            row += ["", "", ""]
    out.append(row)

out += [
    ["Observations", m1["n"], "", "", m2["n"], "", "", m3["n"], "", ""],
    ["Countries", m1["countries"], "", "", m2["countries"], "", "", m3["countries"], "", ""],
    ["R2", m1["r2"], "", "", m2["r2"], "", "", m3["r2"], "", ""],
]

write_csv(
    ROOT / "output" / "table3_main_models.csv",
    ["Variable", "M1 beta", "M1 SE", "M1 p", "M2 beta", "M2 SE", "M2 p", "M3 beta", "M3 SE", "M3 p"],
    out,
)

pairs = [
    ("ln_ai_articles_pm_between", "ln_ai_articles_pm_within"),
    ("ln_gdp_pc_between", "ln_gdp_pc_within"),
    ("agri_share_between", "agri_share_within"),
    ("industry_share_between", "industry_share_within"),
    ("urban_share_between", "urban_share_within"),
    ("internet_share_between", "internet_share_within"),
    ("trade_share_between", "trade_share_within"),
]
R = np.zeros((len(pairs), len(m2["model"].params)))
for i, (between, within) in enumerate(pairs):
    R[i, m2["index"][between]] = 1
    R[i, m2["index"][within]] = -1

joint = m2["model"].f_test(R)
write_csv(
    ROOT / "output" / "mundlak_joint_test.csv",
    ["F", "df_num", "df_denom", "p"],
    [[float(joint.fvalue), 7, 150, float(joint.pvalue)]],
)

print("Model 1:", m1["n"], m1["countries"], round(m1["r2"], 3))
print("Model 2:", m2["n"], m2["countries"], round(m2["r2"], 3))
print("Model 3:", m3["n"], m3["countries"], round(m3["r2"], 3))
print("AI between component and water stress interaction:", term(m3, "ai_between_x_mod"))
print("Mundlak joint F:", float(joint.fvalue), "p=", float(joint.pvalue))
