# Block 1: The AI Coding Agent Landscape

## What's in this folder

```
01-landscape/
  README.md            # this file
  slides.md            # Marp slides
  instructor-notes.md  # speaker notes, demo script, fallbacks, timing
  resources.md         # curated further reading
  demo/
    AGENTS.md          # example project memory (loaded by the agent)
    starter/           # tiny sci_units Python package with a failing test
    notebook.ipynb     # "Agent in 50 lines" via the LiteLLM SDK using our proxy
```

## How to run the material

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

## Bridge to Block 2

This block ends with a question: *"Why does the model know to call `run_bash` instead of just describing it in prose?"* That's post-training, and it's the subject of Block 2.
