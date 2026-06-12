"""Reproducible analysis for the text-entry study (sample / fallback).

Mirrors what the `statistical-tests` skill should produce. Run from the demo
folder so the relative path to the data resolves:

    uv run python expected-artifacts/analysis.py
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

DATA = Path(__file__).resolve().parents[1] / "starter" / "data.csv"
INTERFACES = ["qwerty", "swipe", "predictive"]
ALPHA = 0.05


def matched_pairs_rank_biserial(a: np.ndarray, b: np.ndarray) -> float:
    """Effect size for a Wilcoxon signed-rank test (a - b)."""
    d = a - b
    d = d[d != 0]
    ranks = stats.rankdata(np.abs(d))
    r_pos = ranks[d > 0].sum()
    r_neg = ranks[d < 0].sum()
    total = r_pos + r_neg
    return float((r_pos - r_neg) / total)


def main() -> None:
    df = pd.read_csv(DATA, comment="#")
    wide = df.pivot(index="participant_id", columns="interface", values="wpm")[INTERFACES]

    print("Assumption check (Shapiro-Wilk normality of wpm per interface):")
    for i in INTERFACES:
        w, p = stats.shapiro(wide[i])
        print(f"  {i:11s} W={w:.3f} p={p:.4g} -> {'normal' if p > ALPHA else 'NOT normal'}")

    # Normality fails for swipe -> use the non-parametric within-subjects test.
    chi2, p = stats.friedmanchisquare(*[wide[i] for i in INTERFACES])
    n, k = wide.shape[0], len(INTERFACES)
    kendall_w = chi2 / (n * (k - 1))
    print("\nOmnibus: Friedman test")
    print(f"  chi2={chi2:.3f}, df={k - 1}, p={p:.4g}, Kendall's W={kendall_w:.3f}")

    print("\nPost-hoc: Wilcoxon signed-rank (Holm-corrected)")
    pairs = [("qwerty", "swipe"), ("qwerty", "predictive"), ("swipe", "predictive")]
    raw = [stats.wilcoxon(wide[a], wide[b]).pvalue for a, b in pairs]
    _, p_holm, _, _ = multipletests(raw, method="holm")
    for (a, b), p_raw, p_adj in zip(pairs, raw, p_holm, strict=True):
        rbc = matched_pairs_rank_biserial(wide[a].to_numpy(), wide[b].to_numpy())
        print(f"  {a:10s} vs {b:11s} p_raw={p_raw:.4g} p_holm={p_adj:.4g} rank-biserial={rbc:+.2f}")


if __name__ == "__main__":
    main()
