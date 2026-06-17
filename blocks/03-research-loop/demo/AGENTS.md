# Text-entry study: agent guidance

A small within-subjects HCI experiment used as the running scenario in **Block 3**
of the "Coding with AI Agents" workshop. Read this file first before analyzing the
data.

## Paths and where to write artifacts

This study lives in `blocks/03-research-loop/demo/`. The workshop repo is normally
open at its **root**, so use full repo-root-relative paths:

- **Data:** `blocks/03-research-loop/demo/starter/data.csv`
- **Write every workflow artifact to `blocks/03-research-loop/demo/docs/`** (create
  it if needed) — the profile, analysis plan, EDA, test results, draft, and
  validation. **Do NOT write to the repo's top-level `docs/`.**

These artifacts are meant to be **committed** (`git add blocks/03-research-loop/demo/docs/`)
as the analysis audit trail for a dated record of what was analyzed and why.

## What this data is

`starter/data.csv` — a **synthetic** text-entry experiment. Each participant typed
standardized phrases on three on-screen keyboard interfaces, and we recorded their
typing speed and error rate. The data is **long/tidy**: one row per
participant × interface.

- `make_data.py` generates the CSV deterministically (fixed seed). It is demo
  scaffolding and the thing you analyze is `data.csv`, not the generator.
- The CSV's **first line is a `#` comment**; load with
  `pandas.read_csv(path, comment="#")` (or `skiprows=1`).

## Study design (read carefully — it determines the test)

- **Within-subjects (repeated measures):** Every participant uses **all three**
  interfaces, so the three measurements from one participant are *paired*, not
  independent. **Rows are not independent.** Do **not** analyze this with an
  independent-samples test (one-way ANOVA, Welch/Student t-test).
- **Factor:** `interface` with three levels — `qwerty` (baseline on-screen
  keyboard), `swipe` (gesture typing), `predictive` (heavy auto-complete).
- **Primary outcome:** `wpm` (words per minute). **Secondary:** `error_rate`
  (fraction of characters corrected). The primary analysis is on `wpm`.
- **Order:** `presentation_order` (1/2/3) is counterbalanced across participants,
  so you can sanity check for a learning/order effect.

### Variable dictionary

| column | type | meaning |
|---|---|---|
| `participant_id` | str | participant label (`P01`…`P30`); the repeated-measures key |
| `interface` | categorical | `qwerty` / `swipe` / `predictive` (within-subjects factor) |
| `presentation_order` | int | 1–3, the order this participant saw this interface |
| `wpm` | float | typing speed, words per minute (primary outcome) |
| `error_rate` | float | fraction of characters corrected (secondary outcome) |

### Hypotheses

- **H0:** typing speed (`wpm`) does not differ across the three interfaces.
- **H1:** at least one interface differs in `wpm`.

## Analysis conventions

- **alpha = 0.05.**
- **Respect the repeated-measures design.** The candidate test is a
  repeated-measures ANOVA; its non-parametric equivalent is the **Friedman test**.
  Pairwise follow-ups are **paired** (Wilcoxon signed-rank or paired t), never
  independent-samples.
- **Check assumptions before trusting a parametric test:** normality (e.g.
  Shapiro–Wilk per interface or on residuals) and sphericity. If normality fails,
  **fall back to Friedman + Wilcoxon signed-rank post-hoc.**
- **Always report an effect size**, not just a p-value (e.g. Kendall's W for
  Friedman; matched-pairs rank-biserial for Wilcoxon). Add a **95% CI when you
  compute one**; if you don't, note "CI not computed" rather than inventing an
  interval.
- **Correct for multiple comparisons** (Holm) across the pairwise post-hoc tests.
- **Never invent citations.** Where a reference is needed in a draft, write
  `[CITATION NEEDED]` — do not fabricate authors, years, or DOIs.
- **Reproducibility:** set a NumPy seed; every reported number must reproduce from
  `data.csv`.

## Reporting style

A draft write-up produces, in this order, in markdown:

1. **Methods** — participants, design (within-subjects), apparatus (the three
   interfaces), procedure, measures, and the analysis approach (which test, why,
   assumption checks, effect size, correction).
2. **Analysis / Results** — the findings, each traceable to a computed number,
   leading with the answer to the research question.

## Out of scope for this demo

- Causal claims beyond what the manipulated `interface` factor supports.
- Modeling the learning/order effect beyond a sanity check.
- Publishing, CI, a docs site.

## How to verify a run

Re-run the analysis script the agent wrote and confirm the headline numbers
(Friedman χ², p, effect size, and the pairwise post-hoc) reproduce from
`starter/data.csv`.
