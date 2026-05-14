---
marp: true
theme: default
paginate: true
size: 16:9
title: 'Block 4 - Build Your Own Skill'
description: 'Coding with AI Agents - 2026 Interdisciplinary Science Summit'
style: |
    @import "slides.css";
---

<!-- _class: lead -->

# Build Your Own Skill

## Block 4: Capstone

_Five fields in a markdown file. No magic. Let's go._

<!--
Speaker notes:
- 30 seconds. Hand-off from Block 3.
- The mood: this is the part we've been waiting for. Light on talk, heavy on doing.
-->

---

## The whole workshop, in one slide

| Block           | Takeaway                                                              |
| --------------- | --------------------------------------------------------------------- |
| 1. Landscape    | All coding agents have the same anatomy: LLM + tools + memory + loop. |
| 2. How it works | Most agent failures are **prompt problems**, not training problems.   |
| 3. Workflows    | **Workflows ARE the prompt**, structured, reusable, auditable.        |
| 4. **Now**      | Write one.                                                            |

> The pieces are simple. The **practice** is what makes it useful.
> The next 25 minutes are practice.

<!--
Speaker notes:
- This is the spine recap. Read across the rows. Land each one.
- "The pieces are simple, the practice makes it useful", say slowly.
- Then move on. Don't dwell.
-->

---

## Anatomy of a Copilot chat mode

```markdown
---
description: 'Review code against Scientific Python guidelines (read-only).'
tools: ['readFiles', 'codebase', 'search']
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

> Top: **frontmatter**, what shows in the picker, which tools it can use.
> Below: **system prompt**, persona, steps, constraints.
> That's it. Six fields.

<!--
Speaker notes:
- Walk left-to-right, top-to-bottom: description, tools, name, persona, steps, constraints.
- Each field maps to something from Block 1's anatomy slide. Call it out: "tools = the agent loop's hands. system prompt = persona + project memory."
- Tee up the live build.
-->

---

## Two worked examples in `.github/chatmodes/`

| Mode                         | What it does                                 | Tools        | Why it's a good template                   |
| ---------------------------- | -------------------------------------------- | ------------ | ------------------------------------------ |
| `scientific-python-reviewer` | Reviews against Scientific Python guidelines | read-only    | Persona + standard reference + tight scope |
| `docstring-writer`           | Adds NumPy-style docstrings                  | read + write | Scoped editing + output style example      |

Open them. Read them. **They are the reference for what you'll write.**

> The exercise's `ideas.md` has ~20 more skill ideas if you don't have one
> in mind, by category (review, generation, refactoring, climate-specific,
> general research, onboarding).

<!--
Speaker notes:
- Open scientific-python-reviewer.chatmode.md briefly in VS Code. Point at the structure.
- Then docstring-writer. Same shape, different tool list.
- "The exercise tells you to copy patterns. Do that, the worked examples ARE the curriculum."
-->

---

## Your turn (~15 min)

1. **Copy** the template:
    ```bash
    cp blocks/04-build-a-skill/exercise/my-mode.chatmode.md.template \
       .github/chatmodes/my-mode.chatmode.md
    ```
2. **Pick** a target, the climate model, `sci_units`, or your own code.
3. **Pick** a job, see `exercise/ideas.md`, or invent your own.
4. **Edit** the file: description, tools, system prompt, constraints.
5. **Reload** Copilot Chat (or wait, modes auto-detect).
6. **Run** your mode and **iterate**.

Full instructions: [`blocks/04-build-a-skill/exercise/README.md`](../../blocks/04-build-a-skill/exercise/README.md)

> Instructors circulating. **Get something narrow working** before
> trying to make it broader. Ship a boring mode that runs over an
> ambitious mode that doesn't.

<!--
Speaker notes:
- Project this slide for the duration of the hands-on. Participants need it.
- Repeat the "narrow over broad" line whenever you circulate to someone aiming too big.
- ~3 min in: walk the room. Help anyone whose mode hasn't appeared in the picker.
- ~10 min in: announce 5 min remaining + start scouting show-and-tell volunteers.
-->

---

## Wrap-up

You now have:

- A mental model that survives the next product release (Blocks 1, 2)
- A concrete workflow you've seen run on real code (Block 3)
- A chat mode you wrote yourself that **lives in your Codespace** (Block 4)

This Codespace stays. The repo stays. **Office hours tomorrow**, bring
the code or data you actually want to use this on.

> **Pieces are simple. Practice makes it useful. Go practice.**
>
> Thank you for spending the afternoon with us.

<!--
Speaker notes:
- Office hours pointer: confirm time + location.
- Thank-yous: instructors, Schmidt Sciences, UW SSEC, and the attendees.
- Stop talking.
-->
