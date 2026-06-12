# Block 1: The AI Coding Agent Landscape

**Duration:** ~30 minutes
**Tool focus:** GitHub Copilot in VSCode/Codespaces (with Claude via the workshop's LLM proxy server as the model backend).
**Spine of the workshop:** *all coding agents work the same way under the hood.*

## Learning goals

By the end of this block, an attendee can:

1. Name the major AI coding agent products in 2026 (Copilot, Claude Code, Cursor, OpenCode, Aider, Cline) and place each on four axes: cost, capability, integration, and model hosting.
2. Identify the six load-bearing parts of a modern coding agent, **LLM backbone, agent loop, tool use, project memory (`AGENTS.md`), MCP servers, skills/prompts**, and point to where each lives in a real product.
3. Explain *why* the choice between Copilot, Claude Code, and Cursor is mostly a UX choice, not a capability choice.
4. Decide, for a given piece of research code or data, whether it's safe to send to a given agent, by matching **model hosting** to **data sensitivity** (PII/IRB, embargoed, licensed, retention/training policy).
5. Run a working agent end-to-end against Claude (via the workshop's LLM proxy) in a Jupyter notebook and read the loop's tool-call trace.

## What's in this folder

```
01-landscape/
  README.md            # this file
  slides.md            # Marp slides (~11 slides, 22 min talking)
                       # (theme: shared blocks/_shared/slides.css)
  instructor-notes.md  # speaker notes, demo script, fallbacks, timing
  resources.md         # curated further reading
  demo/
    AGENTS.md          # example project memory (loaded by the agent)
    starter/           # tiny sci_units Python package with a failing test
    notebook.ipynb     # "Agent in 50 lines" via the LiteLLM SDK -> LiteLLM proxy
```

## Timing (30 min)

| min | section |
|---|---|
| 0–2 | Hook + landscape framing |
| 2–7 | Tour of the major tools |
| 7–15 | Anatomy of a coding agent (the spine) |
| 15–17 | "They're all the same" |
| 17–20 | Picking a tool (decision flow) |
| 20–21 | Where does your data go? (data-sensitivity framing; skippable) |
| 21–28 | **Demo**: 2 min live Copilot + 4 min "agent in 50 lines" notebook |
| 28–30 | Bridge to Block 2 |

## How to run the material

### View / present the slides

The Codespace ships with the **Marp for VS Code** extension installed. Two ways to use it:

1. **Live preview while editing**: open `slides.md` and click the preview icon at the top right of the editor (or `Cmd/Ctrl+Shift+V`). Edits hot-reload.
2. **Present full-screen**: open the command palette (`Cmd/Ctrl+Shift+P`) and run **`Marp: Open preview to the side`**, then drag the preview pane to your projector window and toggle full-screen with `F5`.

To export to HTML, PDF, or PPTX (for sharing handouts), run **`Marp: Export Slide Deck...`** from the command palette and pick a format.

### Run the demo

The demo is run **twice** during the block, against the same scenario:

1. **Live with Copilot.** Open `demo/starter/`, open Copilot Chat in agent mode, and paste the prompt from `instructor-notes.md`. Expected: Copilot reads `tests/test_converters.py`, sees both tests fail, edits `src/sci_units/converters.py`, re-runs, and reports success.
2. **In the notebook.** Open `demo/notebook.ipynb` and run all cells. Same scenario, same outcome, but now you can see the JSON tool calls, the system prompt, and the agent loop in plain Python.

### Reset the demo

After running it, the `converters.py` file is fixed. To reset for the next run:

```bash
cd blocks/01-landscape/demo/starter
git restore src/sci_units/converters.py
```

## Prerequisites

- Codespace running (see top-level [`README.md`](../../README.md)).
- LiteLLM proxy credentials configured: `LITELLM_API_KEY` and `LITELLM_BASE_URL` (verified by `post-start.sh`).
- Copilot extension signed in.

## Bridge to Block 2

This block ends with a question: *"Why does the model know to call `run_bash` instead of just describing it in prose?"* That's post-training, and it's the subject of Block 2.
