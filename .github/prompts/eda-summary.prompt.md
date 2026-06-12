---
agent: agent
description: 'Summarize a tabular dataset: shape, columns, types, ranges, and missingness.'
tools: ['read', 'search/codebase', 'vscode/askQuestions']
---

# Exploratory data summary

Produce a quick, honest first look at a dataset so the user knows what they
are working with before they analyze it. This is the **data / EDA** phase of
the research lifecycle.

The file to summarize is: `${input:dataset:path to a .csv / .tsv / .parquet (or leave blank to use the open file)}`.
If blank, don't guess: use `#tool:vscode/askQuestions` to confirm with the user
whether to summarize the open file `${file}` or a specific dataset, then proceed.

## Steps

1. Read the file (or its header + a sample of rows if it is large; do not try
   to load a huge file into the response).
2. Report, as plainly as possible:
    - **Shape**: rows x columns (note if you only sampled).
    - **Columns**: name, inferred dtype, and a one-line meaning if it is
      guessable from the name.
    - **Ranges**: min/max (or a few example values) for numeric and date
      columns; cardinality for categoricals.
    - **Missingness**: which columns have blanks/NaNs and roughly how many.
    - **Smells**: mixed types in a column, suspicious sentinels (`-999`, `0`
      used as missing), duplicate rows, unparsed dates, encoding issues.
3. End with **3 suggested next questions** the data could answer, and any
   **caveat** a careful analyst should know before trusting it.

## Constraints

- Do not modify the file. This is read-only reconnaissance.
- Do not fabricate statistics. If you only sampled, say so and label numbers
  as estimates.
- Keep it to one screen. This is a first look, not a full report.

## Output format

```
## Dataset: <name>  (<rows> x <cols>)

| column | dtype | range / sample | missing |
|---|---|---|---|
| ... | ... | ... | ... |

**Smells:** ...
**Next questions:** 1) ... 2) ... 3) ...
**Caveat:** ...
```
