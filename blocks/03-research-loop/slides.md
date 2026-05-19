---
marp: true
theme: default
paginate: true
size: 16:9
title: "Block 3 - Agent-Driven Research Software Engineering"
description: "Coding with AI Agents - 2026 Interdisciplinary Science Summit"
style: |
  @import "slides.css";
---

<!-- _class: lead -->

# Agent-Driven Research Software Engineering

## Block 3: Workflows, Failure Modes, Use Cases

*From "the model can call tools" to "I trust this on my actual research code."*

<!--
Speaker notes:
- 30 seconds. Hand-off from Block 2.
- Set the stakes: the previous two blocks were about *how it works*. This block is about *how to use it on real research code without it blowing up in your face*.
-->

---

## Where we left off

Block 2: most agent failures are **prompt problems**, not training problems.

So how do you systematically write good prompts for hard, multi-step research tasks?

> You don't write better one-shot prompts. You build **workflows**.
>
> A workflow is a templated, named, reusable prompt that lives next
> to your code and produces an auditable artifact. Sound familiar?
> It's exactly the same trick as `AGENTS.md` from Block 1, applied
> *per phase of your work*, not just per project.

**Workflows ARE the prompt.**

<!--
Speaker notes:
- This is the workshop-spine continuation. Block 1 introduced project memory; Block 2 said "in the prompt > trained in"; Block 3 says structured workflows are the systematic way to do that.
- Hammer "workflows are the prompt", it's the slide-8 takeaway from Block 2 made operational.
-->

---

## The 6-phase workflow we'll demo

| Phase | Slash command | Output | Purpose |
|---|---|---|---|
| 1. Research | `/research` | `.agents/research-<slug>.md` | Understand existing code |
| 2. Plan | `/plan` | `.agents/plan-<slug>.md` | Specify what we'll build |
| 3. Iterate | `/iterate-plan` | updates plan in place | Refine without rewriting |
| 4. Experiment | `/experiment` | `.agents/experiment-<slug>.md` | Compare approaches |
| 5. Implement | `/implement` | `.agents/implement-<slug>.md` | Execute phase by phase |
| 6. Validate | `/validate` | inline report | Verify built vs planned |
| (any time) | `/handoff` | `.agents/handoff-<ts>.md` | Transfer session context |

**You don't use all six every time.** Pick the pattern:

- *Simple change:* `/research` -> `/plan` -> `/implement` -> `/validate`
- *Multiple approaches:* add `/experiment` in the middle
- *Already-known codebase:* `/plan` -> `/implement`

<!--
Speaker notes:
- Read across the table.
- Emphasize: this is the rse-plugins plugin (a Claude Code plugin built by UW SSEC). The pattern is the lesson; the plugin is one polished implementation.
- Tee up the demo: "we're about to run the simple-change pattern, live, on real research code."
-->

---

## Demo: package the climate model

The codebase: `climate_model.py` + `co2_emissions.py` (~90 lines, no package, no tests).

The goal: turn it into an installable `vscm` Python package, following Scientific Python guidelines.

We'll run **four phases** in order: `/research`, `/plan`, `/implement`, `/validate`. Watch the artifacts appear in `.agents/` as we go.

> While `/implement` runs (it's the slow one), we'll use the time to talk
> through **failure modes**, what to watch for, where they come from,
> what to do when you see them.

<!--
Speaker notes:
- Switch to VS Code's integrated terminal. We're running Claude Code as a CLI (`claude`) from the terminal, not from the graphical panel — see instructor-notes.md for why (the CLI lets us pick the working directory; the panel always inherits the workspace root).
- Working directory for the demo: blocks/03-research-loop/demo/ (the parent of starter/, so AGENTS.md is at cwd and the starter scripts sit in the starter/ subfolder).
- Confirm `.agents/` does not exist yet (rm -rf .agents/ if it's been left over from a dry run). Then launch `claude`.
- Have all four prompts copied to clipboard (see instructor-notes.md).
- For each phase: paste the prompt, narrate what's happening, point at the artifact when it appears.
-->

---

## Failure mode taxonomy

Each failure traces back to a specific post-training shortcut from Block 2.

| Failure | What it looks like | Where it comes from | Mitigation |
|---|---|---|---|
| Context exhaustion | Forgets earlier instructions, repeats work | Limited context window | `/handoff`, smaller scope per phase |
| Looping | Same tool called over and over | RL trained on short trajectories | `max_steps`, intervene, restate goal |
| Niche language hallucination | Invents Fortran / Julia / IDL APIs | Underrepresented in training data | Load docs into context, examples in `AGENTS.md` |
| Confident wrong answer | "Done!" when nothing is fixed | RLHF over-tuned for confidence | Always `/validate`; trust nothing without proof |
| Tool misuse | Edits when it should ask | RLHF made it action-biased | "Ask before edit" in system prompt |
| Scope creep | Refactors files you didn't mention | SFT taught "be helpful" too eagerly | Tight `/plan`, narrow per-phase scope |

> Most production agent disasters are 2 or 3 of these stacked.

<!--
Speaker notes:
- The "Where it comes from" column is the workshop's payoff, we said in Block 2 that knowing how the model is shaped tells you how it can fail. This is that payoff.
- Pick one row to elaborate (audience-dependent): scientific computing audiences often hit niche-language and confident-wrong-answer hardest.
-->

---

## Mitigations: the levers you have

**Process levers** (what the rse-plugins workflow gives you):

- Auditable artifacts in `.agents/`, you can read what the model planned vs what it built
- `/validate` as a quality gate, not a vibe check
- `/handoff` to compact context across long sessions

**Prompt-side levers** (what Block 2's "in the prompt" framing gives you):

- `AGENTS.md` for project-wide conventions ("we use uv, not poetry")
- Tight per-phase scope ("just refactor the loader, don't touch the model")
- Examples in the prompt for niche stacks ("here's how we like to use xarray")

**Manual levers** (always available):

- Stop the agent. Read the artifact. Push back. Re-run.
- Agents are *coworkers*, not magic. Coworkers get pushback.

<!--
Speaker notes:
- "Agents are coworkers, not magic", drop this line slowly. It's the most quotable thing in Block 3.
- The mitigations are the actionable thing. Bookmark this slide.
-->

---

## Practical use cases (a quick tour)

| Use case | Where agents shine | Where to be careful |
|---|---|---|
| **Feature implementation** | Multi-step planning + iteration | Scope creeps without tight prompts |
| **Debugging** | "Read error -> form hypothesis -> test" loop | Easy to fix symptoms, not causes |
| **Test writing** | Generates many cases fast | Tests can become tautological (testing the impl, not the spec) |
| **Documentation** | Reads code, writes docs that match | Docs drift if code changes after |
| **Code review** | Catches obvious issues, common pitfalls | Misses architectural concerns |
| **Exploratory coding** | Spike code in minutes | Spikes become "production" code without rewrites |
| **Experiment management** | Run sweeps, summarize results, draft next hypothesis | Confidently mis-reads metrics; always spot-check the numbers |

> The pattern across all seven: the **agent expands what one person can attempt**. The discipline question is which 95% of the work is fine to delegate, and which 5% must stay yours.

<!--
Speaker notes:
- 30 seconds total. Don't dwell on any one row.
- The closing one-liner is the takeaway: agents are a productivity multiplier, but the editorial judgment stays yours.
-->

---

## Two modes: research vs. engineering

The full `/research` -> `/plan` -> `/implement` -> `/validate` loop is the **durable** mode. Research work often wants the **fast** mode instead.

| | Fast (research) | Durable (engineering) |
|---|---|---|
| **When** | Notebook spikes, parameter sweeps, "does this idea work?" | Library / package code, anything that outlives the question |
| **Loop** | Chat against `AGENTS.md`; maybe `/research` | All four phases; `/validate` non-negotiable |
| **Throwaway?** | Yes, by design | No, this is your contribution |
| **Trust model** | You eyeball the output | The artifacts in `.agents/` are the audit trail |

**Same agents. Same workflows. Different dial settings.** Pick the loop length to match the half-life of the code.

> **The workflow generalizes; your `AGENTS.md` is where your research context lives.** It's the one file you'll edit most: conventions, vocabulary, data shape, "don't touch X", citations to your stats methods, what counts as a passing run. NLP labs put eval harness + metric definitions there. Bio puts file-format conventions and pipeline DAGs. Behavioral / social science puts coding schemes, IRB constraints, and analysis assumptions. Physics / climate puts the sci-Python guidelines we used in the demo.

<!--
Speaker notes:
- 60-90 seconds. This slide exists for two audiences: (a) people from non-RSE backgrounds (NLP, ML, comp ling) who want to know the loop isn't only for "build me a package", and (b) AI engineers who want fast iteration and worry the full loop is overkill.
- Read the table left-to-right. Land "pick the loop length to match the half-life of the code" slowly.
- For the cross-field paragraph: pick the audience's closest field and elaborate for 10 seconds. If mixed audience, just read it.
- Avoid claiming the workshop covers all four domains - we don't. The point is the *shape* is portable.
-->

---

## Bridge to Block 4

You just watched the rse-plugins plugin do this:

- **System prompt** for each slash command (templated text)
- **Tool schemas** for `read_file`, `write_file`, `run_bash`, etc. (same schemas as Block 1)
- **Project memory** via `AGENTS.md` (same mechanic as Block 1)
- **Output convention**: write a markdown artifact to `.agents/`

That's all a "skill" is. Five files, no magic.

> **Block 4: build your own.** We'll write one slash command from
> scratch, pick the phase that's most useful to you, or invent your
> own, and run it against the climate model (or your own code).

<!--
Speaker notes:
- Hard hand-off. Don't linger.
- The "five files, no magic" framing is what makes Block 4 feel approachable.
- Last sentence: "Block 4: build your own." Stop talking.
-->
