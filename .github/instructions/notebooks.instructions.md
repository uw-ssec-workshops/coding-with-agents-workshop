---
applyTo: "**/*.ipynb"
---

# Jupyter notebook conventions

These instructions apply automatically whenever a Jupyter notebook is in
context. They demonstrate the **path-scoped instructions** primitive: unlike an
agent or a prompt, you never invoke this — Copilot injects it based on the
`applyTo` glob above.

When working in notebooks for this project:

- Treat the notebook as a **teaching document read top-to-bottom**, not a
  script with comments. Every code cell should be preceded by a markdown cell
  that explains *why* the code exists, not just what it does.
- Keep cells **runnable in order**. Do not rely on state from cells that have
  been deleted or that run later. A reader should be able to "Run All" and get
  the same result.
- Prefer **small, focused cells** with one idea each over a single mega-cell.
- Set a **random seed** near the top of any notebook that uses randomness, and
  call it out in prose.
- Use the project environment: this repo is `uv`-managed (Python 3.12). Do not
  emit `pip install` cells; dependencies belong in `pyproject.toml`.
- Avoid hardcoded absolute paths. Read data via a relative path or a clearly
  defined constant near the top.
- No emojis in notebook prose or output unless explicitly requested.
