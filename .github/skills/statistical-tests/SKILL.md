---
name: statistical-tests
description: 'Run the confirmatory statistical test an analysis plan specifies — honoring the study design and the assumption-check results — and report the statistic, p-value, effect size, and a CI (when one is computed) to docs/, with no fabricated numbers. Use when the plan and assumption checks are done and someone wants the actual test result. Phase 4 of the analysis workflow.'
tools: ['read', 'edit/editFiles', 'search/codebase', 'execute/runInTerminal']
argument-hint: '[optional: force a specific test]'
---

# Statistical tests (phase 4 of the analysis workflow)

Run the confirmatory test, the right one for the design and the assumption results,
and report it honestly. Every number you report must come from code you actually
executed.

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## Context first

1. Read the `docs/analysis-plan-*.md` and `docs/explore-*.md` completely:
   the planned test, the fallback, and whether the assumptions held.
2. Read `AGENTS.md` (alpha, seed, effect-size + CI requirement, multiple-comparison
   policy).

## Steps

1. **Pick the test the evidence supports.** If the assumption checks in
   `explore-*` failed for the parametric test, use the planned **fallback** (e.g.
   Friedman instead of RM-ANOVA) — do not run the parametric test anyway. **Never**
   run an independent-samples test on repeated-measures data.
2. **Write a small, runnable analysis script** (e.g. `analysis.py` in the working
   dir, or a `docs/` scratch script) that loads the data with the seed, runs the
   test, and prints the results. Keep it reproducible.
3. **Run it** and capture the real output.
4. **Report, for each test:** test name, statistic, df (if any), p-value,
   **effect size** (plus a **95% CI when you actually compute one** — otherwise
   state "CI not computed"), and n.
5. **Post-hoc + correction** if there are 3+ conditions: pairwise tests with the
   planned correction (e.g. Holm), reported in a table.
6. **Write the artifact** to `docs/test-<slug>.md` and present the headline
   result (with effect size, not just "p < .05") in chat.

## Artifact structure (`docs/test-<slug>.md`)

```
# Test results: <question>

Test chosen: <test> — because assumptions <held / failed: see explore-<slug>.md>.

## Primary result
- <test>: stat=<..>, p=<..> (alpha=<..>) → <reject / fail to reject H0>
- Effect size: <name>=<..> (95% CI [<..>, <..>] if computed, else "CI not computed")
- n = <..>

## Post-hoc (if applicable, corrected)
| comparison | stat | p (raw) | p (Holm) | effect size |
|---|---|---|---|---|

## Reproduce
- script: `analysis.py`
- command: `uv run python analysis.py`

## References
- [Analysis plan](analysis-plan-<slug>.md)
- [EDA & assumptions](explore-<slug>.md)
```

## Constraints

- **No fabricated numbers, ever.** If you didn't run it, don't report it. Paste
  results from the actual run.
- Report an **effect size alongside every p-value** — a p-value alone is not a
  result. Add a 95% CI **when you compute one**; if you don't, write "CI not
  computed" rather than inventing an interval.
- Don't reshape or edit the source data; the only files you create are the analysis
  script and the `docs/` artifact.
- If reality contradicts the plan (e.g. an assumption you expected to hold fails),
  **stop and say so** — switching to the fallback is fine, but make it visible.

Next phase: `draft-report` writes it up; `validate-analysis` checks it.
