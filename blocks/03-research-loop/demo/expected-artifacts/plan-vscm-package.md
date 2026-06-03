# Plan: Package the VSCM scripts as `vscm`

> **Note:** Hand-crafted sample artifact. Live `/plan` runs may differ in detail; the *shape* (phases with file paths, automated + manual verification, no open questions) is the load-bearing thing.

## Goal

Turn `climate_model.py` + `co2_emissions.py` (currently standalone scripts in `blocks/03-research-loop/demo/starter/`) into an installable Python package called `vscm`, with tests and a CLI, following the conventions in `AGENTS.md`.

## Architecture

- **Layout:** `src/vscm/` with `__init__.py`, `model.py`, `emissions.py`, `data/SSP_CO2emissions.csv`, and `cli.py`.
- **Build:** `pyproject.toml` using `hatchling` as the build backend, `uv` for dev workflow.
- **Public API** re-exported from `vscm.__init__`: `VSCM`, `Constant_CO2`, `SSPEmissions`.
- **CLI** entry point: `vscm = vscm.cli:main`. Subcommands: `vscm run --scenario {126,245,370,585} --start <yr> --end <yr> [--plot]`.
- **Tests** in `tests/` mirror the package layout: `test_model.py`, `test_emissions.py`, `test_cli.py`.

## Phases

### Phase 1: Scaffold the package

**Files:**

- Create `pyproject.toml`
- Create `src/vscm/__init__.py`
- Create `src/vscm/data/SSP_CO2emissions.csv` (move from current location)

**Tasks:**

1. Write `pyproject.toml` with `[project]` metadata (name=`vscm`, version=`0.1.0`, deps=`numpy>=2`, `pandas>=2`), `[project.optional-dependencies]` `plot = ["matplotlib>=3"]`, `[project.scripts]` `vscm = "vscm.cli:main"`, and `[tool.hatch.build.targets.wheel]` `packages = ["src/vscm"]`.
2. Empty `src/vscm/__init__.py` for now (re-exports added in Phase 2).
3. `git mv blocks/03-research-loop/demo/starter/SSP_CO2emissions.csv src/vscm/data/SSP_CO2emissions.csv` (or copy if mv breaks).

**Automated verification:**

- `uv build` succeeds.
- `uv pip install --editable .` succeeds.
- `python -c "import vscm; print(vscm.__name__)"` prints `vscm`.

**Manual verification:**

- Open `pyproject.toml` and confirm metadata reads sensibly.

### Phase 2: Refactor `co2_emissions.py` into `vscm.emissions`

**Files:**

- Create `src/vscm/emissions.py`
- Modify `src/vscm/__init__.py` to re-export

**Tasks:**

1. Move all three classes (`BaseCO2`, `Constant_CO2`, `SSPEmissions`) into `src/vscm/emissions.py`.
2. Convert tabs to 4-space indentation. Add type hints (`year: int -> float`, etc.). Add NumPy-style docstrings on public methods.
3. Replace the hardcoded CSV path in `SSPEmissions._read_ssp_csv` with `importlib.resources`:
   ```python
   from importlib.resources import files
   csv_path = files("vscm.data") / "SSP_CO2emissions.csv"
   df = pd.read_csv(csv_path, skiprows=1)
   ```
4. Add `__str__` to `Constant_CO2` for parity with `SSPEmissions`.
5. Re-export from `__init__`: `from vscm.emissions import Constant_CO2, SSPEmissions`.

**Automated verification:**

- `uv run python -c "from vscm import SSPEmissions; print(SSPEmissions(126).get_CO2_ppm(2050))"` prints a float around 470.
- `ruff check src/vscm/emissions.py` passes.

**Manual verification:**

- Visually inspect that the type hints match the runtime behavior.

### Phase 3: Refactor `climate_model.py` into `vscm.model`

**Files:**

- Create `src/vscm/model.py`
- Modify `src/vscm/__init__.py` to re-export

**Tasks:**

1. Move `class VSCM` into `src/vscm/model.py`. Tabs -> 4-space; add types; docstrings.
2. Replace `def plot(self)` (which calls `plt.show()`) with `def plot(self, ax=None) -> "matplotlib.axes.Axes"` that **returns** the axes. Caller decides whether to `plt.show()`.
3. Gate the matplotlib import behind a try/except; raise an `ImportError` with a helpful message if `vscm[plot]` extra isn't installed.
4. Clarify the `run` loop, rewrite as `for year in range(self.y0, end_year + 1):` for readability.
5. Re-export from `__init__`: `from vscm.model import VSCM`.

**Automated verification:**

- `uv run python -c "from vscm import VSCM, Constant_CO2; m = VSCM(2015, 14.65, 400, 3, Constant_CO2(400, 2015, 10)); m.run(2100); print(m.temp[-1])"` prints a float (rough sanity check, value depends on the bug-fix in step 4).
- `ruff check src/vscm/model.py` passes.

**Manual verification:**

- Confirm temperature trajectories look monotonic for a high-emissions scenario.

### Phase 4: Add the CLI

**Files:**

- Create `src/vscm/cli.py`

**Tasks:**

1. Use `argparse` (no new dep). Subcommand `run` with flags `--scenario`, `--start`, `--end`, `--plot`.
2. `main()` function that parses args, constructs `SSPEmissions(scenario)`, builds a `VSCM`, runs to `--end`, and prints final temperature. If `--plot`, calls `model.plot()` and `plt.show()` (gated by an import check).
3. Pretty error message if `--scenario` isn't one of the supported aliases.

**Automated verification:**

- `uv run vscm run --scenario 126 --start 2015 --end 2050` prints a temperature.
- `uv run vscm run --help` prints help text mentioning `--scenario`, `--start`, `--end`, `--plot`.

**Manual verification:**

- `uv run vscm run --scenario 585 --plot` opens a window with a plot (skip if running headless).

### Phase 5: Tests

**Files:**

- Create `tests/__init__.py`
- Create `tests/test_emissions.py`
- Create `tests/test_model.py`
- Create `tests/test_cli.py`

**Tasks:**

1. `test_emissions.py`:
   - `Constant_CO2(c0=400, year0=2015, rate=10)` has `get_CO2_ppm(2015) == 400`.
   - `SSPEmissions(126).get_CO2_ppm(2015) == 400` (anchor row).
   - `SSPEmissions(126).get_CO2_ppm(2100) == pytest.approx(445, abs=2)` (synthetic anchor).
2. `test_model.py`:
   - `VSCM(2015, 14.65, 400, 3, Constant_CO2(400, 2015, 0))` with zero emissions and 2015 baseline produces a flat temperature trajectory.
   - Snapshot test: `VSCM(...).run(2100)` for SSP1-2.6 produces a `temp[-1]` within `(15, 18)`.
3. `test_cli.py` (use `pytest.CaptureFixture` and `monkeypatch`):
   - Invoking `main(["run", "--scenario", "126", "--start", "2015", "--end", "2050"])` runs cleanly and prints a number.
   - Invoking with `--scenario 999` exits with a non-zero status and an error mentioning "scenario".

**Automated verification:**

- `uv run pytest -v` -> all green.
- `uv run pytest --collect-only | wc -l` >= 6 (sanity check that tests were discovered).

**Manual verification:**

- None, pytest passing is the verification.

### Phase 6: README and final polish

**Files:**

- Create `README.md`
- Modify `pyproject.toml` (point `readme = "README.md"`)

**Tasks:**

1. README sections: install (`pip install vscm`), quickstart (5-line CLI example), API example (5-line Python example), available scenarios (table).
2. Run `ruff check src/vscm tests` and `ruff format src/vscm tests`. Fix anything left.
3. Run all tests one more time.

**Automated verification:**

- `ruff check src/vscm tests` -> clean.
- `ruff format --check src/vscm tests` -> clean.
- `uv run pytest -v` -> all green.

**Manual verification:**

- README renders cleanly on GitHub (preview locally with a markdown previewer).

## Out of scope (per `AGENTS.md`)

- Publishing to PyPI.
- CI / GitHub Actions.
- Docs site (just a README).
- Notebook examples.

## Open questions

**None.** All decisions made above. If something feels ambiguous during `/implement`, stop and update this plan (it's plain markdown) rather than guessing.
