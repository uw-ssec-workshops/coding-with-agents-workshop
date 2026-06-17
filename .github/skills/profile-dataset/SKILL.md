---
name: profile-dataset
description: 'Document a dataset and its study design exactly as they are — shape, columns, dtypes, ranges, missingness, and the stated hypothesis — and write the findings to docs/. Use when someone hands you a dataset (a CSV/TSV/parquet + maybe an AGENTS.md) and wants to understand what they are working with before any analysis. Phase 1 of the analysis workflow.'
argument-hint: '[dataset path] (defaults to the open file)'
---

# Profile dataset (phase 1 of the analysis workflow)

Build context for an analysis by **documenting the data as it exists today**. This
is the first phase of the durable profile → plan → explore → test → draft →
validate loop.

The dataset to profile: the CSV/TSV/parquet the user points you at (or the open
file). Read `AGENTS.md` first if one is present — it carries the study design and
conventions.

## Artifacts directory

Write every artifact to — and read prior-phase artifacts from — the **artifacts
directory**: `docs/` at the project root by default, or the exact path `AGENTS.md`
specifies if it sets one. Wherever this skill writes `docs/...` below,
it means *inside that directory*.

## Critical directive

Your only job is to **document and describe** the dataset and its study design.

- Do NOT run statistical tests, judge data quality, or suggest analyses yet.
- Do NOT clean, reshape, or modify the data.
- You are a documentarian, not an analyst. Describe what IS, not what SHOULD BE.

## Steps

1. **Read `AGENTS.md` first** (if present), then the dataset. For a large file,
   read the header plus a sample of rows — say so if you sampled.
2. **Describe the shape and structure:** rows × columns; is it wide or long/tidy;
   what is the unit of observation (one row = one what?).
3. **Describe each column:** name, inferred dtype, meaning (from `AGENTS.md` or the
   name), and range/sample (min–max for numeric, levels + counts for categorical).
4. **Note the design facts that matter for analysis** *without choosing a test*:
   e.g. "each subject is measured under every condition (repeated measures)",
   grouping keys, the stated outcome(s), missingness, suspicious sentinels.
5. **Write the artifact** to `docs/profile-<slug>.md` (create `docs/` if
   needed; `<slug>` from the dataset/study, lowercase-hyphenated).
6. **Present** a short summary in chat and offer to move to `plan-analysis`.

## Artifact structure (`docs/profile-<slug>.md`)

```
# Dataset profile: <study/dataset name>

## Summary
<2-4 sentences: what was measured, the design, the unit of observation>

## Shape & structure
<rows x cols; wide vs long; one row = ...>

## Columns
| column | dtype | meaning | range / levels | missing |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Study design (as stated in AGENTS.md)
<factors and levels, within- vs between-subjects, outcome(s), hypotheses —
quote the source; do not infer a test>

## Observations a plan must account for
<factual only: "rows are not independent (repeated measures on a subject key)",
"the outcome is right-skewed with an outlier at row N", "first line is a # comment">

## References
- `<data file>` (col `<name>`) — <what's here>
- `AGENTS.md` — <relevant convention>
```

## Constraints

- **Read-only on the data.** The only file you create is the profile artifact in
  `docs/`. Never modify the dataset.
- Do not fabricate statistics. If you sampled, label numbers as estimates.
- Keep the artifact self-contained: a reader should understand the dataset from it
  alone.

Next phase: hand this to `plan-analysis`.
