---
name: plan-analysis
description: 'Turn a dataset profile and a research question into a defensible, testable analysis plan — the right statistical test(s) for the study design, the assumptions to check first, and explicit success criteria — written to docs/. Use when someone knows their data and wants to decide HOW to analyze it before running anything. Phase 2 of the analysis workflow.'
tools: ['read', 'search/codebase', 'search', 'edit/editFiles']
argument-hint: '[research question, e.g. "do the groups differ on the outcome?"]'
---

# Plan analysis (phase 2 of the analysis workflow)

Produce a detailed, **defensible** analysis plan: which test answers the question,
why it is the right test *for this design*, which assumptions must hold, and what a
trustworthy result looks like. A plan is a statistical specification, not a vague
to-do list.

What to plan: the research question the user gives you (e.g. "do the groups differ
on the outcome?").

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## Context first

1. Read any `docs/profile-*.md` that matches the dataset **completely**, plus
   the dataset and `AGENTS.md`.
2. If no profile exists, say so and suggest running `profile-dataset` first, but
   proceed if the user prefers.

## Match the test to the design — this is the whole job

- **Respect the design.** Repeated-measures / within-subjects data is **not**
  independent — do not plan an independent-samples test (t-test, one-way ANOVA) for
  it. Within-subjects → paired / repeated-measures family (paired t / RM-ANOVA, or
  their non-parametric cousins Wilcoxon signed-rank / Friedman).
- **State the assumptions to check up front** (normality, equal variance,
  sphericity, independence) and the **fallback** if each fails (e.g. "if normality
  fails → Friedman + Wilcoxon post-hoc").
- **Plan effect sizes + CIs**, not just p-values.
- **Plan multiple-comparison correction** (e.g. Holm) whenever more than one test
  is run, such as pairwise post-hoc across 3+ conditions.
- Honor `AGENTS.md` conventions (alpha, reporting style, "never invent citations").
- Ask the user only **judgment** questions (which outcome is primary, one- vs
  two-sided, what effect size is meaningful). Don't ask what you can read.

## Write the artifact (`docs/analysis-plan-<slug>.md`)

```
# Analysis plan: <research question>

## Question & hypotheses
<the question; H0 / H1; primary vs secondary outcomes>

## Design facts that drive the test
<within- vs between-subjects, factor(s) and levels, dependence structure —
cite the profile>

## Chosen approach
**Primary test:** <test> because <why it fits the design>.
**Assumptions to check (and fallback):**
- <assumption> — checked via <method>; if it fails → <fallback test>
**Effect size:** <which one + CI method>.
**Multiple comparisons:** <correction, or "n/a — single test">.

## Analysis steps
1. [ ] <load data, respecting the # comment / dtypes>
2. [ ] <EDA + assumption checks — see explore-data>
3. [ ] <run primary test + effect size + CI>
4. [ ] <post-hoc + correction, if applicable>

## Success criteria
### Automated (a script/command can confirm)
- [ ] assumption checks are computed and reported (not skipped)
- [ ] the test family matches the design (paired/RM for within-subjects)
- [ ] effect size + CI reported alongside every p-value
### Manual (human judgment)
- [ ] the chosen test is defensible given the assumption results
- [ ] conclusions don't overreach the design

## References
- [Profile](profile-<slug>.md)
- `AGENTS.md` — <convention used>
```

## Constraints

- **The only file you write is the plan** in `docs/`. Do not run the analysis
  here.
- **No open questions in the final plan.** Resolve every decision by reading the
  profile/AGENTS.md or asking the user.
- Success criteria MUST split into **Automated** and **Manual** — that split is
  what makes `validate-analysis` possible.

Next phase: `explore-data` checks assumptions; `statistical-tests` runs the test.
