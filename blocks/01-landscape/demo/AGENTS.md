# sci_units: agent guidance

A tiny scientific unit-conversion library used as the running scenario in the
"Coding with AI Agents" workshop. This file is **project memory**: any agent
working in this repo should read it first.

## What this package is

- A single module, `sci_units.converters`, with a few temperature conversion
  functions (Fahrenheit / Celsius / Kelvin).
- Tests live in `starter/tests/` and run with `pytest`.
- The package is intentionally minimal so workshop demos stay legible.

## Conventions

- Python 3.12, type-annotated, formatted with `ruff`.
- No external numerical dependencies for this package, keep it stdlib only.
  (If a future feature genuinely needs `pint` or `numpy`, add it to
  `pyproject.toml` and explain why in the commit message.)
- Functions take and return plain `float`s. No unit objects, no exceptions
  for out-of-range temperatures (yet).

## How to run things

```bash
# from blocks/01-landscape/demo/starter/
uv run pytest -v
```
