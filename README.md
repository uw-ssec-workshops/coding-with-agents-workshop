# Coding with AI Agents: A Hands-On Workshop for Scientists

This repository contains the slides, demos, hands-on notebooks, and instructor notes for a ~2-hour workshop teaching scientists how AI coding agents work and how to use them well in research software engineering.

## Workshop structure

The workshop is organized into four 30-minute-ish blocks.

| # | Block | Folder | Format |
|---|---|---|---|
| 1 | The AI Coding Agent Landscape | [`blocks/01-landscape/`](blocks/01-landscape/) | Slides + demo notebook |
| 2 | How It Actually Works (post-training & tool calling) | [`blocks/02-how-it-works/`](blocks/02-how-it-works/) | Slides + model-swap notebook |
| 3 | Agent-Driven Research Software Engineering | [`blocks/03-research-loop/`](blocks/03-research-loop/) | Slides + live Copilot Chat workflow demo |
| 4 | Build Your Own Skill (capstone) | [`blocks/04-build-a-skill/`](blocks/04-build-a-skill/) | Slides + hands-on custom-agent build |

Each block folder follows a similar layout:

```
blocks/0N-name/
  README.md            # what this block teaches, learning goals, timing
  slides.md            # Marp-flavored slides
  instructor-notes.md  # speaker notes, demo script, fallbacks
  resources.md         # curated further reading
  demo/                # runnable code, starter files, notebooks
```

## Tools used

- **Copilot Chat in VSCode / Codespaces**: The Codespace ships a custom **OAI-compatible Copilot** extension ([`uw-ssec/oai-compatible-copilot`](https://github.com/uw-ssec/oai-compatible-copilot)) that points Copilot Chat at the workshop's AI gateway, so you pick the workshop's models in the model picker with no Copilot subscription or setup.
- **Copilot Chat Skills** for Block 3's research loop: `profile-dataset`, `plan-analysis`, `explore-data`, `statistical-tests`, `draft-report`, `validate-analysis`, `handoff` ship **in-repo** as [`.github/skills/<name>/SKILL.md`](.github/skills/) and run in the same Copilot Chat panel (agent mode). The agent auto-selects a skill from its `description`, or you invoke one by name.
- **Claude Models (via the workshop's gateway)**: the model backend, fronting Claude Sonnet 4.6 and Claude Haiku 4.5. Copilot Chat and the notebooks hit the same gateway. The notebooks use the **`litellm` Python SDK**, so the same agent loop works against any other model the gateway fronts.
- **Python 3.12 + `uv`**: environment and package management.
- **Marp**: slides as markdown.

You don't need anything installed locally: everything runs in a GitHub Codespace.

## Copilot customization gallery

The [`.github/`](.github/) folder is a **worked gallery** of ways to customize an AI coding agent for research software engineering with GitHub Copilot. It pairs with Block 4 ("Build Your Own Skill"): read these as references, and then write your own. Everything there is plain markdown but contains **structured prompts, tool lists, and project context**. The same ideas port to Claude Code skills, Cursor rules, and coding agent harnesses.

### The five primitives

| Primitive                    | Folder                                   | Invoked                     | Best for                                     |
| ---------------------------- | ---------------------------------------- | --------------------------- | -------------------------------------------- |
| **Project memory**           | `.github/copilot-instructions.md`        | Always on                   | Conventions every chat should know           |
| **Path-scoped instructions** | `.github/instructions/*.instructions.md` | Auto, by `applyTo` glob     | Rules for a file type (notebooks, tests)     |
| **Custom agents**            | `.github/agents/*.agent.md`              | Agent picker                | A persistent persona with a narrow tool list |
| **Commands (prompt files)**  | `.github/prompts/*.prompt.md`            | `/name` slash command       | A repeatable one-shot task                   |
| **Skills**                   | `.github/skills/<name>/SKILL.md`         | On demand (auto or `/name`) | A multi-step capability that bundles scripts |

> **Note on naming:** custom agents were previously called **custom chat
> modes** (`.chatmode.md` in `.github/chatmodes/`). VS Code renamed them to
> custom agents (`.agent.md` in `.github/agents/`); the functionality is the
> same. This repo uses the current `.agent.md` form.

### Mapped to the research-software lifecycle


| Lifecycle phase           | What it is                                          | Primitive    | Location                                                                                                  |
| ------------------------- | -------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| Research loop (Block 3)   | Seven skills, each writing an artifact to `docs/`   | skills       | [`.github/skills/`](.github/skills/)                                                                      |
| Full analysis loop        | Orchestrate the seven research-loop skills          | agent        | [`research-data-scientist`](.github/agents/research-data-scientist.agent.md)                              |
| Project setup             | Flat script → installable package (plan)            | command      | [`scaffold-package`](.github/prompts/scaffold-package.prompt.md)                                          |
| Data / EDA                | First look at a dataset                             | command      | [`eda-summary`](.github/prompts/eda-summary.prompt.md)                                                    |
| Implementation / planning | Read-only thinking partner, then hand off           | agent        | [`research-pair`](.github/agents/research-pair.agent.md)                                                  |
| Testing / validation      | Focused pytest tests for a target                  | command      | [`write-tests`](.github/prompts/write-tests.prompt.md)                                                    |
| Reproducibility           | Audit for paths, seeds, pinned env                  | agent        | [`reproducibility-auditor`](.github/agents/reproducibility-auditor.agent.md)                              |
| Documentation             | Add NumPy-style docstrings                          | agent        | [`docstring-writer`](.github/agents/docstring-writer.agent.md)                                            |
| Code review               | Review vs Scientific Python guidelines              | agent        | [`scientific-python-reviewer`](.github/agents/scientific-python-reviewer.agent.md)                        |
| Packaging / publication   | Draft `CITATION.cff` + release notes                | command      | [`citation-and-release`](.github/prompts/citation-and-release.prompt.md)                                  |
| Conventions (notebooks)   | Notebook-as-teaching-document rules                 | instructions | [`notebooks.instructions.md`](.github/instructions/notebooks.instructions.md)                             |
| Conventions (tests)       | pytest + `uv` conventions                           | instructions | [`tests.instructions.md`](.github/instructions/tests.instructions.md)                                     |

### How to try them in this Codespace

- **Agents:** open Copilot Chat → the **agent picker** at the top of the panel
  → choose an agent (e.g. `reproducibility-auditor`). If it is missing, run
  **Developer: Reload Window**.
- **Commands:** type `/` in chat and pick a prompt (e.g.
  `/eda-summary`), or pass the input: `/write-tests target=sci_units.converters`.
- **Skills:** ask in plain language ("profile the text-entry dataset in
  `blocks/03-research-loop/demo/starter/`") and the matching research-loop skill
  (here `profile-dataset`) loads on demand.
- **Instructions:** open a notebook or a file under `tests/` and they apply
  automatically.


## Repo conventions

- One folder per block, reusable layout.
- All Python work goes through `uv` (`uv run pytest`, `uv add <pkg>`, etc.).
- Notebooks are written to be read top-to-bottom as a teaching document, not just executed.
- Slides are written for the **Marp for VS Code** extension (preinstalled in the Codespace). Open any `slides.md` and click the preview icon, or run **`Marp: Export Slide Deck...`** from the command palette to produce HTML/PDF/PPTX.


## Contact

- **Anshul Tambay**, UW SSEC, [anshul37@uw.edu](mailto:anshul37@uw.edu)
