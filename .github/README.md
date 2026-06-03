# `.github/` — Copilot customization gallery

This folder is a **worked gallery** of the ways you can customize an AI coding
agent for research software engineering, using GitHub Copilot's current
customization surface. It pairs with Block 4 of the workshop ("Build Your Own
Skill"): read these as references, then write your own.

Everything here is plain markdown (plus one tiny Python helper). The whole point
of the workshop's spine — _all coding agents work the same way under the hood_ —
is that these files are just **structured prompts + tool lists + project
memory**. The same ideas port to Claude Code skills, Cursor rules, and others.

## The five primitives

| Primitive                    | Folder                           | Invoked                     | Best for                                     |
| ---------------------------- | -------------------------------- | --------------------------- | -------------------------------------------- |
| **Project memory**           | `copilot-instructions.md`        | Always on                   | Conventions every chat should know           |
| **Path-scoped instructions** | `instructions/*.instructions.md` | Auto, by `applyTo` glob     | Rules for a file type (notebooks, tests)     |
| **Custom agents**            | `agents/*.agent.md`              | Agent picker                | A persistent persona with a narrow tool list |
| **Commands (prompt files)**  | `prompts/*.prompt.md`            | `/name` slash command       | A repeatable one-shot task                   |
| **Skills**                   | `skills/<name>/SKILL.md`         | On demand (auto or `/name`) | A multi-step capability that bundles scripts |

> **Note on naming:** custom agents were previously called **custom chat
> modes** (`.chatmode.md` in `.github/chatmodes/`). VS Code renamed them to
> custom agents (`.agent.md` in `.github/agents/`); the functionality is the
> same. This repo uses the current `.agent.md` form.

## Mapped to the research-software lifecycle

These demos are deliberately **narrow** — each does one job on one phase of a
research project. Narrow agents work; "be my coding assistant" disappoints.

| Lifecycle phase           | What it is                                                                                                                                  | Primitive    | File                                                                                                                                                                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Research loop (Block 3)   | `/research` → `/plan` → `/iterate-plan` → `/experiment` → `/implement` → `/validate` (+ `/handoff`), each writing an artifact to `.agents/` | commands     | [`research`](prompts/research.prompt.md), [`plan`](prompts/plan.prompt.md), [`iterate-plan`](prompts/iterate-plan.prompt.md), [`experiment`](prompts/experiment.prompt.md), [`implement`](prompts/implement.prompt.md), [`validate`](prompts/validate.prompt.md), [`handoff`](prompts/handoff.prompt.md) |
| Project setup             | Flat script → installable package (plan)                                                                                                    | command      | [`prompts/scaffold-package.prompt.md`](prompts/scaffold-package.prompt.md)                                                                                                                                                                                                                               |
| Data / EDA                | First look at a dataset                                                                                                                     | command      | [`prompts/eda-summary.prompt.md`](prompts/eda-summary.prompt.md)                                                                                                                                                                                                                                         |
| Implementation / planning | Read-only thinking partner, then hand off                                                                                                   | agent        | [`agents/research-pair.agent.md`](agents/research-pair.agent.md)                                                                                                                                                                                                                                         |
| Testing / validation      | Focused pytest tests for a target                                                                                                           | command      | [`prompts/write-tests.prompt.md`](prompts/write-tests.prompt.md)                                                                                                                                                                                                                                         |
| Experiment management     | Summarize a run, append to a lab notebook                                                                                                   | skill        | [`skills/experiment-log/`](skills/experiment-log/)                                                                                                                                                                                                                                                       |
| Reproducibility           | Audit for paths, seeds, pinned env                                                                                                          | agent        | [`agents/reproducibility-auditor.agent.md`](agents/reproducibility-auditor.agent.md)                                                                                                                                                                                                                     |
| Documentation             | Add NumPy-style docstrings                                                                                                                  | agent        | [`agents/docstring-writer.agent.md`](agents/docstring-writer.agent.md)                                                                                                                                                                                                                                   |
| Code review               | Review vs Scientific Python guidelines                                                                                                      | agent        | [`agents/scientific-python-reviewer.agent.md`](agents/scientific-python-reviewer.agent.md)                                                                                                                                                                                                               |
| Packaging / publication   | Draft `CITATION.cff` + release notes                                                                                                        | command      | [`prompts/citation-and-release.prompt.md`](prompts/citation-and-release.prompt.md)                                                                                                                                                                                                                       |
| Conventions (notebooks)   | Notebook-as-teaching-document rules                                                                                                         | instructions | [`instructions/notebooks.instructions.md`](instructions/notebooks.instructions.md)                                                                                                                                                                                                                       |
| Conventions (tests)       | pytest + `uv` conventions                                                                                                                   | instructions | [`instructions/tests.instructions.md`](instructions/tests.instructions.md)                                                                                                                                                                                                                               |

The two **worked examples** referenced throughout Block 4 are
`scientific-python-reviewer` (read-only) and `docstring-writer` (write-mode).
The rest of the gallery extends the same pattern across the lifecycle.

## How to try them in this Codespace

- **Agents:** open Copilot Chat → the **agent picker** at the top of the panel
  → choose an agent (e.g. `reproducibility-auditor`). If it is missing, run
  **Developer: Reload Window**.
- **Commands:** type `/` in chat and pick a prompt (e.g.
  `/eda-summary`), or pass the input: `/write-tests target=sci_units.converters`.
- **Skills:** ask in plain language ("log this run to my lab notebook from
  `runs/...`") and the `experiment-log` skill loads on demand.
- **Instructions:** open a notebook or a file under `tests/` and they apply
  automatically — no picker, no slash command.

Good targets are already in the repo:
[`blocks/01-landscape/demo/starter/`](../blocks/01-landscape/demo/starter/)
(`sci_units`, small) and
[`blocks/03-research-loop/demo/starter/`](../blocks/03-research-loop/demo/starter/)
(the climate model, realistically messy). Or point them at your own code.

## Design principles (steal these for your own)

- **Narrow beats broad.** One job, stated in numbered steps.
- **Constrain the tools.** A reviewer with no `edit/editFiles` _cannot_ change your
  code. The tool list is a real safety lever, not decoration.
- **Say what NOT to do.** The "do NOT" section prevents the most common
  failure modes (scope creep, silent edits, runaway loops).
- **Show the output format.** A concrete example beats an abstract description.
- **No emojis** in workshop material unless explicitly requested.
