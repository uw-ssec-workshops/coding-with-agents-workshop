---
applyTo: "**/tests/**/*.py"
---

# Test conventions

These instructions apply automatically to files under any `tests/` directory.
They demonstrate the **path-scoped instructions** primitive — Copilot injects
them based on the `applyTo` glob above, with no action from you.

When writing or editing tests in this project:

- Use **`pytest`**, not `unittest`. Plain `assert`; no `self.assertEqual`.
- Run tests with **`uv run pytest`** (this repo is `uv`-managed).
- Compare floats with **`pytest.approx`**, never exact `==`.
- Use **`pytest.mark.parametrize`** for tables of known-answer cases instead of
  copy-pasted test bodies.
- Use **`pytest.raises`** to assert documented error behavior.
- Name tests for the behavior they pin down (`test_celsius_to_fahrenheit_freezing`),
  not the function name alone (`test_convert`).
- Prefer a few **sharp, meaningful** tests (known answers, invariants, edge
  cases, error paths) over many shallow ones. Do not test the standard library.
- A test must be able to **fail**: if you cannot describe what bug a test would
  catch, it probably is not worth writing.
