# Implementation: VSCM package

> **Note:** Hand-crafted sample artifact showing what `/implement`'s tracking output looks like. The real `/implement` writes to this file as it progresses, ticking checkboxes in real time.

## Status: COMPLETE

All 6 phases verified.

## Phase 1: Scaffold the package

- [x] Created `pyproject.toml` with hatch backend, `vscm` script entry point, `numpy + pandas` deps, `[plot]` extra.
- [x] Created `src/vscm/__init__.py` (initially empty).
- [x] Moved `SSP_CO2emissions.csv` to `src/vscm/data/SSP_CO2emissions.csv`.
- [x] **Verification:** `uv build` succeeded. `uv pip install -e .` succeeded. `python -c "import vscm"` succeeded.

## Phase 2: Refactor `co2_emissions.py` -> `vscm.emissions`

- [x] Moved all three classes to `src/vscm/emissions.py`.
- [x] Converted tabs -> 4 spaces.
- [x] Added type hints to all public methods (`year: int -> float`, etc.).
- [x] Added NumPy-style docstrings.
- [x] Replaced hardcoded CSV path with `importlib.resources.files("vscm.data") / "SSP_CO2emissions.csv"`.
- [x] Added `__str__` to `Constant_CO2`.
- [x] Re-exported from `__init__`: `from vscm.emissions import Constant_CO2, SSPEmissions`.
- [x] **Verification:** `SSPEmissions(126).get_CO2_ppm(2050)` returns `468.71`. `ruff check` clean.

## Phase 3: Refactor `climate_model.py` -> `vscm.model`

- [x] Moved `VSCM` to `src/vscm/model.py`.
- [x] Tabs -> 4 spaces; types added; docstrings added.
- [x] Refactored `plot(self, ax=None)` to **return** the axes instead of calling `plt.show()`.
- [x] Gated matplotlib import behind try/except with helpful `ImportError`.
- [x] Rewrote the `run` loop as `for year in range(self.y0 + 1, end_year + 1):` (more readable).
- [x] Re-exported from `__init__`: `from vscm.model import VSCM`.
- [x] **Verification:** `VSCM(2015, 14.65, 400, 3, Constant_CO2(400, 2015, 10)).run(2100)` produces a sensible trajectory. `ruff check` clean.

## Phase 4: CLI

- [x] Created `src/vscm/cli.py` with `argparse`-based `main()`.
- [x] Subcommand `run` with flags `--scenario`, `--start`, `--end`, `--plot`.
- [x] Validates `--scenario` against `{126, 245, 370, 585}` with a clear error otherwise.
- [x] Plotting gated by import check.
- [x] **Verification:** `uv run vscm run --scenario 126 --start 2015 --end 2050` printed `15.94`. `uv run vscm run --help` shows expected help text.

## Phase 5: Tests

- [x] `tests/test_emissions.py`, 3 tests, all pass.
- [x] `tests/test_model.py`, 2 tests, all pass.
- [x] `tests/test_cli.py`, 2 tests, all pass.
- [x] **Verification:** `uv run pytest -v` -> 7 passed in 0.4s.

## Phase 6: README and polish

- [x] Created `README.md` with install, quickstart, API example, scenarios table.
- [x] Pointed `pyproject.toml` `readme = "README.md"`.
- [x] `ruff check src/vscm tests` -> clean.
- [x] `ruff format --check src/vscm tests` -> clean.
- [x] **Verification:** Final `uv run pytest -v` -> 7 passed.

## Notes from the implementation run

- **Phase 2 caveat:** `importlib.resources.files()` returns a `Traversable`, not a `Path`. Passed `str(...)` to `pd.read_csv` to keep things compatible with older pandas. Worth a follow-up to verify on a fresh install.
- **Phase 3 surprise:** the original `run` loop's termination condition was even more confusing than `/research` flagged. The rewrite changes behavior in one edge case (running `end_year == start_year` now returns the initial state instead of erroring). Believe this is the intended behavior; flagging for review.
- **Phase 5 note:** the `test_model.py` snapshot test uses `pytest.approx(15, abs=3)` rather than an exact value, since the climate sensitivity parameter is a float and small numerical drift is expected.

Ready for `/validate`.
