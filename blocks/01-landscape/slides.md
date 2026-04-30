---
marp: true
theme: default
paginate: true
size: 16:9
title: "Block 1 - The AI Coding Agent Landscape"
description: "Coding with AI Agents - 2026 Interdisciplinary Science Summit"
style: |
  @import "slides.css";
---

<!-- _class: lead -->

# Coding with AI Agents

## Block 1: The Landscape

*2026 Interdisciplinary Science Summit*
*Schmidt Sciences x UW SSEC*

<!--
Speaker notes:
- 30-second intro. Welcome them. State the workshop's spine: "all coding agents work the same way under the hood."
- Tell them this block is the map; Block 2 is the engine; Block 3 is the workflow; Block 4 is the build.
-->

---

## What changed

- 18 months ago: **autocomplete**. The IDE finished your line.
- Today: **agents**. They read the codebase, plan, edit files, run tests, debug, iterate.
- Same models, mostly. *What changed is the loop wrapped around them.*
- This workshop is about that loop.

<!--
Speaker notes:
- Don't oversell. Most attendees have already used some of this.
- The point is: the *category* changed, not just the quality.
-->

---

## The landscape (2026)

| Tool | Form | Models | Notable trait |
|---|---|---|---|
| **GitHub Copilot** | IDE (VSCode, JetBrains) | OpenAI, Anthropic, Google | Built into the editor most scientists already use |
| **Claude Code** | CLI | Anthropic | First-party Anthropic, Bedrock-friendly |
| **Cursor** | Forked IDE | Multi-provider | Aggressive UX experiments |
| **OpenCode** | CLI, OSS | Bring your own | Self-hostable |
| **Aider** | CLI, OSS | Bring your own | Pioneered git-aware workflows |
| **Cline** | VSCode extension | Bring your own | OSS competitor to Copilot |

<!--
Speaker notes:
- 30 seconds per row, max. Don't dwell.
- Emphasize: this list will be different in 6 months. The categories won't.
-->

---

## Four axes that actually matter

When you compare tools, ignore the marketing. Look at:

1. **Cost**: flat subscription vs metered API vs self-hosted compute.
2. **Capability**: single-file edits vs multi-file refactors vs long autonomous runs.
3. **Integration**: IDE-native vs CLI vs cloud agent.
4. **Model hosting**: vendor API vs your cloud account vs your hardware.

> The right tool depends on **your constraints**, not on benchmarks.

<!--
Speaker notes:
- For science contexts, model hosting matters more than for industry: data residency, IRB, sometimes air-gapped.
- Capability claims are noisy; trust your own evaluation on your code.
-->

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
            ┌──────────────────────────────┐
            │   Agent loop  (decide & act) │
            └─┬────────────┬─────────────┬─┘
              ▼            ▼             ▼
           Tools        Memory          MCP
        (read/edit/   (AGENTS.md /     servers
         shell/...)   instructions)   (extend tools)
                            ▲
                            │
                       Skills / prompts
                       (templated behaviors)
```

<!--
Speaker notes:
- This is THE diagram. Reference it for the rest of the workshop.
- Each label maps to a concrete file, function, or API call we'll see in the demo.
-->

---

## Why they all feel the same

Same six pieces. Different wrappers.

| Concept | GitHub Copilot | Claude Code | Cursor |
|---|---|---|---|
| LLM backbone | configurable | Anthropic | configurable |
| Tool use | built-in | built-in | built-in |
| Project memory | `.github/copilot-instructions.md` | `AGENTS.md` / `CLAUDE.md` | `.cursor/rules` |
| MCP servers | yes | yes | yes |
| Skills / prompts | prompt files, chatmodes | skills, slash commands | rules, modes |
| Agent loop | "agent mode" | the whole CLI | "Cmd+I" |

> If you understand the **pieces**, switching tools is a config exercise.

<!--
Speaker notes:
- This is the workshop's spine. Say it explicitly.
- Pay-off: when a new tool launches next quarter, you'll know what to look for.
-->

---

## Picking a tool

A short decision flow. Not a leaderboard.

1. **Where do you write code?** IDE -> Copilot or Cursor. Terminal-first -> Claude Code or Aider.
2. **Who pays?** Lab budget on a vendor API? Cloud credits? Personal?
3. **Where can the model see your data?** Vendor cloud? Your AWS account? On-prem?
4. **Do you need self-hosting?** Then OpenCode + a hosted or local model.

For today: **GitHub Copilot in VSCode + Codespaces, with Claude (via the workshop's LLM proxy server) as the model backend**. It's the lowest-friction option for a workshop, and it's representative.

<!--
Speaker notes:
- Acknowledge: Cursor users in the room, your skills transfer 1:1.
- The choice is "what runs cleanly in 90 minutes for 30 people on borrowed laptops."
-->

---

## Setup for today

Three things, all done for you:

1. **GitHub Codespace**: preconfigured Python 3.12 + JupyterLab + Copilot.
2. **GitHub Copilot**: signed in via your GitHub identity, agent mode enabled.
3. **Claude via the workshop's LLM proxy server**: exposed as `LITELLM_API_KEY` and `LITELLM_API_BASE`. Copilot and the notebook talk to the same proxy.

If `postCreate.sh` printed a green "Done", you are ready. If not, see [`docs/setup.md`](../../docs/setup.md) and ping an instructor.

<!--
Speaker notes:
- Pause here. Walk the room. Help anyone whose Codespace didn't build.
- Be reassuring: failures here are setup failures, not your fault.
-->

---

## Demo: same task, two ways

**The scenario**: a tiny `sci_units` Python package with a failing pytest.

We are going to fix it twice.

1. **First**, with Copilot in agent mode. ~2 minutes. Polished UX. Watch what it does.
2. **Then**, with a ~50-line Python notebook that talks to Claude through the workshop's LLM proxy, the same proxy Copilot is using. Watch the **same loop** with no UX polish at all.

The point: it's the same loop.

<!--
Speaker notes:
- Reset starter/src/sci_units/converters.py before this slide!
- Have the prompt copied to clipboard.
-->

---

## Bridge to Block 2

You just watched a model **decide** to call `run_bash`, then **decide** to call `read_file`, then **decide** to write a fix.

Nothing in the API said "you're allowed to use these." We just *gave* it a tool list. It chose to use them, in a sensible order, with sensible arguments.

That behavior didn't fall out of next-token prediction on web text.

It was **trained in**. That's Block 2.

<!--
Speaker notes:
- Hard hand-off. Don't linger. Block 2 is where the "why does this work" answer lives.
-->
