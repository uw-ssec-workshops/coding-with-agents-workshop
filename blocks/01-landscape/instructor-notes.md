# Block 1: Instructor Notes


## Per-slide notes

### 1. Title

- Let's start with Block 1 that maps the AI Coding Agent Landscape

### 2. What changed

- Read the slide.

### 3. The landscape

- Emphasize that the list will be different in 6 months. 

### 4. Axes that matter

- Don't fixate on the count, the list isn't exhaustive. The point is *which axes matter for your constraints*, not memorizing four (or five) of them.
- Emphasize: **for science, model hosting and privacy matter more than for industry.** Data residency, IRB, proprietary code, unpublished research. 
- Capability claims are noisy after a certain threshold. The only benchmark that matters is your own code on your own task.

### 5. Anatomy of a coding agent

- For each, name a concrete example:
  - LLM backbone: "Claude Sonnet 4.5, GPT-5, Gemini 2.5, pick one."
  - Agent loop: "decides what to do next based on what just happened."
  - Tools: "read file, edit file, run shell command."
  - Memory: "AGENTS.md or copilot-instructions.md is loaded into the system prompt."
  - MCP: "a way to plug external data sources tools into any agent without rewriting the agent."
  - Skills/prompts: "templated behaviors you invoke by name."
- Emphasize that the demo will show every one of these.

### 6. Why they all feel the same

- Read the slide.

### 7. Before you paste: where does your data go?

- Read the slide.

### 8. Demo intro

- Confirm the converters file is reset to the buggy state and tests are failing. (you did this in the pre-block checklist).
- Open Copilot Chat in agent mode
- "There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change.""

### 9. Bridge to Block 2

- Read the slide.

## Demo script

### Part A: Live Copilot 

1. **Set the scene** (15s). "Here's a tiny package with a failing test. I'm going to ask Copilot in agent mode to fix it. I won't tell it where the bug is."
2. **Open Copilot Chat → Agent mode**. Make sure the workspace folder is `blocks/01-landscape/demo/starter`.
3. **Paste the prompt** from your clipboard:

   > There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change.

4. **Narrate as it works** (60–90s). Point at:
   - "It's reading the test file." (`read_file` call)
   - "It's running pytest." (`run_in_terminal` call)
   - "It's reading the implementation."
   - "It's editing the file." (the diff appears)
   - "It's re-running pytest." (green)
5. **Punchline** (15s). "OK, that's the polished version. Now let's see the same thing without polish."

**If Copilot misbehaves:**
- *It refuses to run pytest:* tell it explicitly "run `uv run pytest -v` from the project root."
- *It edits the wrong file:* manually revert with `git checkout`, point out that agents make mistakes all the time and go straight to the notebook.
- *It loops or stalls:* cancel, switch to the notebook. 

### Part B: The notebook 

- Kernel: `Python Environments`.
