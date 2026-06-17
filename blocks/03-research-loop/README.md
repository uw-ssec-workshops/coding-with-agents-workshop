# Block 3: Agent-Driven Research Software Engineering

**Duration:** ~30 minutes
**Tool focus:** **GitHub Copilot Chat** (agent mode) driven by workshop **skills** that live in [`.github/skills/`](../../.github/skills/): `profile-dataset`, `plan-analysis`, `explore-data`, `statistical-tests`, `draft-report`, `validate-analysis`, and `handoff`. 

## Learning goals

By the end of this block, an attendee can:

1. Recognize the **phases** of the workshop workflow, see that each is just a `.github/skills/<name>/SKILL.md` file, and pick the right subset for a given task.
2. Name the common **agent failure modes** (context exhaustion, looping, niche-language hallucination, confidently wrong answers, tool misuse, and scope creep).
3. Apply the corresponding **mitigations** (tighter scope per turn, auditable artifacts, fresh chats to compact context, `validate-analysis` as a quality gate, AGENTS.md as durable project memory, manual intervention).
4. Stay in control of an agent that edits files: **review the diff (not the chat), commit per phase, and roll back cleanly with git**, and recognize **prompt injection** (the agent acting on instructions hidden in untrusted code/data/web) and the tool-scoping that mitigates it.
5. Map the workshop's **practical use cases** (statistical analysis, debugging, EDA, scientific writing, code review, test writing, experiment management) to where agents help most and where they hurt.

## What's in this folder

```
03-research-loop/
  README.md            # this file
  slides.md            # Marp slides 
  instructor-notes.md  # speaker notes
  resources.md         # the skills, stats-for-HCI references, failure-mode reading
  demo/
    AGENTS.md          # project memory: the text-entry study design + analysis conventions
    starter/           # the dataset (and its generator)
      data.csv         # 90 rows: 30 participants x 3 interfaces (within-subjects)
      make_data.py     # seeded generator; re-running it reproduces data.csv
    expected-artifacts/  # pre-generated docs/ outputs (+ analysis.py, figures/) as fallback
```

## How to run the material

### Run the demo

This is a **live, instructor-led demo**. 

1. Open **Copilot Chat** and switch the picker to **Agent** mode.
2. Wipe any leftover artifacts from prior runs (from the repo root): `rm -rf blocks/03-research-loop/demo/docs/`.
3. Walk the seven skills from [`instructor-notes.md`](instructor-notes.md), one at a time. They are defined in [`.github/skills/`](../../.github/skills/); invoke one by name (*"use the `plan-analysis` skill…"*) or describe the task and let the agent pick. The **first** prompt names the full demo paths (e.g. `blocks/03-research-loop/demo/starter/data.csv`) and tells the agent to read `blocks/03-research-loop/demo/AGENTS.md` first.
4. When you're done, **commit the trail**: `git add blocks/03-research-loop/demo/docs/ && git commit`. That's the auditability lesson. These artifacts are a dated record of what was analyzed and why.

If anything goes wrong on the day, the [`expected-artifacts/`](demo/expected-artifacts/) folder ships pre-generated outputs (including a runnable `analysis.py` and the EDA figures) to walk through instead.


## Bridge to Block 4

Block 4 is the capstone where attendees write their first custom agent / skill and run it against their own data or code.
