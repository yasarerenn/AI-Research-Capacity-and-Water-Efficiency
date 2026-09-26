from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
import statsmodels.api as sm

BASE_CONTROLS = [
    "ln_gdp_pc",
    "agri_share",
    "industry_share",
    "urban_share",
    "internet_share",
    "trade_share",
]

TEXT_FIELDS = {
    "iso3", "country", "water_stress_cat", "water_stress_label", "wb_region",
    "missing_baseline_requirements", "ai_patent_coverage", "ai_invest_coverage",
}


def load_data(path: str | Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            clean = {}
            for key, value in row.items():
                if key in TEXT_FIELDS:
                    clean[key] = value
                elif value in (None, ""):
                    clean[key] = np.nan
                else:
                    try:
                        clean[key] = float(value)
                    except ValueError:
                        clean[key] = value
            if np.isfinite(clean.get("gdp_pc", np.nan)) and clean["gdp_pc"] > 0:
                clean["ln_gdp_pc"] = math.log(clean["gdp_pc"])
            else:
                clean["ln_gdp_pc"] = np.nan
            rows.append(clean)
    return rows


def is_finite(value) -> bool:
    try:
        return bool(np.isfinite(value))
    except TypeError:
        return False


def subset_rows(rows, flag=None, outcome=None, predicate=None):
    out = []
    for original in rows:
        row = dict(original)
        if flag is not None and row.get(flag) != 1:
            continue
        if predicate is not None and not predicate(row):
            continue
        if outcome is not None:
            value = row.get(outcome, np.nan)
            if not is_finite(value) or value <= 0:
                continue
            row["y"] = math.log(value)
        out.append(row)
    return out


def add_within_between(rows, variables):
    for variable in variables:
        values = defaultdict(list)
        for row in rows:
            values[row["iso3"]].append(row[variable])
        means = {country: float(np.mean(v)) for country, v in values.items()}
        for row in rows:
            mean = means[row["iso3"]]
            row[f"{variable}_between"] = mean
            row[f"{variable}_within"] = row[variable] - mean


def prepare_ai_measure(row, name):
    if name == "ln_ai_articles_pm":
        return row.get(name, np.nan)
    if name == "ln_ai_invest_pm":
        inv = row.get("ai_invest_est_musd", np.nan)
        pop = row.get("population", np.nan)
        if not (is_finite(inv) and is_finite(pop) and pop > 0):
            return np.nan
        return math.log1p(inv / (pop / 1_000_000.0))
    if name == "ln_ai_patent_pm":
        patents = row.get("ai_patent_apps", np.nan)
        pop = row.get("population", np.nan)
        if not (is_finite(patents) and is_finite(pop) and pop > 0):
            return np.nan
        return math.log1p(patents / (pop / 1_000_000.0))
    raise ValueError(f"Unknown AI measure: {name}")


def prepare_moderator(row, name):
    if name == "water_stress_score_clean":
        return row.get(name, np.nan)
    if name == "ln1p_freshwater_pc":
        value = row.get("freshwater_pc", np.nan)
        if not is_finite(value) or value < 0:
            return np.nan
        return math.log1p(value)
    raise ValueError(f"Unknown moderator: {name}")


def fit_mundlak(
    rows,
    outcome,
    flag,
    controls=None,
    include_controls=True,
    include_interactions=True,
    region_effects=False,
    predicate=None,
    ai_measure="ln_ai_articles_pm",
    moderator="water_stress_score_clean",
):
    controls = list(BASE_CONTROLS if controls is None else controls)
    sample = subset_rows(rows, flag=flag, outcome=outcome, predicate=predicate)

    prepared = []
    for row in sample:
        row[ai_measure] = prepare_ai_measure(row, ai_measure)
        row[moderator] = prepare_moderator(row, moderator)
        needed = [ai_measure]
        if include_controls:
            needed += controls
        if include_interactions:
            needed += [moderator]
        if all(is_finite(row.get(v, np.nan)) for v in needed):
            prepared.append(row)
    sample = prepared

    wb_vars = [ai_measure] + (controls if include_controls else [])
    add_within_between(sample, wb_vars)

    if include_interactions:
        stress_mean = float(np.mean([row[moderator] for row in sample]))
        for row in sample:
            row["moderator_c"] = row[moderator] - stress_mean
            row["ai_within_x_mod"] = row[f"{ai_measure}_within"] * row["moderator_c"]
            row["ai_between_x_mod"] = row[f"{ai_measure}_between"] * row["moderator_c"]
    else:
        stress_mean = np.nan

    names = [f"{ai_measure}_within", f"{ai_measure}_between"]
    if include_controls:
        for control in controls:
            names += [f"{control}_within", f"{control}_between"]
    if include_interactions:
        names += ["moderator_c", "ai_within_x_mod", "ai_between_x_mod"]

    years = sorted({int(row["year"]) for row in sample})
    year_dummies = years[1:]
    regions = sorted({row["wb_region"] for row in sample})
    region_dummies = regions[1:] if region_effects else []

    X, y, groups = [], [], []
    for row in sample:
        values = [1.0] + [row[name] for name in names]
        values += [1.0 if int(row["year"]) == year else 0.0 for year in year_dummies]
        values += [1.0 if row["wb_region"] == region else 0.0 for region in region_dummies]
        X.append(values)
        y.append(row["y"])
        groups.append(row["iso3"])

    model = sm.OLS(np.asarray(y, dtype=float), np.asarray(X, dtype=float)).fit(
        cov_type="cluster",
        cov_kwds={"groups": np.asarray(groups), "use_correction": True},
    )
    coef_names = ["const"] + names
    coef_names += [f"year_{year}" for year in year_dummies]
    coef_names += [f"region_{region}" for region in region_dummies]
    index = {name: i for i, name in enumerate(coef_names)}

    return {
        "model": model,
        "index": index,
        "rows": sample,
        "stress_mean": stress_mean,
        "n": int(model.nobs),
        "countries": len(set(groups)),
        "r2": float(model.rsquared),
        "ai_measure": ai_measure,
        "moderator": moderator,
    }


def term(result, name):
    model = result["model"]
    idx = result["index"][name]
    return {
        "coef": float(model.params[idx]),
        "se": float(model.bse[idx]),
        "p": float(model.pvalues[idx]),
        "ci_low": float(model.conf_int()[idx, 0]),
        "ci_high": float(model.conf_int()[idx, 1]),
    }


def write_csv(path, header, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
