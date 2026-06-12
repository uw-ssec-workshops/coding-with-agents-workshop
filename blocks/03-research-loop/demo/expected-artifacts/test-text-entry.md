# Test results: do the three keyboard interfaces differ in typing speed?

> **Note:** Hand-crafted sample artifact (live-demo fallback for the
> `statistical-tests` skill). All numbers reproduce from
> `expected-artifacts/analysis.py`.

Test chosen: **Friedman test** (non-parametric, within-subjects) — because the
normality assumption failed for `swipe` (see [explore](explore-text-entry.md)), so
the parametric repeated-measures ANOVA is not trustworthy. An independent-samples
one-way ANOVA is **not** an option: the design is repeated-measures.

## Primary result

- **Friedman:** χ²(2) = 45.19, p = 1.5 × 10⁻¹⁰ (α = 0.05) → **reject H0**. Typing
  speed differs across the three interfaces.
- **Effect size:** Kendall's W = 0.75 — a large concordance of rankings (most
  participants order the interfaces the same way).
- n = 30 participants (complete cases on all three interfaces).

## Post-hoc (Wilcoxon signed-rank, Holm-corrected)

| comparison | p (raw) | p (Holm) | rank-biserial | result |
|---|---|---|---|---|
| qwerty vs swipe | 1.1 × 10⁻⁵ | 2.2 × 10⁻⁵ | +0.94 | qwerty faster |
| qwerty vs predictive | 1.9 × 10⁻⁹ | 5.6 × 10⁻⁹ | +1.00 | qwerty faster |
| swipe vs predictive | 7.7 × 10⁻⁴ | 7.7 × 10⁻⁴ | +0.70 | swipe faster |

All three pairwise differences survive Holm correction. The ordering is
**qwerty > swipe > predictive** for typing speed.

## Reproduce

- script: `expected-artifacts/analysis.py`
- command: `uv run python expected-artifacts/analysis.py` (run from `demo/`)

## References

- [Analysis plan](analysis-plan-text-entry.md)
- [EDA & assumptions](explore-text-entry.md)
