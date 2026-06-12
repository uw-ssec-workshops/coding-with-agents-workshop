# EDA & assumption checks: text-entry study

> **Note:** Hand-crafted sample artifact (live-demo fallback for the `explore-data`
> skill). Numbers below were computed from the committed `starter/data.csv`.

## Summaries (wpm)

| interface | n | mean | median | SD | IQR |
|---|---|---|---|---|---|
| qwerty | 30 | 41.4 | 41.9 | 4.9 | 7.6 |
| swipe | 30 | 36.7 | 38.2 | 6.8 | 5.9 |
| predictive | 30 | 34.5 | 34.1 | 5.6 | 6.1 |

Ordering of central tendency: `qwerty` > `swipe` > `predictive`. Note `swipe` has
the largest SD — inflated by a low outlier (see below), and its mean (36.7) sits
well below its median (38.2), a classic left-pull from one extreme value.

## Assumption checks

| assumption | method | result | holds? |
|---|---|---|---|
| normality (qwerty) | Shapiro–Wilk | W=0.969, p=0.513 | ✅ |
| normality (swipe) | Shapiro–Wilk | W=0.785, p<0.0001 | ❌ |
| normality (predictive) | Shapiro–Wilk | W=0.991, p=0.995 | ✅ |

`swipe` fails normality decisively, driven by the outlier. With a within-subjects
factor and a violated normality assumption, the parametric RM-ANOVA is **not**
trustworthy here.

## Outliers / data quirks

- **`P07`, `swipe`: `wpm = 9.8`** — far below the rest of the swipe distribution
  (next lowest ≈ 24). Consistent with the "dropped stylus" note in `AGENTS.md`.
  Kept in the analysis (it's real measured behavior), but it is *why* we go
  non-parametric rather than deleting a data point to rescue a t-test.

## Figures

- [Typing speed by interface](figures/dist-by-interface.png) — box + jittered
  points; the swipe outlier is the point near 10 wpm.
- [Within-participant paired profiles](figures/paired-by-participant.png) — each
  gray line is one participant across the three interfaces; the red line is the
  mean. The mostly-parallel downward slopes show the within-subjects effect.

## Implication for the plan

Normality fails for `swipe`, so use the planned fallback: **Friedman test** for the
omnibus, with **Wilcoxon signed-rank** pairwise post-hoc (Holm-corrected). Report
Kendall's W and matched-pairs rank-biserial effect sizes.
