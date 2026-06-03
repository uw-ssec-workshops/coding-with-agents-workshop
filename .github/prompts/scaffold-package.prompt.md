---
agent: agent
description: 'Plan the conversion of a flat research script into an installable src/ package.'
tools: ['read', 'search/codebase']
---

# Scaffold a package (plan only)

Take a flat research script (or loose folder of scripts) and produce a
concrete plan to turn it into a small, installable, `uv`-managed package with
a `src/` layout. This is the **project setup** phase of the research
lifecycle.

Target: `${input:target:script or folder to package, e.g. blocks/03-research-loop/demo/starter/ (blank = open file)}`.
If blank, use the currently open file `${file}`.

## Steps

1. Read the target and any nearby `pyproject.toml`, `requirements.txt`, or
   imports. Infer the third-party dependencies actually used.
2. Propose a target layout, named after the project:

    ```
    <pkg>/
      pyproject.toml          # PEP 621 metadata, hatchling backend
      src/<pkg>/__init__.py
      src/<pkg>/<module>.py   # the script's logic, as importable functions
      tests/test_<module>.py
      README.md
    ```

3. Map **every** existing file/blob of logic to where it lands in the new
   layout. Call out top-level script code that needs wrapping in functions or
   a `if __name__ == "__main__":` / `argparse` entry point.
4. List the dependencies to declare and a sensible Python version floor.
5. Give the exact `uv` commands to bootstrap it (`uv init`, `uv add ...`,
   `uv run pytest`).

## Constraints

- **Plan only — do not create or edit files.** This command produces a
  migration plan the user can execute (or hand to the coding agent). Editing
  is out of scope here on purpose.
- Follow Scientific Python layout norms (`src/` layout, `pyproject.toml`,
  hatchling or setuptools+PEP 621). Do not invent exotic structure.
- Keep the package small. Do not propose CI, docs sites, or release tooling
  unless the user asks — that is later in the lifecycle.

## Output format

```
## Packaging plan: <pkg>

### Proposed layout
<tree>

### File-by-file migration
- <old> -> <new>: <what changes (wrap in function, add entry point, ...)>

### Dependencies
- runtime: ...
- dev: pytest, ...
- requires-python: >=3.x

### Bootstrap commands
uv init ...
uv add ...
uv run pytest
```
