# Block 3: Agent-Driven Research Software Engineering

**Duration:** ~30 minutes
**Tool focus:** **Claude Code VS Code extension** with the [`rse-plugins`](https://github.com/uw-ssec/rse-plugins) plugin (a 6-phase research-plan-implement workflow built by UW SSEC). Same LiteLLM proxy as Blocks 1-2; different IDE panel.
**Spine:** *Workflows ARE the prompt.* Structured slash commands (`/research`, `/plan`, `/implement`, `/validate`) are templated, named, reusable prompts that produce auditable artifacts.

## Learning goals

By the end of this block, an attendee can:

1. Articulate the **research-plan-implement-validate** discipline and explain why "research before plan, plan before code, validate before ship" beats unstructured prompting on real research codebases.
2. Recognize the **6 phases** of the `rse-plugins` workflow (`/research`, `/plan`, `/iterate-plan`, `/experiment`, `/implement`, `/validate`, `/handoff`) and pick the right subset for a given task.
3. Name the common **agent failure modes** (context exhaustion, looping, niche-language hallucination, confidently-wrong answers, tool misuse, scope creep) and trace each one back to a specific post-training shortcut from Block 2.
4. Apply the corresponding **mitigations** (tighter scope per turn, auditable artifacts, `/handoff` to compact context, `/validate` as a quality gate, AGENTS.md as durable project memory, manual intervention).
5. Map the workshop's **practical use cases** (feature implementation, debugging, test writing, documentation, code review, exploratory coding, experiment management) to where agents help most and where they hurt.
6. Pick the right **loop length** for the task: the full `/research` -> `/plan` -> `/implement` -> `/validate` cycle for durable code vs. fast chat-against-`AGENTS.md` iteration for research spikes.

## What's in this folder

```
03-research-loop/
  README.md            # this file
  slides.md            # Marp slides (~9 slides, ~22 min talking + demo)
  slides.css           # minimal slide theme tweaks
  instructor-notes.md  # per-slide notes, demo script with copy-paste prompts, fallback plan
  resources.md         # rse-plugins, Scientific Python guidelines, failure-mode reading
  demo/
    AGENTS.md          # project memory: VSCM goals + Scientific Python conventions
    starter/           # the climate model code (intentionally messy)
      climate_model.py
      co2_emissions.py
      SSP_CO2emissions.csv
    expected-artifacts/  # pre-generated .agents/ outputs as live-demo fallback
```

## Timing (30 min)

| min | section |
|---|---|
| 0–3 | Recap + "workflows are the prompt" |
| 3–6 | The 6-phase rse-plugins workflow (overview slide) |
| 6–10 | **Demo: `/research`** |
| 10–14 | **Demo: `/plan`** |
| 14–20 | **Demo: `/implement`** + narrate failure modes while it runs |
| 20–22 | **Demo: `/validate`** |
| 22–26 | Failure mode taxonomy + mitigations |
| 26–27 | Practical use cases tour |
| 27–29 | Research vs. engineering mode + cross-field framing |
| 29–30 | Bridge to Block 4 |

The `/implement` step is timed as the longest because that's when we narrate the failure modes in parallel, productive use of the agent's "thinking time."

## How to run the material

### Present the slides

Same Marp-for-VS-Code workflow as Blocks 1 and 2, see [`blocks/01-landscape/README.md`](../01-landscape/README.md#view--present-the-slides). Open `slides.md`, click the preview icon.

### Run the demo

This is a **live, instructor-led demo**. Participants don't need to type anything during the block, but the same Codespace they have open will work, so they can re-run on their own afterward.

1. Open VS Code with the workspace folder set to `blocks/03-research-loop/demo/starter/`.
2. Open the Claude Code panel (extension auto-installed in the Codespace).
3. Wipe any leftover `.agents/` from prior runs: `rm -rf .agents/`.
4. Run the four prompts from [`instructor-notes.md`](instructor-notes.md), `/research`, `/plan`, `/implement`, `/validate`, one at a time.

If anything goes wrong on the day, the [`expected-artifacts/`](demo/expected-artifacts/) folder ships pre-generated outputs to walk through instead.

## Prerequisites

- Codespace running (see top-level [`README.md`](../../README.md) and [`docs/setup.md`](../../docs/setup.md)).
- `LITELLM_API_KEY` and `LITELLM_BASE_URL` Codespace secrets set (the devcontainer also exposes them as `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL` so Claude Code uses the same proxy).
- Claude Code VS Code extension signed in (auto-prompted on first launch).
- `ai-research-workflows` plugin (from the [`rse-plugins`](https://github.com/uw-ssec/rse-plugins) marketplace) installed and visible in `claude plugin list`. Auto-installed by `postCreate.sh` via two commands — `claude plugin marketplace add ...` followed by `claude plugin install ai-research-workflows@rse-plugins`. Falls back to printing both manual commands if the Claude Code CLI isn't on PATH yet. Requires Claude Code `>= 2.1.61`.

## Bridge to Block 4

This block ends with: *"You just watched the rse-plugins plugin do all this. Now you'll build a small skill of your own. The pieces are the same."* Block 4 is the capstone where attendees write their first custom agent / prompt-file command / skill and run it against their own code.
