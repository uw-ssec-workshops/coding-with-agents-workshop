# Block 3: Instructor Notes

These are the notes you actually deliver from. The slide deck has the
public-facing version; this is the inside view.

## Pre-block checklist (do this in the 5 min before you start)

- [ ] Open VS Code in the Codespace and open the integrated terminal (`` Ctrl+` `` / `` Cmd+` ``). We're running Claude Code as a CLI from the terminal, not from the graphical panel — `claude` in the integrated terminal still gets VS Code's inline diff viewer and diagnostics for free, and (unlike the panel) lets us pick the working directory.
- [ ] Confirm Claude Code is on a recent version (`claude --version`, want `>= 2.1.61`). Older builds reject the `rse-plugins` manifest. Upgrade with `npm i -g @anthropic-ai/claude-code` if needed.
- [ ] Confirm Claude Code is signed in: run `claude` once and verify it doesn't prompt for login (then `/exit`). If it does prompt, follow the sign-in flow before going on stage.
- [ ] Confirm the `ai-research-workflows` plugin is installed: `claude plugin list` should include `ai-research-workflows`. If it's missing, run, in order:
    1. `claude plugin marketplace add https://github.com/uw-ssec/rse-plugins` (registers the source — this alone does **not** install anything)
    2. `claude plugin install ai-research-workflows@rse-plugins` (this is the step that actually installs the `/research`, `/plan`, `/implement`, `/validate` commands)
    3. Exit any running `claude` session; the next launch picks up the new slash commands.
- [ ] In the integrated terminal: `cd blocks/03-research-loop/demo && rm -rf .agents/`. We want a clean slate so artifacts appear *during* the demo. **Don't launch `claude` yet** — the demo starts with you running it live in front of the room (slide 4). Working directory matters: `claude`'s cwd becomes wherever you launch it, so cd'ing into `demo/` (not `demo/starter/`) makes `AGENTS.md` visible at the cwd, with the starter scripts in the `starter/` subfolder and the fallback `expected-artifacts/` right next to them.
- [ ] Have **all four prompts copied to a scratch buffer** (text file, sticky note, Slack DM to yourself, wherever you can paste fast). The exact prompts are below.
- [ ] Open `blocks/03-research-loop/demo/expected-artifacts/` in a side tab as the **fallback** in case the live demo fails.

## Timing checkpoints

| at minute | should be on slide / phase | content |
|---|---|---|
| 3 | slide 3 (6-phase workflow) | Done with framing |
| 6 | switching to Claude Code | Demo about to start |
| 10 | `/research` complete | Plan kicks off |
| 14 | `/plan` complete | Implement kicks off |
| 20 | `/implement` complete (or near it) | Validate kicks off |
| 22 | `/validate` complete | Switching back to slides |
| 26 | slide 5 (failure modes) -> slide 6 (mitigations) | Demo recap done |
| 27 | slide 7 (use cases) | Tour done |
| 29 | slide 8 (research vs. engineering) | Cross-field framing done |
| 30 | slide 9 (bridge) | Hand off to Block 4 |

If `/implement` is faster than expected, jump to slide 6 (mitigations) early. If it's slower, **keep narrating** failure modes, that's the design.

## Per-slide notes

### 1. Title

- 30 seconds. Hand-off from Block 2.
- *"Blocks 1 and 2 were about how it works. This block is about how to use it on real research code without it blowing up."*

### 2. Where we left off ("workflows are the prompt")

- This is the through-line. Land it explicitly.
- Connect: *"Block 2 said 'in the prompt' matters more than 'trained in.' Workflows are the systematic version of that, every phase of your work has a templated prompt."*

### 3. The 6-phase workflow

- Read the table. **Don't memorize**: the *patterns* at the bottom matter more than the individual commands.
- *"You don't use all six every time. You pick the pattern that matches your work."*
- Acknowledge: this is one specific implementation (`rse-plugins` for Claude Code). The pattern is portable; in Block 4, attendees will build their own.

### 4. Demo intro

- In the integrated terminal (already at `blocks/03-research-loop/demo`), run `claude`. Briefly show that there is no `.agents/` directory yet, and that `AGENTS.md` and the `starter/` scripts are right there at the cwd.
- *"We're going to package this. Watch the artifacts appear in `.agents/` as we go."*

### 5. Failure mode taxonomy

- Read across the rows. Spend most time on the **"Where it comes from"** column, that's the Block 2 payoff.
- Pick **one row to elaborate** based on audience: scientific computing audiences usually relate hardest to "niche language hallucination" and "confident wrong answers."

### 6. Mitigations

- Three groups: process, prompt-side, manual.
- *"Agents are coworkers, not magic. Coworkers get pushback."* Drop this line slowly.

### 7. Practical use cases

- 30 seconds total. Don't dwell on any row.
- The closing one-liner, *"agents expand what one person can attempt; the editorial judgment stays yours"*, is the takeaway.
- **Experiment management** (new row) is the one to flag for NLP / ML attendees: agent kicks off a sweep, summarizes results, drafts the next hypothesis. Office hours can dig in further.

### 8. Two modes: research vs. engineering

- 60-90 seconds. Reframes everything they just saw: the four-phase demo was the *durable* end of the dial. Research work usually wants the *fast* end.
- Read the table left-to-right. Then drop the punchline slowly: *"Pick the loop length to match the half-life of the code."*
- **The `AGENTS.md` callout is the answer to "how do I configure an agent for my research context?"** Stress it explicitly: *"This is the one file you'll edit most. It's portable across tools (Claude Code, Copilot, Cursor all read some flavor of it). Your domain conventions live there, not in your daily prompts."*
- For the cross-field examples: pick the closest field to your audience and elaborate for ~10 seconds. Examples:
  - **NLP / ML:** *"AGENTS.md = eval harness paths, metric definitions, 'always use seed=42', model registry conventions."*
  - **Behavioral / social science:** *"AGENTS.md = your coding scheme, IRB constraints on what data the agent may read, stats assumptions (parametric vs not), how you label conditions."*
  - **Bio / bioinformatics:** *"AGENTS.md = file-format conventions (BED, VCF), pipeline DAG, where the reference genome lives."*
  - **Physics / climate:** the demo we just ran.
- Don't oversell: we have *one* worked example (climate). The claim is that the workflow shape is portable, not that the workshop covers every field.

### 9. Bridge to Block 4

- Hard hand-off.
- *"Five files, no magic."*
- Stop talking.

## Demo script: the four prompts

Copy these to your scratch buffer before starting. **Run them one at a time, in order**, in your `claude` terminal session.

### Prompt 1: `/research` (target: 4 min)

```
/research I have two standalone Python scripts (climate_model.py and co2_emissions.py) implementing a Very Simple Climate Model. Research the current code structure, identify what's missing for it to be an installable scientific Python package, and document existing conventions and quirks (mixed tabs/spaces, missing types, hardcoded CSV paths, etc.). Read AGENTS.md first.
```

**What to narrate while it runs:**
- *"`/research` reads everything completely, not just snippets. It's a documentarian, not an evaluator."*
- *"Notice it's already discovered the `AGENTS.md` file and is reading it for context."*
- When the artifact appears: open `.agents/research-*.md` in a split view. Scroll through. Point at the `file:line` references.

### Prompt 2: `/plan` (target: 4 min)

```
/plan Read the research document and create an implementation plan to package these scripts as an installable Python package called vscm, following the Scientific Python guidelines in AGENTS.md. Use uv for the dev workflow and hatchling for the build backend. Phase the work so each phase is independently verifiable.
```

**What to narrate:**
- *"`/plan` reads the research document automatically, that's why we did `/research` first."*
- *"It asks clarifying questions. Watch."* (Sometimes it does, sometimes the AGENTS.md was specific enough that it doesn't.)
- When the artifact appears: open `.agents/plan-*.md`. Point at the **automated** vs **manual** verification sections. *"This is what makes `/validate` possible, we know what to check."*

### Prompt 3: `/implement` (target: 6 min: narrate failure modes during)

```
/implement .agents/plan-vscm-package.md
```

**What to narrate** (fill the agent's processing time with slides 5 and 6, failure modes + mitigations):

1. (Slide 5) Walk through the failure mode taxonomy. Pause periodically to glance at the agent's progress.
2. (Slide 6) Walk through mitigations.
3. By the time you finish slide 6, the implement should be done or close to it.

**Optional 30-second aside** (drop it once, while `/implement` is grinding, to preempt the "isn't this overkill?" question):

> *"What you're watching now is the slow, durable loop - we're going to ship this code. For day-to-day research iteration you'd just chat against `AGENTS.md`, or run `/research` alone. The point of the full loop is the audit trail in `.agents/`, not throughput. We come back to that on slide 8."*

**If `/implement` blows up live:** narrate the failure mode in real time. *"Look, it just hit context exhaustion / it's looping / it's hallucinating an API. This is the taxonomy on slide 5, in action."* Then pivot to the `expected-artifacts/` folder for the rest of the demo.

### Prompt 4: `/validate` (target: 2 min)

```
/validate .agents/plan-vscm-package.md
```

**What to narrate:**
- *"This is the quality gate. Without `/validate`, you'd just trust the agent's 'Done!' message."*
- When the report appears: read the pass/fail summary. If anything failed, **don't fix it live**, narrate it as a failure mode example and move on.

## Live-demo fallback plan

| Symptom | Recovery |
|---|---|
| `claude` won't launch / not signed in | Switch to slides 5-7 immediately; walk through the `expected-artifacts/` folder as if it were live output. Promise to debug after the block. |
| `claude plugin list` doesn't show `ai-research-workflows` | In a fresh terminal: `claude plugin marketplace add https://github.com/uw-ssec/rse-plugins && claude plugin install ai-research-workflows@rse-plugins`, then exit and re-launch `claude`. ~30 sec total. (Adding the marketplace alone does *not* install the plugin — both commands are required.) |
| `claude plugin install` fails with `Unrecognized keys: "category", "strict"` | Claude Code is too old. Upgrade: `npm i -g @anthropic-ai/claude-code`, restart, retry the install. |
| `/research` produces obviously wrong output | Open `expected-artifacts/research-vscm-package.md` and walk through it instead. Frame it as: *"the live one was a bit off; here's what a polished one looks like."* |
| `/implement` runs forever | Interrupt it with `Esc` (cancels the current tool and returns to the prompt; `Ctrl+C` exits the whole session, which we don't want). *"This is exactly the failure mode on slide 5, the model gets stuck. Here's what we'd do."* Switch to the pre-built `expected-artifacts/implement-*.md`. |
| The whole thing fails (proxy down, etc.) | Skip the demo entirely. Spend extra time on slides 5-7 (failure modes are the bigger conceptual content anyway). |

The expected-artifacts folder is your safety net. **Don't try to debug live.** A failed demo narrated as a failure mode is *better* than a successful demo, pedagogically.

## Common audience questions

| Question | Short answer |
|---|---|
| "Can I use rse-plugins with Copilot?" | "The plugin is Claude Code-specific, but the *pattern* (slash commands, markdown artifacts in `.agents/`) is portable. Block 4 walks through how to build a similar workflow in your tool of choice, Copilot prompt files are one option." |
| "Why didn't you use Copilot for this block?" | "Workshop's spine: all coding agents work the same way under the hood. Showing a different IDE *proves* the spine in front of the room. Block 4 brings it back to Copilot." |
| "Should I write workflows for my own projects?" | "Yes, but start small. One slash command for the workflow you do most often (e.g., `/run-tests-and-summarize` or `/explain-this-traceback`) is a good first project. That's Block 4." |
| "Does `/handoff` actually work?" | "Yes, it writes a self-contained markdown doc; the next session reads it and picks up. Especially valuable for long-running multi-day work." |
| "Can the agent's plan be wrong?" | "Often. That's why `/iterate-plan` exists, surgical edits, not regenerate. And why `/validate` is non-optional for anything you'd commit." |

## What to skip if you're behind time

In order of expendability:

1. The "iterate" / "experiment" / "handoff" rows on slide 3, collapse to "and three more for refinement, comparison, and context transfer."
2. One column of the failure modes table on slide 5, drop "Where it comes from" if you have to (sad, it's the Block 2 payoff, but the *mitigations* are more actionable).
3. The practical use cases tour (slide 7), collapse to one sentence: *"Agents help most with feature implementation, debugging, test writing, docs, code review, exploration, and experiment management; they're easiest to misuse on architectural decisions."*
4. The cross-field paragraph at the bottom of slide 8, keep the table, drop the prose. Or vice versa if you have a single-field audience.
5. The bonus discussion of `/validate` failures during the demo.

**Never skip:** the "workflows are the prompt" framing (slide 2), the demo (even if abbreviated to 2 phases), the research-vs-engineering table on slide 8 (it's why the durable loop isn't overkill), or the bridge to Block 4 (slide 9).
