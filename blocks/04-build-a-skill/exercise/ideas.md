# Skill Ideas

A scrolling menu so nobody freezes on "what should I build?" Each idea
includes a suggested target file, a starting tool list, and a one-line
description. Pick one and remix it.

## Code review (read-only: easiest)

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `style-checker` | `readFiles`, `codebase` | Flag PEP 8 violations + missing types in a file | `climate_model.py` |
| `docstring-checker` | `readFiles`, `codebase` | List public functions missing docstrings, with a one-line ask | `co2_emissions.py` |
| `complexity-flagger` | `readFiles`, `codebase` | Identify functions that need splitting; suggest extraction points | any |
| `naming-reviewer` | `readFiles`, `codebase` | Flag confusing variable / function names in scope | `climate_model.py` (variables `c0`, `t0`, `s` are great fodder) |
| `dependency-auditor` | `readFiles`, `codebase` | Read `pyproject.toml` and identify unpinned / suspicious deps | any package |

## Code generation (writes to files: slightly trickier)

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `test-author` | `readFiles`, `editFiles` | Write pytest tests for a function | `vscm.emissions` (in expected-artifacts) |
| `cli-designer` | `readFiles`, `editFiles` | Add an `argparse`-based CLI to a script | `climate_model.py` |
| `type-annotator` | `readFiles`, `editFiles` | Add type hints to functions in a file | `co2_emissions.py` |
| `pyproject-bootstrapper` | `readFiles`, `editFiles` | Generate a starter `pyproject.toml` from existing imports | climate model dir |

## Refactoring

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `tab-to-space` | `readFiles`, `editFiles` | Replace tabs with 4 spaces in selected files | `climate_model.py`, `co2_emissions.py` |
| `script-to-package` | `readFiles`, `editFiles` | Plan (in markdown) the steps to convert a flat script to a `src/` package | climate model dir |
| `extract-function` | `readFiles`, `editFiles` | Pull a code block into a named function with appropriate args | `VSCM.run` |
| `path-modernizer` | `readFiles`, `editFiles` | Replace `os.path` calls with `pathlib` equivalents | any older code |

## Domain-specific (climate / SSP)

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `ssp-explainer` | `readFiles`, `codebase` | Explain a given SSP scenario in plain language with a numerical sketch | climate model |
| `forcing-equation-checker` | `readFiles`, `codebase` | Read the temperature update step and verify the climate sensitivity formula | `climate_model.py:VSCM.run` |
| `co2-trajectory-summarizer` | `readFiles`, `codebase` | Summarize the SSP CSV: shape, range, year coverage, columns | `SSP_CO2emissions.csv` |

## General research

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `error-explainer` | `readFiles`, `codebase` | Take a Python traceback (pasted), explain in plain English, suggest fix | n/a, paste |
| `paper-summarizer` | `readFiles` | Summarize a markdown / `.txt` document into bullets | any docs |
| `data-pipeline-reviewer` | `readFiles`, `codebase` | Spot reproducibility issues (hardcoded paths, magic numbers, missing seeds) | any pipeline code |
| `repro-checklist` | `readFiles`, `codebase` | Score a repo against a research-reproducibility checklist | any |

## Onboarding

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `repo-tour-guide` | `readFiles`, `codebase` | Read a repo's structure and produce a 5-bullet "what is this and where to start" doc | this workshop repo! |
| `function-of-the-day` | `readFiles`, `codebase` | Pick one function in the project and explain it in detail | any |
| `glossary-builder` | `readFiles`, `codebase` | Identify domain terms in a codebase and define them | climate model |

## Going-further (stretch: probably won't finish in the block, take home)

| Skill | What it does |
|---|---|
| `iterative-improver` | Multi-turn: identify one issue, fix it, run tests, identify the next, repeat |
| `pre-commit-hook-generator` | Read the project, generate a starter `.pre-commit-config.yaml` |
| `dataset-eda` | Read a CSV / parquet file and produce a 1-page exploratory analysis |

---

**A note on scope:** the most successful first chatmodes are **boring and
narrow**. "Add docstrings to one file" beats "be my coding assistant",
because the narrow one will work and the broad one will disappoint. You
can always broaden later.
