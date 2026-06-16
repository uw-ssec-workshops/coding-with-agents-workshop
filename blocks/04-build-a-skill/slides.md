---
marp: true
theme: workshop
paginate: true
title: "Block 4 - Build Your Own Skill"
description: "Coding with AI Agents"
---

<!-- _class: lead -->

# Build Your Own Skill

## Block 4: Capstone

*Five fields in a markdown file. No magic. Let's go.*

---

## The whole workshop, in one slide

| Block | Takeaway |
|---|---|
| 1. Landscape | All coding agents have the same anatomy: LLM + tools + memory + loop. |
| 2. How it works | Triage failures: **prompt problem** vs **training problem** — the prompt is your lever. |
| 3. Workflows | **Workflows are reusable skills** — structured, auditable, the agent picks one or you invoke it. |
| 4. **Now** | Write one. |

> The pieces are simple. The **practice** is what makes it useful.
> The next 25 minutes are practice.

---

## Anatomy of a Copilot custom agent

```markdown
---
name: scientific-python-reviewer
description: 'Review code against Scientific Python guidelines (read-only).'
tools: ['read', 'search/codebase', 'search']
---

# Scientific Python Reviewer

You are a senior research software engineer reviewing scientific Python code...

## What you do

1. Read the code thoroughly.
2. Identify gaps against the recommendations.
3. Output a markdown review with file:line references.

## What you do NOT do

- You do not edit files.
- You do not invent issues.
```

> Top: **frontmatter**, the name + what shows in the picker + which tools it can use.
> Below: **system prompt**, persona, steps, constraints.
> That's it. A handful of fields.

---

## Two worked examples in `.github/agents/`

| Agent | What it does | Tools | Why it's a good template |
|---|---|---|---|
| `scientific-python-reviewer` | Reviews against Scientific Python guidelines | read-only | Persona + standard reference + tight scope |
| `docstring-writer` | Adds NumPy-style docstrings | read + write | Scoped editing + output style example |

Open them. Read them. **They are the reference for what you'll write.**

> The exercise's `ideas.md` has 30+ more agent ideas if you don't have one
> in mind, by category (review, generation, refactoring, HCI / experiment
> analysis, general research, onboarding). The rest of `.github/` is a fuller gallery.

---

## Prompts vs. skills vs. agents (all in `.github/`)

Three primitives, same idea (a markdown file = instructions + tools), different shapes:

| | **Prompt file** | **Skill** | **Custom agent** |
|---|---|---|---|
| **Folder** | `.github/prompts/*.prompt.md` | `.github/skills/<name>/SKILL.md` | `.github/agents/*.agent.md` |
| **Invoked** | You type `/name` | Agent auto-picks (or `/name`) | You select it in the agent picker |
| **Input** | Structured `${input:var}` fields | Natural-language context (+ `argument-hint`) | The whole conversation |
| **Best for** | One-shot repeatable task | A multi-step capability (can bundle scripts) | A persistent persona with a fixed tool list |
| **Lifespan** | One turn | One task | The whole chat |
| **Example here** | `eda-summary`, `scaffold-package` | the 7 research-loop skills | `docstring-writer`, `research-analyst` |

> They **compose**: `research-analyst` (an *agent*) drives the seven *skills* in
> order. Pick the smallest primitive that does the job — most of the time that's a
> prompt file or a skill, not a whole agent.

> Prompts don't only take static `${input}` fields — they can gather context
> *interactively* by calling the `vscode/askQuestions` tool ("which file should I
> test?") instead of guessing.

---

## Your turn (~15 min)

1. **Copy** the template:
    ```bash
    cp blocks/04-build-a-skill/exercise/my-agent.agent.md.template \
       .github/agents/my-agent.agent.md
    ```
2. **Pick** a target, the `sci_units` package, the Block 3 text-entry dataset, or your own code.
3. **Pick** a job, see `exercise/ideas.md`, or invent your own.
4. **Edit** the file: name, description, tools, system prompt, constraints.
5. **Reload** Copilot Chat (or wait, agents auto-detect).
6. **Run** your agent and **iterate**.

Full instructions: [`blocks/04-build-a-skill/exercise/README.md`](../../blocks/04-build-a-skill/exercise/README.md)

> Instructors circulating. **Get something narrow working** before
> trying to make it broader. Ship a boring agent that runs over an
> ambitious agent that doesn't.

---

## Optional: want to write *more* skills?

Once your first agent works, the natural next step is a **multi-phase skill
workflow** — several skills that hand off through artifacts, like the Block 3
research loop you watched.

> **Try it (take-home / office hours):** write **one** new skill of your own
> that chains onto the Block 3 loop —
> e.g. a `power-analysis` skill that runs *before* `plan-analysis`, or a
> `peer-review` skill that critiques a `draft-report` artifact. Same shape:
> `name` + `description` + `tools` + steps + an artifact in `docs/`.

---

## Wrap-up

You now have:

- A mental model that survives the next product release (Blocks 1, 2)
- A concrete workflow you've seen run on real code (Block 3)
- A custom agent you wrote yourself that **lives in your Codespace** (Block 4)

This Codespace stays. The repo stays. 

> Thank you for spending the afternoon with us.
