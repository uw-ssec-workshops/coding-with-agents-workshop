# Statistical Tests Reference (Block 3: Research Loop)

A quick instructor reference for every statistical test, assumption check, effect
size, and correction that appears in `blocks/03-research-loop/`. Use it to answer
"what is that test?" during Q&A. Grounded in the demo artifacts under
`blocks/03-research-loop/demo/` and the skills in `.github/skills/`.

## The study context (why these tests, not others)

The running example is a **within-subjects (repeated-measures)** experiment: all 30
participants typed on all three interfaces (`qwerty`, `swipe`, `predictive`). Each
participant contributes three *paired* measurements, so the rows are **not
independent**. This single design fact drives every test choice below.

---

## 1. Assumption checks (run before trusting any test)

### Shapiro–Wilk test (normality)
- **What it is:** A test of whether a sample comes from a normally-distributed
  population. H0 = "the data are normal"; a small p-value rejects normality.
- **In the demo:** Run per interface on `wpm`. `qwerty` (W=0.969, p=0.51) and
  `predictive` (W=0.991, p=0.99) pass; **`swipe` fails decisively** (W=0.785,
  p<0.0001), pulled down by the `P07` outlier (9.8 wpm). This failure is why the
  analysis abandons parametric RM-ANOVA and falls back to Friedman.

### Sphericity (+ Greenhouse–Geisser correction)
- **What it is:** Sphericity is an assumption specific to repeated-measures ANOVA:
  the variances of the *differences* between every pair of conditions must be equal.
  If violated, the RM-ANOVA F-test becomes too liberal (inflated false positives).
  **Greenhouse–Geisser** corrects for this by adjusting the degrees of freedom
  downward.
- **In the demo:** Listed as an assumption to check *if* RM-ANOVA were used. Since
  normality already failed, the analysis goes non-parametric and sphericity becomes
  moot — but it is named as the other thing you'd verify for the parametric route.

### Equal variance / homogeneity of variance
- **What it is:** The assumption that different groups have similar spread; relevant
  to between-subjects parametric tests.
- **In the demo:** Mentioned generically in the skills as an assumption "as the
  design requires." Not central here because the design is within-subjects
  (sphericity is the relevant variance assumption, not between-group equal variance).

---

## 2. Omnibus tests (the main "do the groups differ at all?" test)

### Friedman test — the one actually used
- **What it is:** The non-parametric equivalent of a repeated-measures ANOVA. Within
  each participant it ranks the conditions, then tests whether the rank distributions
  differ. Works on ranks, so it assumes no normality and is robust to outliers.
- **In the demo:** Chosen because `swipe` failed normality. Result:
  χ²(2) = 45.19, p = 1.5×10⁻¹⁰ → reject H0; typing speed differs across interfaces.

### Repeated-measures ANOVA (RM-ANOVA) — planned parametric option, not used
- **What it is:** An ANOVA for within-subjects designs. It partitions out each
  participant's baseline, giving more power than a between-subjects ANOVA. Assumes
  normality and sphericity.
- **In the demo:** It was the *primary* test "if assumptions hold." They didn't
  (normality failed), so it was correctly **not** run.

### One-way ANOVA (`f_oneway`) — explicitly the WRONG test
- **What it is:** Compares means across 3+ **independent** groups.
- **Why rejected:** It assumes every observation is independent. Here the three
  measurements per participant are paired, so it would ignore the pairing and the
  non-independence — invalid. The skills call this out as a thing to never do.

### Welch / Student t-test — also flagged as wrong here
- **What it is:** Compares the means of **two independent** groups. *Student's*
  assumes equal variances; *Welch's* does not (the safer default for two independent
  samples).
- **Why rejected:** Independent-samples tests on repeated-measures data are invalid.
  (Also, with three conditions you'd need an omnibus test, not a pairwise t-test, as
  the primary analysis.)

---

## 3. Post-hoc / pairwise tests (which specific pairs differ)

Once the omnibus test says "something differs," you compare conditions pairwise.

### Wilcoxon signed-rank test — the one actually used
- **What it is:** The non-parametric, **paired** two-sample test. It takes the
  within-participant differences between two conditions, ranks their absolute values,
  and tests whether positive and negative differences balance. The paired counterpart
  of the Friedman/RM-ANOVA family.
- **In the demo:** Run on all three pairs. All three remain significant after
  correction; ordering is qwerty > swipe > predictive.

### Paired t-test — the parametric pairwise alternative, not used
- **What it is:** Tests whether the mean of within-participant differences is zero.
  Assumes those differences are normal.
- **In the demo:** Named as the parametric pairwise option you'd use if assumptions
  held; replaced by Wilcoxon for the same normality reason.

---

## 4. Effect sizes (how big is the difference, beyond "is it significant")

The skills insist a p-value alone is never a result — always pair it with an effect
size.

### Kendall's W (coefficient of concordance)
- **What it is:** The effect size for the Friedman test. Ranges 0–1 and measures how
  consistently participants rank the conditions the same way. 0 = no agreement, 1 =
  perfect agreement. Computed as W = χ² / (n·(k−1)).
- **In the demo:** W = 0.75 — a large, consistent ranking effect. CI not computed
  (and the artifact honestly says so rather than inventing one).

### Matched-pairs rank-biserial correlation
- **What it is:** The effect size for a Wilcoxon signed-rank test. The difference
  between the proportion of positive ranks and negative ranks, ranging −1 to +1.
  Magnitude = strength, sign = direction.
- **In the demo:** e.g. qwerty vs predictive = +1.00 (every participant typed faster
  on qwerty), swipe vs predictive = +0.70.

---

## 5. Multiple-comparison correction

### Holm correction (Holm–Bonferroni)
- **What it is:** Running several tests inflates the chance of at least one false
  positive. Holm controls this family-wise error rate by sorting the p-values and
  applying a progressively less strict Bonferroni-style threshold — more powerful
  than plain Bonferroni while still controlling false positives.
- **In the demo:** Applied across the three pairwise Wilcoxon tests. All three
  survive correction, so the conclusions are robust.

---

## Quick cheat-sheet (if someone asks on the spot)

| Role | Used here | Non-chosen alternative | Why the choice |
|---|---|---|---|
| Normality check | Shapiro–Wilk | — | `swipe` failed it |
| RM-ANOVA assumption | Sphericity (+ Greenhouse–Geisser) | — | moot once parametric route dropped |
| Omnibus | **Friedman** | RM-ANOVA (parametric); one-way ANOVA / t-test (invalid — ignores pairing) | normality failed + repeated measures |
| Pairwise | **Wilcoxon signed-rank** | paired t-test (parametric) | same normality reason |
| Effect size (omnibus) | Kendall's W | — | matches Friedman |
| Effect size (pairwise) | rank-biserial | — | matches Wilcoxon |
| Correction | Holm | Bonferroni | controls false positives, more powerful |

**One-sentence narrative:** because the data are repeated-measures and one condition
fails normality, the analysis uses the non-parametric within-subjects family —
Friedman for the omnibus, Wilcoxon signed-rank for paired post-hocs, Holm-corrected —
with Kendall's W and rank-biserial effect sizes, deliberately avoiding the
independent-samples ANOVA/t-test that would ignore the pairing.

---

## Sources

- `blocks/03-research-loop/demo/AGENTS.md` — study design and stats conventions
- `blocks/03-research-loop/demo/expected-artifacts/analysis-plan-text-entry.md`
- `blocks/03-research-loop/demo/expected-artifacts/explore-text-entry.md`
- `blocks/03-research-loop/demo/expected-artifacts/test-text-entry.md`
- `blocks/03-research-loop/demo/expected-artifacts/validate-text-entry.md`
- `blocks/03-research-loop/demo/expected-artifacts/analysis.py`
- `.github/skills/` — `plan-analysis`, `explore-data`, `statistical-tests`,
  `validate-analysis`
