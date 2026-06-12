# Block 3: Agent-Driven Research Software Engineering

**Duration:** ~30 minutes
**Tool focus:** **GitHub Copilot Chat** (agent mode) driven by workshop **skills** that live in [`.github/skills/`](../../.github/skills/): `profile-dataset`, `plan-analysis`, `explore-data`, `statistical-tests`, `draft-report`, `validate-analysis`, and `handoff`. They ship in-repo — no marketplace plugin to install. The agent can **auto-select** a skill from its `description`, or you can invoke one by name. Same Copilot Chat and same LiteLLM gateway as the rest of the workshop.
**Spine:** *Workflows are reusable skills.* Each phase of the research lifecycle is a named, reusable, auditable instruction the agent can pick for you — or you can invoke directly — and each produces a markdown artifact in `docs/`.

## Learning goals

By the end of this block, an attendee can:

1. Articulate the **profile-plan-explore-test-draft-validate** discipline and explain why "understand the data before planning, plan the test before running it, validate before you trust it" beats unstructured prompting on real research analysis.
2. Recognize the **phases** of the workshop workflow, see that each is just a `.github/skills/<name>/SKILL.md` file, and pick the right subset for a given task — invoking a skill by name *or* letting the agent select it from a generic ask.
3. Name the common **agent failure modes** (context exhaustion, looping, niche-language hallucination, confidently-wrong answers, tool misuse, scope creep) and trace each one back to a specific post-training shortcut from Block 2.
4. Apply the corresponding **mitigations** (tighter scope per turn, auditable artifacts, fresh chats to compact context, `validate-analysis` as a quality gate, AGENTS.md as durable project memory, manual intervention).
5. Stay in control of an agent that edits files: **review the diff (not the chat), commit per phase, and roll back cleanly with git**, and recognize **prompt injection** (the agent acting on instructions hidden in untrusted code/data/web) and the tool-scoping that mitigates it.
6. Map the workshop's **practical use cases** (statistical analysis, debugging, EDA, scientific writing, code review, test writing, experiment management) to where agents help most and where they hurt.
7. Pick the right **loop length** for the task: the full `profile` → `plan` → `test` → `validate` cycle for analyses that go in a paper vs. fast chat-against-`AGENTS.md` iteration for exploratory spikes.

## What's in this folder

```
03-research-loop/
  README.md            # this file
  slides.md            # Marp slides (~11 slides, ~22 min talking + demo)
                       # (theme: shared blocks/_shared/slides.css)
  instructor-notes.md  # per-slide notes, demo script with copy-paste prompts, fallback plan
  resources.md         # the skills, stats-for-HCI references, failure-mode reading
  demo/
    AGENTS.md          # project memory: the text-entry study design + analysis conventions
    starter/           # the dataset (and its generator)
      data.csv         # 90 rows: 30 participants x 3 interfaces (within-subjects)
      make_data.py     # seeded generator; re-running it reproduces data.csv
    expected-artifacts/  # pre-generated docs/ outputs (+ analysis.py, figures/) as fallback
```

## Timing (30 min)

| min | section |
|---|---|
| 0–3 | Recap + "workflows are reusable skills" |
| 3–6 | The research loop as skills (overview + invoke-or-auto-select slide) |
| 6–10 | **Demo: `profile-dataset` + `plan-analysis`** |
| 10–14 | **Demo: `explore-data`** (the assumption-check trap) |
| 14–20 | **Demo: `statistical-tests` + `draft-report`** + narrate failure modes while they run |
| 20–22 | **Demo: `validate-analysis`** |
| 22–26 | Failure mode taxonomy + mitigations (+ optional git-hygiene / prompt-injection slides) |
| 26–27 | Practical use cases tour |
| 27–29 | Research vs. publication mode + cross-field framing |
| 29–30 | Bridge to Block 4 |

The `statistical-tests` + `draft-report` steps are timed as the longest because that's when we narrate the failure modes in parallel — productive use of the agent's "thinking time."

## How to run the material

### Present the slides

Same Marp-for-VS-Code workflow as Blocks 1 and 2, see [`blocks/01-landscape/README.md`](../01-landscape/README.md#view--present-the-slides). Open `slides.md`, click the preview icon.

### Run the demo

This is a **live, instructor-led demo**. Participants don't need to type anything during the block, but the same Codespace they have open will work, so they can re-run on their own afterward.

1. Open the Codespace **at the repo root** (the default — no need to reopen a subfolder).
2. Open **Copilot Chat** and switch the picker to **Agent** mode.
3. Wipe any leftover artifacts from prior runs (from the repo root): `rm -rf blocks/03-research-loop/demo/docs/`.
4. Walk the seven skills from [`instructor-notes.md`](instructor-notes.md), one at a time. They are defined in [`.github/skills/`](../../.github/skills/); invoke one by name (*"use the `plan-analysis` skill…"*) or describe the task and let the agent pick. The **first** prompt names the full demo paths (e.g. `blocks/03-research-loop/demo/starter/data.csv`) and tells the agent to read `blocks/03-research-loop/demo/AGENTS.md` first.
5. When you're done, **commit the trail**: `git add blocks/03-research-loop/demo/docs/ && git commit`. That's the auditability lesson — these artifacts are a dated record of what was analyzed and why.

**Where do the artifacts land?** You keep the repo open at its root, so the skills' default ("write to `docs/` at the workspace root") would land in the repo's *real* top-level `docs/`. To avoid that, the demo's [`AGENTS.md`](demo/AGENTS.md) **directs the artifacts** to `blocks/03-research-loop/demo/docs/` — and the skills honor an `AGENTS.md` artifacts-location override. So the agent reads and writes there, the top-level `docs/` stays clean, and you've shown a real lesson: **`AGENTS.md` controls where artifacts go.** In your own project (opened at its root, with no override) they land in your `docs/`. The artifacts are committable on purpose (not git-ignored).

If anything goes wrong on the day, the [`expected-artifacts/`](demo/expected-artifacts/) folder ships pre-generated outputs (including a runnable `analysis.py` and the EDA figures) to walk through instead.

## Prerequisites

- Codespace running (see top-level [`README.md`](../../README.md)).
- `LITELLM_API_KEY` and `LITELLM_BASE_URL` Codespace secrets set (Copilot Chat reads them via the OAI-compatible extension).
- The workflow skills present in [`.github/skills/`](../../.github/skills/) — they ship with the repo. If the agent doesn't seem to see them, run **Developer: Reload Window**.
- `pandas`, `scipy`, and `statsmodels` are in the workshop environment (the analysis needs them; they're declared in the root `pyproject.toml`).
- Copilot Chat in **Agent** mode with one of the workshop models selected (Claude Sonnet 4.6 / Haiku 4.5).

## Bridge to Block 4

This block ends with: *"You just watched seven skills do all this. Now you'll build a small one of your own. The pieces are the same."* Block 4 is the capstone where attendees write their first custom agent / skill and run it against their own data.
