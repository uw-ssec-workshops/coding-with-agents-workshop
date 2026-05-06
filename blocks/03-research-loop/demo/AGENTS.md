# Very Simple Climate Model (VSCM): agent guidance

A minimal climate model used as the running scenario in **Block 3** of the
"Coding with AI Agents" workshop. Any agent working in this directory
should read this file first.

## What this code is

Two standalone Python scripts implementing a Very Simple Climate Model:

- `climate_model.py`, class `VSCM` that integrates temperature change
  from CO2 concentrations using a climate sensitivity parameter and
  logarithmic forcing.
- `co2_emissions.py`, CO2 concentration sources: a `Constant_CO2`
  toy model and an `SSPEmissions` reader that loads
  `SSP_CO2emissions.csv` (the four standard SSP scenarios, synthetic
  values for the workshop).

Currently, this is **not a package**: no `pyproject.toml`, no `src/`
layout, no tests, no installable CLI. The whole point of the demo is to
turn it into one.

## What we want it to become

An installable Python package called **`vscm`**, following the
[Scientific Python project guidelines](https://scientific-python.org/specs/),
suitable for a research lab to `pip install` and use programmatically or
from the command line.

Concretely:

- **Layout:** `src/vscm/` with `__init__.py`, modules split sensibly
  (`model.py`, `emissions.py`, etc.).
- **Build:** `pyproject.toml` using `uv` for dev workflow and `hatchling`
  for the build backend.
- **CLI:** a `vscm` entry point (e.g., `vscm run --scenario 245 --start 2015 --end 2100 --plot`).
- **Tests:** `tests/` directory, `pytest`-based, covering the SSP loader,
  the constant-emissions toy, and the `VSCM` integrator with at least
  one snapshot test of the temperature trajectory.
- **Style:** type-annotated, formatted with `ruff`, NumPy-style docstrings
  on the public API.
- **Docs:** a short `README.md` with install + usage instructions.
- **Reproducibility:** the SSP CSV ships with the package (use
  `importlib.resources` to find it, not a relative path).

## Conventions

- Python 3.12.
- Prefer NumPy + (existing) pandas dependencies. Do not add `xarray` or
  `scipy` unless a concrete feature requires it.
- Keep matplotlib optional, gate the plotting helpers behind an extra
  (`vscm[plot]`) so headless installs work without a GUI backend.
- Use `pathlib`, not `os.path`.
- The CSV's first line is a comment that pandas should skip
  (`pd.read_csv(..., skiprows=1)`); preserve that contract or add a
  proper `# `-comment-aware loader.

## Out of scope for this demo

- Publishing to PyPI.
- Continuous integration / GitHub Actions.
- A docs site beyond a `README.md`.
- Notebook examples (a follow-up).

## How to verify the script still runs after refactoring

```bash
uv run python -m vscm --scenario 245 --start 2015 --end 2100
```

It should print (or plot, if `--plot`) a temperature trajectory that
ends roughly between +1 C and +5 C above the 2015 baseline depending on
scenario.
