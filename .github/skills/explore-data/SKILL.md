---
name: explore-data
description: 'Run exploratory data analysis and the assumption checks an analysis plan calls for — distributions, group summaries, normality/variance/sphericity, outliers — emit figures, and write the findings to docs/. Use when someone has a plan (or just a dataset) and wants to see the data and check whether the intended test''s assumptions actually hold before running it. Phase 3 of the analysis workflow.'
tools: ['read', 'edit/editFiles', 'search/codebase', 'execute/runInTerminal']
argument-hint: '[optional: assumptions or columns to focus on]'
---

# Explore data (phase 3 of the analysis workflow)

Look at the data honestly and **check the assumptions the plan depends on**, before
trusting any test. EDA is where you find the skew, the outlier, or the
dependence structure that decides which test is valid.

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## Context first

1. Read the matching `docs/analysis-plan-*.md` (and `profile-*.md`) so you know
   which assumptions to check and which fallback each failure triggers.
2. Read `AGENTS.md` for conventions (seed, alpha, dependence structure).

## Steps

1. **Load the data faithfully** — respect the `#` comment line and dtypes; set the
   `numpy` seed from `AGENTS.md`.
2. **Summarize** the outcome(s) overall and per group/condition (n, mean, median,
   SD, IQR). For repeated measures, summarize *within* participant too.
3. **Check the planned assumptions and report the numbers:**
   - Normality (e.g. `scipy.stats.shapiro` per condition or on residuals) — report
     the statistic and p, don't just say "looks normal".
   - Equal variance / sphericity as the design requires.
   - Outliers (and flag the specific rows).
4. **Make a few figures** and save them to `docs/figures/` (e.g. per-condition
   distributions, and for repeated measures a per-participant paired-line plot).
   Reference them from the artifact.
5. **State the implication** for the plan: do the assumptions hold? If not, which
   fallback test does that point to? (Describe — the decision is confirmed in the
   plan / by the user.)
6. **Write the artifact** to `docs/explore-<slug>.md` and present a short
   summary with the key numbers and figure links.

## Artifact structure (`docs/explore-<slug>.md`)

```
# EDA & assumption checks: <study>

## Summaries
| condition | n | mean | median | SD | IQR |
|---|---|---|---|---|---|

## Assumption checks
| assumption | method | result | holds? |
|---|---|---|---|
| normality (group A) | Shapiro–Wilk | W=.., p=.. | ✅ / ❌ |
| ... | ... | ... | ... |

## Outliers / data quirks
- row <N>: <value> — <why flagged>

## Figures
- [distributions](figures/dist-by-group.png)
- [paired lines](figures/paired-by-subject.png)

## Implication for the plan
<which test the assumption results support; which fallback if violated>
```

## Constraints

- **Read-only on the source data.** Write only to `docs/` (artifact + figures).
- **Do not fabricate numbers.** Every statistic comes from code you actually ran;
  show the command or snippet if asked.
- This phase informs the test choice — it does not run the confirmatory test. That
  is `statistical-tests`.

Next phase: `statistical-tests`.
