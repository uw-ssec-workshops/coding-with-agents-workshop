# Validation: text-entry interface comparison

> **Note:** Hand-crafted sample artifact (live-demo fallback for the
> `validate-analysis` skill).

Plan: [analysis-plan-text-entry.md](analysis-plan-text-entry.md)

## Overall: ✅ Ready

## Design & assumptions

- Test matches design (repeated-measures respected): ✅ — the omnibus is the
  Friedman test and post-hoc tests are paired (Wilcoxon signed-rank). No
  independent-samples test was used on the paired data.
- Assumptions checked and test chosen accordingly: ✅ — Shapiro–Wilk was run per
  interface; `swipe` failed (W = 0.79, p < .0001), and the analysis correctly fell
  back from RM-ANOVA to Friedman rather than running the parametric test anyway.

## Numbers reconcile (re-run vs reported)

Re-ran `uv run python expected-artifacts/analysis.py`:

| reported | source | re-run | match? |
|---|---|---|---|
| Friedman χ² = 45.19, p = 1.5e-10 | test-text-entry.md | χ² = 45.193, p = 1.536e-10 | ✅ |
| Kendall's W = 0.75 | test-text-entry.md | 0.753 | ✅ |
| qwerty vs swipe Holm p = 2.2e-5 | test-text-entry.md | 2.154e-5 | ✅ |
| qwerty vs predictive Holm p = 5.6e-9 | test-text-entry.md | 5.588e-9 | ✅ |
| swipe vs predictive Holm p = 7.7e-4 | test-text-entry.md | 7.71e-4 | ✅ |

## Draft audit

- Claims supported by results: ✅ — every statistic in the draft matches
  `test-text-entry.md`; descriptive means match the EDA summary.
- No fabricated citations (only `[CITATION NEEDED]`): ✅ — the draft uses
  `[CITATION NEEDED]` placeholders rather than invented references.
- Overclaiming / leftover `[TODO]`: one `[TODO]` flags the optional secondary
  `error_rate` analysis; the draft correctly avoids causal claims beyond the
  manipulated factor.

## Recommendations

- Critical (fix before trusting): none.
- Nice to have: resolve the `[CITATION NEEDED]` markers (Shapiro–Wilk, Friedman,
  Holm, the text-entry protocol) and decide whether `error_rate` is in scope.
