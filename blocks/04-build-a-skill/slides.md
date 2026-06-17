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


---

## The whole workshop, in one slide

| Block | Takeaway |
|---|---|
| 1. Landscape | All coding agents have the same anatomy: LLM + tools + memory + loop. |
| 2. How it works | Triage failures: **prompt problem** vs **training problem**. The prompt is your lever. |
| 3. Workflows | **Workflows are reusable skills** that are structured and auditable. The agent picks one or you invoke it. |
| 4. **Now** | Write one. |

--
> The next 25 minutes are practice.

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
| **Example here** | `eda-summary`, `scaffold-package` | the 6 research-loop skills | `docstring-writer`, `research-data-scientist` |

> They **compose**: `research-data-scientist` (an *agent*) drives the seven *skills* in
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

## Wrap-up

You now have:

- A mental model that survives the next product release from a frontier AI lab
- A concrete agentic workflow you've seen run on real data 
- A custom agent you wrote yourself that **lives in your Codespace** 


> Thank you for spending the afternoon with us.
