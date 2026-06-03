# Research: VSCM Package Structure

> **Note:** This is a hand-crafted sample artifact, used as a live-demo fallback if the live `/research` command misbehaves on the day. It is structured to look like a real `/research` output so attendees can study it as a reference. The first run of `/research` against the actual climate model code will produce something similar in shape.

## Question

> *"I have two standalone Python scripts (`climate_model.py` and `co2_emissions.py`) implementing a Very Simple Climate Model. Research the current code structure, identify what's missing for it to be an installable scientific Python package, and document existing conventions and quirks."*

## Summary

The codebase consists of two standalone scripts (`climate_model.py:1-66` and `co2_emissions.py:1-58`) implementing a logarithmic-forcing climate model with two CO2 emission scenarios (a constant-rate toy and an SSP CSV reader). The code is **not currently a package**: it has no `pyproject.toml`, no `src/` layout, no tests, and several Python style issues (mixed tabs/spaces, missing type hints, hardcoded relative paths). The `AGENTS.md` file states the goal is to package this as `vscm` following Scientific Python community guidelines.

## Code structure as it exists today

### `climate_model.py` (66 lines)

- Defines `class VSCM` with `__init__`, `run`, and `plot` methods (`climate_model.py:8-47`).
- Top-level `if __name__ == '__main__'` block runs the model from 2015-2100 using SSP1-2.6 (`climate_model.py:51-65`).
- **Imports:** `numpy`, `matplotlib.pyplot`, and `co2_emissions` (`climate_model.py:4-6`).
- **Tabs, not spaces.** Inconsistent with PEP 8 (`climate_model.py:8` and throughout).
- **No type hints.** Public API surface is undocumented at the type level.
- **No docstrings** beyond the file-header comment.
- **`plot()` calls `plt.show()` directly**: couples the model to a GUI backend, which breaks headless runs (`climate_model.py:47`).
- The `run` loop's termination condition is unusual: `while i + self.time[-1] <= end_year` (`climate_model.py:21`). Combined with `year = self.y0 + i`, this is effectively `i < end_year - start_year`, but the form is hard to read and may have an off-by-one if `end_year` equals the start.

### `co2_emissions.py` (58 lines)

- Defines `class BaseCO2` with abstract `get_CO2_ppm(year)` (`co2_emissions.py:3-8`).
- Two concrete implementations:
  - `Constant_CO2`, analytic exponential approach to a steady state (`co2_emissions.py:10-25`).
  - `SSPEmissions`, reads a CSV via `pd.read_csv('SSP_CO2emissions.csv', skiprows=1)` (`co2_emissions.py:38-41`).
- **Hardcoded relative path** to the CSV. Will break the moment the script is run from any directory other than `demo/starter/` (`co2_emissions.py:39`).
- **CSV is referenced but not part of any package data mechanism.** A future `pip install vscm` would have nothing to load.
- **`SSPEmissions.__str__` exists but `Constant_CO2.__str__` does not** (`co2_emissions.py:36-37`). Inconsistent.
- Tabs, no types, no docstrings, same as `climate_model.py`.
- Top-level `if __name__ == '__main__'` block exercises both classes (`co2_emissions.py:48-58`).

### `SSP_CO2emissions.csv`

- 88 lines: 1 comment row (skipped by `skiprows=1`), 1 header row (`Year,126,245,370,585`), 86 data rows for years 2015-2100.
- Columns are SSP scenario aliases as **strings of integers** (e.g., `"126"` for SSP1-2.6). The reader passes the integer scenario and the column lookup happens via `df[self._scheme]` after `self._scheme = str(scheme)` (`co2_emissions.py:5, 41`).
- Synthetic values; not authoritative IPCC data.

### `AGENTS.md`

States explicit conventions and goals (read in full before planning):
- Layout: `src/vscm/` with `__init__.py`, modules split sensibly.
- Build: `pyproject.toml` with `uv` for dev workflow and `hatchling` for build backend.
- CLI: `vscm` entry point (`vscm run --scenario 245 --start 2015 --end 2100 --plot`).
- Tests in `tests/`, pytest-based; cover loader, toy emissions, and integrator.
- Type-annotated, `ruff`-formatted, NumPy-style docstrings on public API.
- **Out of scope:** PyPI publishing, CI, docs site, notebooks.

## Gaps between current state and "installable package"

| Gap | Where it bites today | Required for the package |
|---|---|---|
| No `pyproject.toml` | Can't `pip install` | Build backend (`hatchling`), entry points, deps |
| No package layout | Imports break outside cwd | `src/vscm/{__init__.py, model.py, emissions.py, ...}` |
| No tests | Nothing protects refactors | `tests/` with pytest |
| No type hints | IDE / mypy can't help | Annotate public API |
| Hardcoded CSV path | Breaks on install | `importlib.resources` |
| `plt.show()` coupled to model | Breaks headless | Optional `[plot]` extra; return fig instead of showing |
| Mixed tabs / no formatter | Drift over time | `ruff` config in `pyproject.toml` |
| No CLI | Only-script-entry usage | `argparse` or `click` entry point |
| No `README.md` | New users have no on-ramp | Install + usage instructions |

## Existing conventions to preserve

- **NumPy is already a dependency.** Don't replace it.
- **Pandas is already a dependency** (used by `SSPEmissions._read_ssp_csv`). Don't replace it with `csv` stdlib unless there's a strong reason.
- **`AGENTS.md` says no `xarray` or `scipy`.** Stick with that.
- **The `_co2_ppm` interface (`get_CO2_ppm(year) -> float`) is the contract** between `VSCM` and emissions classes. Preserve it across the refactor.
- **Public class names (`VSCM`, `Constant_CO2`, `SSPEmissions`) are likely already used downstream** by the demo author. Re-export from `vscm.__init__` so existing imports break minimally.

## Open questions for `/plan`

- Should the CLI use `argparse` (stdlib) or `click` (extra dep)? `AGENTS.md` says "minimize deps"; default to `argparse`.
- Should `Constant_CO2` and `SSPEmissions` move to one `emissions.py` or each get their own file? Suggest one `emissions.py` for now (~50 lines combined, no need to split).
- Should the demo's `if __name__ == '__main__'` block become a package-level entry point or be moved to an `examples/` directory? Suggest examples + a thin CLI; keep them in sync.
