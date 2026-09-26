from pathlib import Path

from model_utils import fit_mundlak, load_data, term, write_csv

ROOT = Path(__file__).resolve().parents[1]
rows = load_data(ROOT / "data" / "analysis_data.csv")

outcomes = [
    ("Total WUE", "wue_total"),
    ("Agricultural WUE", "wue_agri"),
    ("Industrial WUE", "wue_ind"),
    ("Services WUE", "wue_serv"),
]

models = []
for label, outcome in outcomes:
    result = fit_mundlak(
        rows,
        outcome=outcome,
        flag="main_moderation_sample",
        include_controls=True,
        include_interactions=True,
    )
    models.append((label, result))

keys = [
    ("AI research capacity, within country", "ln_ai_articles_pm_within"),
    ("AI research capacity, between country", "ln_ai_articles_pm_between"),
    ("Baseline water stress", "moderator_c"),
    ("AI within country x water stress", "ai_within_x_mod"),
    ("AI between country x water stress", "ai_between_x_mod"),
]

output = []
for variable, key in keys:
    line = [variable]
    for _, result in models:
        stat = term(result, key)
        line += [stat["coef"], stat["se"], stat["p"]]
    output.append(line)

for metric, getter in [
    ("Observations", lambda x: x["n"]),
    ("Countries", lambda x: x["countries"]),
    ("R2", lambda x: x["r2"]),
]:
    line = [metric]
    for _, result in models:
        line += [getter(result), "", ""]
    output.append(line)

header = ["Variable"]
for label, _ in models:
    header += [f"{label} beta", f"{label} SE", f"{label} p"]

write_csv(ROOT / "output" / "table4_sectoral_models.csv", header, output)

for label, result in models:
    stat = term(result, "ai_between_x_mod")
    print(label, result["n"], result["countries"], round(stat["coef"], 6), round(stat["se"], 6))
