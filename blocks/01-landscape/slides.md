---
marp: true
theme: workshop
paginate: true
title: "Block 1 - The AI Coding Agent Landscape"
description: "Coding with AI Agents"
---

<!-- _class: lead -->

# Coding with AI Agents

## Block 1: The Landscape

*Eighteen months ago this was autocomplete. Today it's agents.*

---

## What changed

- 18 months ago: **autocomplete**. The IDE finished your line.
- Today: **agents**. They read the codebase, plan, edit files, run tests, debug, iterate.
- Same models, mostly. 
- *What changed is the loop wrapped around them. What the industry calls it the agent "harness."*
- This workshop primarily builds intuition about that loop.

---

## The landscape (2026)

| Tool | Form | Models | Notable trait |
|---|---|---|---|
| **GitHub Copilot** | IDE (VSCode, JetBrains) | OpenAI, Anthropic, Google | Built into the editor most scientists already use |
| **Claude Code** | CLI | Anthropic | First-party Anthropic, Bedrock-friendly |
| **Cursor** | Forked IDE | Multi-provider | Aggressive UX experiments |
| **OpenCode** | CLI, OSS | Bring your own | Self-hostable |
| **Hermes** | CLI | Bring your own | Lightweight, scriptable agent |
| **Pi Coding** | CLI / IDE | Multi-provider | Coding-focused agent workflows |

---

## Axes that actually matter

When you compare tools, ignore the marketing. Look at:

1. **Cost**: flat subscription vs metered API vs self-hosted compute.
2. **Capability**: single-file edits vs multi-file refactors vs long autonomous runs.
3. **Integration**: IDE-native vs CLI vs cloud agent.
4. **Model hosting**: vendor API vs your cloud account vs your hardware.
5. **Privacy**: proprietary code, unpublished research, and other data you can't send to a vendor.

There are other axes too, depending on your context.

> The right tool depends on **your constraints**, not on benchmarks.

---

## Anatomy of a coding agent

```
                  ┌────────────────────────┐
                  │     User prompt        │
                  └───────────┬────────────┘
                              ▼
                ┌─────────────────────────┐
                │     LLM backbone        │  <-- post-trained for tool use
                └───────────┬─────────────┘
                            ▼
            ┌────────────────────────────────────────────┐
            │          Agent loop  (decide & act)        │
            └─┬──────────────┬─────────────────────────┬─┘
              ▼              ▼                         ▼
           Tools          Memory                      MCP
        (read/edit/     (AGENTS.md /                servers
         shell/...)     copilot-instructions.md)  (extend tools)
                            ▲
                            │
                       Skills / prompts
                       (templated behaviors)
```

---

## Why they all feel the same

Same six pieces. Different wrappers / harness.

| Concept | GitHub Copilot | Claude Code | Cursor |
|---|---|---|---|
| LLM backbone | configurable | Anthropic | configurable |
| Tool use | built-in | built-in | built-in |
| Project memory | `.github/copilot-instructions.md` | `AGENTS.md` / `CLAUDE.md` | `.cursor/rules` |
| MCP servers | yes | yes | yes |
| Skills / prompts | prompt files, agents, skills | skills, slash commands | rules, modes |
| Agent loop | "agent mode" | the whole CLI | "Cmd+I" |

--
> If you understand the **pieces**, switching tools is a config exercise.

---

## Before you paste: where does your data go?

When you use an agent, **your code, data, and prompts leave your machine** and go to whoever hosts the model.

| Ask first | Why it matters in research |
|---|---|
| **Who hosts the model?** | Vendor cloud, your institution's cloud account, or on-prem each have different data-handling terms. |
| **Is the data governed?** | Human subjects, PII, IRB-restricted, or HIPAA data may *not* be allowed to leave your environment. |
| **Is it licensed / proprietary?** | NDA'd collaborator data, pre-publication results, or restrictively licensed code. |
| **Is it logged or trained on?** | Check whether the provider retains prompts or trains on them. Enterprise/proxy tiers usually do not but consumer tiers often do. |

--
> **The workshop's setup is deliberate:** the LLM proxy keeps requests inside a controlled gateway rather than hitting a consumer endpoint. For your own work, match the **model hosting** to the **sensitivity of the data**, and when in doubt, do not simply send it to the model as context. A redacted snippet or a synthetic sample is often enough for the agent to help.

---

## Demo: same task, two ways

**The scenario**: a tiny `sci_units` Python package for temperature unit conversions with failing tests (`uv run pytest -v`).

We are going to fix it twice.

1. **First**, with Copilot in agent mode. ~2 minutes. Polished UX. Watch what it does.
  _Prompt_: `There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change.`
2. **Then**, with a ~50-line Python notebook that talks to a model through the workshop's LLM proxy, the same proxy Copilot is using. Watch the **same loop** with no UX polish at all.
  _Remember to select kernel as_: `Python Environments`.


--
> The point: it's the same loop.

---

## Bridge to Block 2

You just watched a model **decide** to call `run_bash`, then **decide** to call `read_file`, then **decide** to write a fix.

Nothing in the API said "you're allowed to use these." We just *gave* it a tool list. It chose to use them, in a sensible order, with sensible arguments.

That behavior didn't fall out of next-token prediction on web text.

It was **trained in**. That's Block 2.
