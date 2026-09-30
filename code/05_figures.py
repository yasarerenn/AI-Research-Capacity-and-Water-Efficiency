from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from model_utils import fit_mundlak, load_data, term

ROOT = Path(__file__).resolve().parents[1]
rows = load_data(ROOT / "data" / "analysis_data.csv")
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

labels = [
    "Matched country-year grid\n1,464 observations / 183 countries",
    "Total WUE available\n1,336 / 167",
    "Baseline estimation sample\n1,156 / 151",
    "Water-stress moderation sample\n1,086 / 142",
]
fig, ax = plt.subplots(figsize=(8, 7))
ax.axis("off")
ys = np.linspace(0.88, 0.12, len(labels))
for i, (label, y) in enumerate(zip(labels, ys)):
    ax.text(
        0.5, y, label, ha="center", va="center",
        bbox={"boxstyle": "round,pad=0.6", "fill": False},
    )
    if i < len(labels) - 1:
        ax.annotate(
            "", xy=(0.5, ys[i + 1] + 0.08), xytext=(0.5, y - 0.08),
            arrowprops={"arrowstyle": "->"},
        )
fig.tight_layout()
fig.savefig(FIG / "Figure_1_sample_construction.svg", bbox_inches="tight")
plt.close(fig)

main = fit_mundlak(
    rows,
    outcome="wue_total",
    flag="main_moderation_sample",
    include_controls=True,
    include_interactions=True,
)
model = main["model"]
idx = main["index"]
b = idx["ln_ai_articles_pm_between"]
i = idx["ai_between_x_mod"]
cov = model.cov_params()

stress = np.linspace(0, 5, 201)
centered = stress - main["stress_mean"]
effect = model.params[b] + model.params[i] * centered
variance = cov[b, b] + centered**2 * cov[i, i] + 2 * centered * cov[b, i]
se = np.sqrt(variance)
lo, hi = effect - 1.96 * se, effect + 1.96 * se

fig, ax = plt.subplots(figsize=(7.5, 5.2))
ax.plot(stress, effect)
ax.fill_between(stress, lo, hi, alpha=0.2)
ax.axhline(0, linestyle="--")
ax.axvline(main["stress_mean"], linestyle=":")
ax.set_xlabel("Baseline water stress")
ax.set_ylabel("Marginal association of the between component")
fig.tight_layout()
fig.savefig(FIG / "Figure_2_marginal_relationship.svg", bbox_inches="tight")
plt.close(fig)

outcomes = [
    ("Total", "wue_total"),
    ("Agricultural", "wue_agri"),
    ("Industrial", "wue_ind"),
    ("Services", "wue_serv"),
]
coef, low, high = [], [], []
for _, outcome in outcomes:
    result = fit_mundlak(
        rows,
        outcome=outcome,
        flag="main_moderation_sample",
        include_controls=True,
        include_interactions=True,
    )
    stat = term(result, "ai_between_x_mod")
    coef.append(stat["coef"])
    low.append(stat["ci_low"])
    high.append(stat["ci_high"])

pos = np.arange(len(outcomes))
err = np.vstack([
    np.asarray(coef) - np.asarray(low),
    np.asarray(high) - np.asarray(coef),
])
fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.errorbar(coef, pos, xerr=err, fmt="o", capsize=3)
ax.axvline(0, linestyle="--")
ax.set_yticks(pos, [name for name, _ in outcomes])
ax.set_xlabel("AI between component and baseline water stress interaction coefficient")
ax.invert_yaxis()
fig.tight_layout()
fig.savefig(FIG / "Figure_3_sectoral_heterogeneity.svg", bbox_inches="tight")
plt.close(fig)
