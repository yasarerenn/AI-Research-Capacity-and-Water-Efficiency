from collections import defaultdict
from pathlib import Path

import numpy as np

from model_utils import BASE_CONTROLS, fit_mundlak, load_data, term, write_csv

ROOT = Path(__file__).resolve().parents[1]
rows = load_data(ROOT / "data" / "analysis_data.csv")

counts = defaultdict(int)
for row in rows:
    if row["main_moderation_sample"] == 1:
        counts[row["iso3"]] += 1
balanced = {country for country, n in counts.items() if n == 8}

pop = defaultdict(list)
for row in rows:
    if row["main_moderation_sample"] == 1:
        pop[row["iso3"]].append(row["population"])
low_population = {country for country, values in pop.items() if np.mean(values) < 1_000_000}

wue = np.asarray([row["wue_total"] for row in rows if row["main_moderation_sample"] == 1], dtype=float)
q01, q99 = np.quantile(wue, [0.01, 0.99])
zero_ai_countries = {
    row["iso3"] for row in rows
    if row["main_moderation_sample"] == 1 and row["ai_articles"] == 0
}


def beta(result):
    stat = term(result, "ai_between_x_mod")
    return [stat["coef"], stat["se"], stat["p"], result["n"], result["countries"]]


def model(outcome="wue_total", **kwargs):
    return fit_mundlak(
        rows,
        outcome=outcome,
        flag="main_moderation_sample",
        include_controls=True,
        include_interactions=True,
        **kwargs,
    )


panel_a = [
    ["Main model"] + beta(model()),
    ["World Bank regional effects"] + beta(model(region_effects=True)),
    ["Balanced panel"] + beta(model(predicate=lambda r: r["iso3"] in balanced)),
    ["Excluding low population countries"] + beta(model(predicate=lambda r: r["iso3"] not in low_population)),
    ["Excluding lower and upper 1% of WUE observations"] + beta(
        model(predicate=lambda r: q01 <= r["wue_total"] <= q99)
    ),
    ["Controlling for general scientific publication capacity"] + beta(
        model(controls=BASE_CONTROLS + ["ln_scientific_articles_pm"])
    ),
]

panel_b = [
    ["Main model"] + beta(model(outcome="wue_ind")),
    ["World Bank regional effects"] + beta(model(outcome="wue_ind", region_effects=True)),
    ["Balanced panel"] + beta(model(outcome="wue_ind", predicate=lambda r: r["iso3"] in balanced)),
    ["Excluding low population countries"] + beta(
        model(outcome="wue_ind", predicate=lambda r: r["iso3"] not in low_population)
    ),
    ["Excluding China"] + beta(model(outcome="wue_ind", predicate=lambda r: r["iso3"] != "CHN")),
    ["Excluding AI observations coded as zero"] + beta(
        model(outcome="wue_ind", predicate=lambda r: r["ai_zero_imputed"] == 0)
    ),
    ["Excluding countries with any zero AI year"] + beta(
        model(outcome="wue_ind", predicate=lambda r: r["iso3"] not in zero_ai_countries)
    ),
    ["Controlling for general scientific publication capacity"] + beta(
        model(outcome="wue_ind", controls=BASE_CONTROLS + ["ln_scientific_articles_pm"])
    ),
    ["Controlling for general scientific publication capacity and R&D expenditure"] + beta(
        model(outcome="wue_ind", controls=BASE_CONTROLS + ["ln_scientific_articles_pm", "rd_exp_gdp"])
    ),
    ["Controlling for general scientific publication capacity and R&D researcher intensity"] + beta(
        model(outcome="wue_ind", controls=BASE_CONTROLS + ["ln_scientific_articles_pm", "researchers_per_million"])
    ),
    ["Excluding the industry share control"] + beta(
        model(outcome="wue_ind", controls=["ln_gdp_pc", "agri_share", "urban_share", "internet_share", "trade_share"])
    ),
    ["Excluding agriculture and industry share controls"] + beta(
        model(outcome="wue_ind", controls=["ln_gdp_pc", "urban_share", "internet_share", "trade_share"])
    ),
]

rows_out = [["Panel A: Total economic WUE", "", "", "", "", ""]] + panel_a
rows_out += [["Panel B: Industrial WUE", "", "", "", "", ""]] + panel_b
write_csv(
    ROOT / "output" / "table5_robustness.csv",
    ["Specification", "beta", "SE", "p", "Observations", "Countries"],
    rows_out,
)

private_ai = fit_mundlak(
    rows,
    outcome="wue_ind",
    flag="main_moderation_sample",
    ai_measure="ln_ai_invest_pm",
    include_controls=True,
    include_interactions=True,
)
patents = fit_mundlak(
    rows,
    outcome="wue_ind",
    flag="main_moderation_sample",
    ai_measure="ln_ai_patent_pm",
    include_controls=True,
    include_interactions=True,
)
freshwater = fit_mundlak(
    rows,
    outcome="wue_ind",
    flag="freshwater_robust_complete",
    moderator="ln1p_freshwater_pc",
    include_controls=True,
    include_interactions=True,
)
write_csv(
    ROOT / "output" / "measurement_sensitivity.csv",
    ["Specification", "beta", "SE", "p", "Observations", "Countries"],
    [
        ["Private AI investment per million population"] + beta(private_ai),
        ["AI patents per million population"] + beta(patents),
        ["Renewable internal freshwater resources per capita"] + beta(freshwater),
    ],
)

for row in panel_a + panel_b:
    print(row)

print("Measurement sensitivity")
for label, result in [
    ("Private investment", private_ai),
    ("Patents", patents),
    ("Freshwater", freshwater),
]:
    print(label, beta(result))
