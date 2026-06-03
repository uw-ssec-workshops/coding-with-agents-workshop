---
mode: agent
description: 'Write focused pytest tests for a target function or module.'
tools: ['readFiles', 'editFiles', 'codebase', 'runCommands']
---

# Write pytest tests

Add a small, high-value set of `pytest` tests for a target the user names.
This is the **testing / validation** phase of the research lifecycle.

Target: `${input:target:function or module to test, e.g. sci_units.converters.celsius_to_fahrenheit (blank = open file)}`.
If blank, use the currently open file `${file}`.

## Steps

1. Read the target and its existing tests (look under `tests/` and for any
   `test_*.py`). Match the project's existing test style and imports.
2. Write tests that earn their keep, in this priority order:
   - **Known-answer cases**: inputs with a value you can compute by hand
     (e.g. `0 C -> 32 F`). These catch real regressions.
   - **Properties / invariants**: round-trips (`f(g(x)) == x`),
     monotonicity, units, conservation laws relevant to the science.
   - **Edge cases**: empty input, zero, negative, NaN, boundary values.
   - **Error behavior**: that bad input raises the documented exception.
3. Use `pytest` idioms: plain `assert`, `pytest.approx` for floats,
   `pytest.mark.parametrize` for tables of cases, `pytest.raises` for errors.
4. Run the new tests with `uv run pytest` (this repo uses `uv`). Report
   pass/fail. If a test fails, decide: is it a bug in the code (flag it, do
   not silently fix) or a wrong expectation (fix the test)?

## Constraints

- **Only create/modify test files.** Do not change the code under test. If you
  find a bug, write a test that documents it (xfail if needed) and call it out.
- Prefer a few sharp tests over many shallow ones. Do not test the language
  or the standard library.
- Use `pytest.approx` for any floating-point comparison; never assert exact
  float equality.

## Output format

After writing and running, summarize:

```
Added <n> tests in <path>:
- <test name> — <what it pins down>

Run: uv run pytest <path>  ->  <X passed, Y failed>
Bugs found (not fixed): <none | file:line + description>
```
