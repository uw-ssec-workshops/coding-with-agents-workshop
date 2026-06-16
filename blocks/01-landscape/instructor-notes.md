# Block 1: Instructor Notes

These are the notes you actually deliver from. The slide deck has the
public-facing version; this is the inside view.

## Keep these handy 

- Prompt you can paste during the demo:

  ```
  There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change.
  ```

## Per-slide notes

### 1. Title

- Let's start with Block 1 that maps the AI Coding Agent Landscape

### 2. What changed

- Look at slide.

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

- Look at slide.

### 7. Before you paste: where does your data go?

- Look at slide.

### 8. Demo intro

- Confirm the converters file is reset to the buggy state and tests are failing. (you did this in the pre-block checklist).
- Open Copilot Chat in agent mode
- "There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change.""

### 9. Bridge to Block 2

- Look at slide.

## Demo script

### Part A: Live Copilot (target: 2 min)

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

### Part B: The notebook (target: 4 min)

1. **Open `notebook.ipynb`**. Kernel: `Python Environments`.
2. **Restart kernel and run all cells from the top.**:
   - **Cell 2 (imports + client)**: "Two lines wire up `litellm` to the workshop proxy via `LITELLM_API_KEY` + `LITELLM_BASE_URL`. *That's the LLM backbone.* Note the `MODEL` is just a string, try `gpt-5` or `gemini-2.5-flash` later, the loop won't change."
   - **Cell 4 (sandbox)**: "Tools are gated. The agent can't touch anything outside `starter/`."
   - **Cell 6 (reset)**: "We re-break the file so the demo is reproducible."
   - **Cells 8 + 10 (tools + schemas)**: "Three tools. JSON Schemas tell the model how to call them."
   - **Cell 12 (system prompt + AGENTS.md)**: "This is project memory. We just paste `AGENTS.md` into the system prompt, same trick Claude Code does, same trick `.github/copilot-instructions.md` does."
   - **Cell 14 (loop)**: "This is the whole agent. Twenty-five lines."
   - **Cell 16 (run)**: kick it off. Watch the trace stream. Let participants read the `[tool_use]` and `[tool_result]` lines. This is the core of the demo.
3. **Punchline**: "That's it. That's all there is. Copilot, Claude Code, Cursor, they're all this loop with more tools, better UX, and project memory."

**If the proxy fails:**
- Notebook ships with cells *not* pre-executed (intentionally, to keep the diff clean), so a live failure is visible.
- Fallback: walk through the code as a literate read-along. The notebook is *also* a teaching document, not just a runnable thing.
- If it's an auth error, the issue is `LITELLM_API_KEY` not being passed through to the kernel, this is the most common live failure. `os.environ.get('LITELLM_API_KEY')` in a fresh cell will tell you (don't print the value on the projector, just check it's truthy).
