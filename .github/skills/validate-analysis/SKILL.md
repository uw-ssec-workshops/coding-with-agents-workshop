---
name: validate-analysis
description: 'Verify an analysis and its write-up against the plan and the data — re-run the test, confirm the reported numbers reproduce, confirm the right test was used for the design, and confirm the draft''s claims are supported with no fabricated citations — and report pass/fail with evidence to docs/. Use as the quality gate before trusting or shipping an analysis. Phase 6 of the analysis workflow.'
tools: ['read', 'edit/editFiles', 'search/codebase', 'execute/runInTerminal']
argument-hint: '[plan or artifacts to validate]'
---

# Validate analysis (phase 6 of the analysis workflow)

The quality gate. Without it you are trusting the agent's "Done!" — and a
confidently-wrong p-value or a fabricated citation looks exactly like a correct
one. Verify with evidence.

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## What to validate against

The `docs/analysis-plan-*.md` for the study, plus its `explore-*`, `test-*`, and
`draft-*` artifacts and `AGENTS.md`. If unsure which, list `docs/` and ask.

## Process

1. **Read the plan and all artifacts completely.** Note the success criteria
   (automated and manual) and every reported number/claim.
2. **Re-run the analysis** (`uv run python analysis.py` or equivalent) and record
   the real output. Don't assume.
3. **Check design-validity (the big one):** does the test family match the design?
   An independent-samples test on repeated-measures data is a ❌ even if it "ran".
4. **Check the assumptions were actually checked**, not skipped, and that the test
   chosen matches the assumption results (parametric only if assumptions held).
5. **Reconcile numbers:** every statistic, p-value, effect size, and CI in
   `test-*.md` and `draft-*.md` must match the re-run output. Flag mismatches with
   the file and value.
6. **Audit the draft:** are all claims supported by the results? Any overclaiming?
   Any **fabricated citation** (a real-looking reference instead of `[CITATION
   NEEDED]`)? Any leftover `[TODO]`?
7. **Write the artifact** to `docs/validate-<slug>.md` and present a short
   pass/fail summary in chat.

## Artifact structure (`docs/validate-<slug>.md`)

```
# Validation: <question>

Plan: [analysis-plan-<slug>.md](analysis-plan-<slug>.md)

## Overall: ✅ Ready | ⚠️ Issues found | ❌ Not trustworthy

## Design & assumptions
- Test matches design (repeated-measures respected): ✅ / ❌ — <note>
- Assumptions checked and test chosen accordingly: ✅ / ❌ — <note>

## Numbers reconcile (re-run vs reported)
| reported | source | re-run | match? |
|---|---|---|---|
| p=.. | test-<slug>.md | p=.. | ✅ / ❌ |

## Draft audit
- Claims supported by results: ✅ / ❌ — <note>
- No fabricated citations (only [CITATION NEEDED]): ✅ / ❌
- Overclaiming / leftover [TODO]: <list or none>

## Recommendations
- Critical (fix before trusting): ...
- Nice to have: ...
```

## Constraints

- **Actually re-run the analysis.** Validation is systematic, not a vibe check.
- Be objective: report what is, even when inconvenient. A failed validation
  narrated honestly is the whole point of this phase.
- **Read-only on data/source.** Don't fix issues here — report them. Fixes go back
  to `statistical-tests` or `draft-report`, then re-validate.
