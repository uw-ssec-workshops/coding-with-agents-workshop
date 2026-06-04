# Agent Ideas

A scrolling menu so nobody freezes on "what should I build?" Each idea
includes a suggested target file, a starting tool list, and a one-line
description. Pick one and remix it into a custom agent (`.github/agents/`).

## Code review (read-only: easiest)

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `style-checker` | `read`, `search/codebase` | Flag PEP 8 violations + missing types in a file | `climate_model.py` |
| `docstring-checker` | `read`, `search/codebase` | List public functions missing docstrings, with a one-line ask | `co2_emissions.py` |
| `complexity-flagger` | `read`, `search/codebase` | Identify functions that need splitting; suggest extraction points | any |
| `naming-reviewer` | `read`, `search/codebase` | Flag confusing variable / function names in scope | `climate_model.py` (variables `c0`, `t0`, `s` are great fodder) |
| `dependency-auditor` | `read`, `search/codebase` | Read `pyproject.toml` and identify unpinned / suspicious deps | any package |

## Code generation (writes to files: slightly trickier)

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `test-author` | `read`, `edit/editFiles` | Write pytest tests for a function | `vscm.emissions` (in expected-artifacts) |
| `cli-designer` | `read`, `edit/editFiles` | Add an `argparse`-based CLI to a script | `climate_model.py` |
| `type-annotator` | `read`, `edit/editFiles` | Add type hints to functions in a file | `co2_emissions.py` |
| `pyproject-bootstrapper` | `read`, `edit/editFiles` | Generate a starter `pyproject.toml` from existing imports | climate model dir |

## Refactoring

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `tab-to-space` | `read`, `edit/editFiles` | Replace tabs with 4 spaces in selected files | `climate_model.py`, `co2_emissions.py` |
| `script-to-package` | `read`, `edit/editFiles` | Plan (in markdown) the steps to convert a flat script to a `src/` package | climate model dir |
| `extract-function` | `read`, `edit/editFiles` | Pull a code block into a named function with appropriate args | `VSCM.run` |
| `path-modernizer` | `read`, `edit/editFiles` | Replace `os.path` calls with `pathlib` equivalents | any older code |

## Domain-specific (climate / SSP)

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `ssp-explainer` | `read`, `search/codebase` | Explain a given SSP scenario in plain language with a numerical sketch | climate model |
| `forcing-equation-checker` | `read`, `search/codebase` | Read the temperature update step and verify the climate sensitivity formula | `climate_model.py:VSCM.run` |
| `co2-trajectory-summarizer` | `read`, `search/codebase` | Summarize the SSP CSV: shape, range, year coverage, columns | `SSP_CO2emissions.csv` |

## General research

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `error-explainer` | `read`, `search/codebase` | Take a Python traceback (pasted), explain in plain English, suggest fix | n/a, paste |
| `paper-summarizer` | `read` | Summarize a markdown / `.txt` document into bullets | any docs |
| `data-pipeline-reviewer` | `read`, `search/codebase` | Spot reproducibility issues (hardcoded paths, magic numbers, missing seeds) | any pipeline code |
| `repro-checklist` | `read`, `search/codebase` | Score a repo against a research-reproducibility checklist | any |

## Behavioral / social science / stats

For attendees working with survey data, behavioral experiments, mixed-methods, or applied statistics. Most of these are read-only and target a CSV or a notebook rather than a package.

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `survey-codebook-checker` | `read`, `search/codebase` | Read a survey data file + a codebook, flag mismatches (missing columns, value ranges out of spec) | any survey CSV |
| `stats-assumption-checker` | `read`, `search/codebase` | Read a stats notebook, flag where parametric tests are used without checking assumptions (normality, equal variance) | any analysis `.ipynb` or `.py` |
| `qualitative-coder-helper` | `read` | Given a coding scheme + a transcript snippet, suggest tags and explain disagreements | any interview transcript |
| `irb-redactor` | `read`, `search/codebase` | Flag identifiers (names, emails, exact dates, free-text) that might leak through to a paper-ready dataset | any participant CSV |
| `analysis-narrator` | `read`, `search/codebase` | Read a notebook of effects + p-values, draft a "results" paragraph in your field's voice (APA / AMA / your style guide) | any analysis notebook |
| `power-analysis-explainer` | `read`, `search/codebase` | Read a study design, propose what a reasonable power analysis would look like (without claiming to do the math) | any preregistration draft |

> **Tip for non-physical-science attendees:** pick `climate_model.py` only if it's faster than opening your own work. Otherwise, drop a notebook / CSV from your lab into a scratch folder and target that, the custom-agent pattern is identical.

## Experiment management

The agent reads run outputs, summarizes them, and helps drive the next iteration. Especially relevant for ML / NLP / simulation work where you launch sweeps and compare results.

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `run-summarizer` | `read`, `search/codebase` | Read a directory of run logs / CSV metrics, produce a one-page comparison table | any `runs/` or `results/` folder |
| `sweep-designer` | `read` | Given a config file + a hypothesis ("does dropout help?"), propose the next 4-8 hyperparameter combinations | any training config |
| `metric-explainer` | `read`, `search/codebase` | Read training curves (CSV / `.jsonl`) and narrate what went well, what went wrong, where to look next | any logged run |
| `failed-run-triager` | `read`, `search/codebase`, `execute/runInTerminal` | Read the last failed run's stderr + config, classify the failure (OOM / NaN loss / data issue), suggest fix | any crashed run |
| `experiment-journal` | `read`, `edit/editFiles` | Append a structured entry ("what I tried, what happened, what's next") to a markdown lab notebook | `notebook.md` |

## Onboarding

| Skill | Tools | What it does | Good target |
|---|---|---|---|
| `repo-tour-guide` | `read`, `search/codebase` | Read a repo's structure and produce a 5-bullet "what is this and where to start" doc | this workshop repo! |
| `function-of-the-day` | `read`, `search/codebase` | Pick one function in the project and explain it in detail | any |
| `glossary-builder` | `read`, `search/codebase` | Identify domain terms in a codebase and define them | climate model |

## Going-further (stretch: probably won't finish in the block, take home)

| Skill | What it does |
|---|---|
| `iterative-improver` | Multi-turn: identify one issue, fix it, run tests, identify the next, repeat |
| `pre-commit-hook-generator` | Read the project, generate a starter `.pre-commit-config.yaml` |
| `dataset-eda` | Read a CSV / parquet file and produce a 1-page exploratory analysis |

---

**A note on scope:** the most successful first agents are **boring and
narrow**. "Add docstrings to one file" beats "be my coding assistant",
because the narrow one will work and the broad one will disappoint. You
can always broaden later.
