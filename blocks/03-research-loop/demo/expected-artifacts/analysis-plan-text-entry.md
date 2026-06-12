# Analysis plan: do the three keyboard interfaces differ in typing speed?

> **Note:** Hand-crafted sample artifact (live-demo fallback for the
> `plan-analysis` skill).

## Question & hypotheses

Does typing speed (`wpm`) differ across the three interfaces (`qwerty`, `swipe`,
`predictive`)?

- **H0:** the distribution of `wpm` is the same across interfaces.
- **H1:** at least one interface differs.
- **Primary outcome:** `wpm`. **Secondary (exploratory only):** `error_rate`.

## Design facts that drive the test

Within-subjects: each of the 30 participants is measured on all three interfaces
(see [profile](profile-text-entry.md)). The three measurements per participant are
**paired**. An independent-samples test (one-way ANOVA, Welch t-test) would be
**invalid** here — it ignores the pairing and the non-independence of rows.

## Chosen approach

- **Primary test:** **repeated-measures ANOVA** *if* its assumptions hold;
  otherwise the **Friedman test** (its non-parametric, rank-based equivalent for a
  within-subjects factor).
- **Assumptions to check (and fallback):**
  - Normality of `wpm` within each interface (Shapiro–Wilk). *If it fails →
    Friedman.*
  - Sphericity (for RM-ANOVA). *If violated → Greenhouse–Geisser correction, or
    Friedman.*
- **Effect size:** Kendall's W for the omnibus Friedman; matched-pairs
  rank-biserial correlation for each pairwise post-hoc. Report with the test.
- **Multiple comparisons:** three pairwise post-hoc tests → **Holm** correction.

## Analysis steps

1. [ ] Load `data.csv` with `comment="#"`; confirm 90 rows, 3 interfaces × 30 ppts.
2. [ ] EDA + assumption checks (normality per interface, spot the outlier) — see
   `explore-data`.
3. [ ] Run the omnibus test the assumptions support; report statistic, p, effect
   size.
4. [ ] Pairwise post-hoc (paired) with Holm correction; report effect sizes.

## Success criteria

### Automated (a script/command can confirm)

- [ ] Shapiro–Wilk is computed and reported per interface (assumptions not skipped).
- [ ] The omnibus test is a **within-subjects** test (Friedman or RM-ANOVA), never
  `f_oneway` / independent t-test.
- [ ] Every p-value is reported with an effect size + (where applicable) CI.
- [ ] Post-hoc p-values are Holm-corrected.

### Manual (human judgment)

- [ ] The chosen test is defensible given the assumption results.
- [ ] Conclusions stay within the manipulated factor (no overreach).

## References

- [Profile](profile-text-entry.md)
- `AGENTS.md` — alpha, effect-size + CI rule, Holm correction, "never invent
  citations".
