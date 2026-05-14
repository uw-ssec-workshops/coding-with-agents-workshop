# Block 4: Build Your Own Skill (Capstone)

**Duration:** ~30 minutes (the remaining workshop time)
**Tool focus:** **GitHub Copilot custom chat modes** (`.github/chatmodes/*.chatmode.md`).
**Spine:** *Skills are simple, six fields in a markdown file. Now write one.*

The capstone. Each attendee builds a working chat mode of their own and
runs it against the climate model from Block 3 (or their own code). The
two worked examples in [`.github/chatmodes/`](../../.github/chatmodes/)
plus the [`exercise/`](exercise/) folder are the scaffolding.

## Learning goals

By the end of this block, an attendee can:

1. Read a Copilot chat mode file and identify which line corresponds to which **anatomy concept** from Block 1 (LLM backbone, tool use, project memory, system prompt).
2. **Write** a chat mode end-to-end: pick a job, write a focused system prompt, choose a narrow tool list, save it to `.github/chatmodes/`, and invoke it.
3. **Iterate** on a chat mode that almost works: tighten the prompt, add explicit constraints, narrow or broaden the tool list.
4. Map the same chat mode pattern to **other tools** (Copilot prompt files for one-shots; Claude Code skills if they prefer the Block 3 setup; MCP servers if they want to add new tools).

## What's in this folder

```
04-build-a-skill/
  README.md            # this file
  slides.md            # Marp slides (~6 slides, ~10 min talking)
  slides.css           # minimal slide theme tweaks
  instructor-notes.md  # facilitation guide, live-build script, what to circulate for
  resources.md         # Copilot chatmode docs, prompt files, MCP, Claude Code skills
  exercise/
    README.md                       # participant-facing step-by-step
    my-mode.chatmode.md.template    # SKELETON to copy + fill in
    ideas.md                        # ~20 starter skill ideas
```

The two **worked example chat modes** live in
[`.github/chatmodes/`](../../.github/chatmodes/) so they're auto-loaded
by Copilot in the Codespace from the start of the workshop:

- [`scientific-python-reviewer.chatmode.md`](../../.github/chatmodes/scientific-python-reviewer.chatmode.md), read-only opinionated reviewer
- [`docstring-writer.chatmode.md`](../../.github/chatmodes/docstring-writer.chatmode.md), focused write-mode for adding NumPy-style docstrings

## Timing (~30 min)

| min | section |
|---|---|
| 0–3 | Workshop recap + "the simplest skill is a chat mode" |
| 3–8 | Anatomy of a chat mode + tour the two worked examples |
| 8–12 | **Live build**: instructor builds a tiny chat mode in front of the room |
| 12–25 | **Hands-on**: attendees build their own; instructors circulate |
| 25–28 | Show-and-tell: 1-2 volunteers demo their mode |
| 28–30 | Wrap-up + office hours |

The hands-on is the load-bearing part. Slides are intentionally light.

## How to run the material

### Present the slides

Marp-for-VS-Code, same as the other blocks, see [`blocks/01-landscape/README.md`](../01-landscape/README.md#view--present-the-slides).

### Run the exercise

Participants follow [`exercise/README.md`](exercise/README.md). Instructors
circulate. The exercise's troubleshooting table covers the common
"my mode doesn't appear" / "mode runs but does the wrong thing" issues.

## Prerequisites

- All of Blocks 1, 2, 3 done (or at least their setup: Codespace, Copilot signed in, LiteLLM proxy credentials).
- Both worked-example chat modes appear in the Copilot mode picker. (If not: **Developer: Reload Window**.)

## Office hours (next day)

VISS members will be available the day after the workshop to help
attendees:

- Try their chat mode against their own data or workflows.
- Promote a chat mode to a Copilot **prompt file** or an **MCP server** if they want a different shape.
- Port their chat mode to a **Claude Code skill** if they prefer that setup.
- Talk through agentic research workflows in general.

Bring whatever code or data you wanted to try during the workshop but
didn't get to.
