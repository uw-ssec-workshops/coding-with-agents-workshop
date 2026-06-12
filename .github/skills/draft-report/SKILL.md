---
name: draft-report
description: 'Draft the Methods and Analysis/Results sections of a paper from the analysis artifacts — grounded strictly in what was actually computed, with no invented numbers and no fabricated citations. Use when the EDA and tests are done and someone wants a paper-ready write-up of the method and the results. Phase 5 of the analysis workflow.'
tools: ['read', 'edit/editFiles', 'search/codebase']
argument-hint: '[optional: target section or venue/style]'
---

# Draft report (phase 5 of the analysis workflow)

Write the **Methods** and **Analysis/Results** sections of the paper, using only
what the earlier phases actually established. This is where a careless agent
invents a number or a citation — your job is to refuse to.

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## Context first

Read, completely, every artifact that exists for this study:
`docs/profile-*.md`, `docs/analysis-plan-*.md`, `docs/explore-*.md`,
`docs/test-*.md`, and `AGENTS.md` (for study design and reporting style).

## What to write

Produce two sections, in this order, in markdown:

1. **Methods** — participants (n, design), apparatus/conditions, procedure,
   measures, and the **analysis approach** (which test, why, assumption checks,
   effect size, correction). Past tense, neutral, reproducible.
2. **Analysis / Results** — the findings, each one traceable to a number in
   `test-*.md`: report statistic, p, **effect size + CI**, and direction. Lead with
   the answer to the research question. State non-significant results plainly.

## Grounding rules (the point of this phase)

- **Every number must trace to an artifact.** If it isn't in `explore-*` or
  `test-*`, it does not go in the draft.
- **Never invent citations.** Where a reference is needed, write `[CITATION
  NEEDED]` (or `[CITATION NEEDED: e.g. the test's original paper]`). Do not produce
  author names, years, DOIs, or titles you cannot verify.
- **Don't overclaim.** Match the strength of the claim to the design (this is an
  experiment → causal language is OK *within* the manipulated factor; correlational
  asides are not). No "proves"; prefer "is consistent with".
- Flag anything the artifacts don't cover with `[TODO: ...]` rather than guessing.

## Output

Write the draft to `docs/draft-<slug>.md` with `## Methods` and `## Analysis`
headings. Present a short summary in chat noting every `[CITATION NEEDED]` /
`[TODO]` the human must resolve.

## Constraints

- Read-only on data and source; the only file you create is the draft in
  `docs/`.
- The draft is a **draft** — surface its gaps honestly. A draft full of visible
  `[CITATION NEEDED]` markers is correct; a draft with confident fake citations is
  a failure.

Next phase: `validate-analysis` checks the numbers and claims against the data.
