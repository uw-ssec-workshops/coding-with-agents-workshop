# Block 1: Instructor Notes

These are the notes you actually deliver from. The slide deck has the
public-facing version; this is the inside view.

## Pre-block checklist (do this in the 5 min before you start)

- [ ] Reset the demo: `cd blocks/01-landscape/demo/starter && git checkout -- src/sci_units/converters.py`
- [ ] Run the failing test once to confirm: `uv run pytest -v` → 2 failed, 2 passed.
- [ ] Open VSCode in the workshop Codespace, with two windows arranged:
  - **Left:** `slides.md` Marp preview, full-screen on the projector.
  - **Right:** A second VSCode window in `blocks/01-landscape/demo/starter/` for the Copilot demo, plus `blocks/01-landscape/demo/notebook.ipynb` open in a tab.
- [ ] Copy this prompt to your clipboard so you can paste during the demo:

  ```
  There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change.
  ```

- [ ] Confirm LiteLLM proxy credentials are visible in the Codespace terminal: `echo $LITELLM_BASE_URL` should print the proxy URL.
- [ ] Restart the notebook kernel so it shows a clean state.

## Timing checkpoints

Glance at these. If you're behind, cut from the "Landscape" or "Axes that matter" slides, they have the most fat.

| at minute | should be on slide | content |
|---|---|---|
| 2 | slide 2 (What changed) | Done with the hook |
| 7 | slide 4 (Axes that matter) | Done with the tool tour |
| 15 | slide 6 (Why they all feel the same) | Done with the anatomy |
| 21 | slide 7 (where does your data go?) | Data-sensitivity framing; skippable if behind |
| 22 | slide 8 (Demo) | Demo about to start |
| 28 | slide 9 (Bridge) | Demo done, transitioning |
| 30 | hand off to Block 2 | |

## Per-slide notes

### 1. Title

- 30 seconds. Welcome. State the spine: **"all coding agents work the same way under the hood."**
- This isn't a tool review. It's a mental model that outlasts any product.
- Frame the arc: *this block is the map; Block 2 is the engine; Block 3 is the workflow; Block 4 is the build.*

### 2. What changed

- Most attendees have used some autocomplete-ish tool already.
- **Don't oversell.** The point is the *category* changed, not the quality.
- Don't get into history. Move on.

### 3. The landscape

- 30 seconds per row, max. Six rows = three minutes. Don't dwell.
- If asked "which is best?" → defer with: "wrong question. Look at slide 4."
- If asked about a tool not on the list (Devin, Replit Agent, etc.) → "same anatomy, different wrapper."
- Emphasize: *this list will be different in 6 months. The categories won't.*

### 4. Axes that matter

- Don't fixate on the count, the list isn't exhaustive. The point is *which axes matter for your constraints*, not memorizing four (or five) of them.
- Emphasize: **for science, model hosting and privacy matter more than for industry.** Data residency, IRB, air-gapped clusters, proprietary code, unpublished research. (Privacy gets its own slide, slide 7, right before the demo, just plant the seed here.)
- Capability claims are noisy. The only benchmark that matters is your own code on your own task.

### 5. Anatomy of a coding agent

- This is *the* slide of Block 1. Spend real time here. **Reference this diagram for the rest of the workshop.**
- Each label maps to a concrete file, function, or API call you'll see in the demo.
- Walk through each box. For each, name a concrete example:
  - LLM backbone → "Claude Sonnet 4.5, GPT-5, Gemini 2.5, pick one."
  - Agent loop → "decides what to do next based on what just happened."
  - Tools → "read file, edit file, run shell command."
  - Memory → "AGENTS.md or copilot-instructions.md is loaded into the system prompt."
  - MCP → "a way to plug new tools into any agent without rewriting the agent."
  - Skills/prompts → "templated behaviors you invoke by name."
- Tell them: **the demo will show every one of these.**

### 6. Why they all feel the same

- Read across the rows, not down the columns.
- Don't apologize for tools you didn't pick. Make the framing-claim instead: *if you understand the pieces, switching is a config exercise.*
- This is the workshop's spine, say it explicitly. Pay-off: *when a new tool launches next quarter, you'll know what to look for.*

### 7. Before you paste: where does your data go?

- 60-90 seconds, and the most science-specific slide in the block. Don't rush past it: for many attendees "can I even put my data in here?" is the real blocker to adopting agents.
- The actionable line: **"match the model hosting to the sensitivity of the data, and when in doubt, don't paste it."**
- Make the workshop setup concrete: *"That's why we run a proxy/gateway instead of having you each paste into a consumer chatbot, the requests stay inside a controlled endpoint."*
- The redaction tip is the practical out: *"You rarely need the real data. A synthetic sample or a redacted snippet is usually enough for the agent to help."*
- Skippable if you're behind: fold it back into the slide-4 "model hosting" bullet as a one-liner. But try to keep it, this is the slide that earns trust with a cautious research audience.

### 8. Demo intro

- Confirm the converters file is reset to the buggy state (you did this in the pre-block checklist).
- Open Copilot Chat in agent mode (the icon at the top of the chat panel; or `Ctrl+Shift+I` then switch to "Agent" from the picker).
- Say: "Same task, two ways. Watch how it feels."

### 9. Bridge to Block 2

- Hard hand-off. Don't linger. Block 2 is where the *"why does this work"* answer lives.
- Last sentence: *"That behavior was trained in. That's Block 2."*

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
- *It edits the wrong file:* manually revert with `git checkout`, point out that even good agents make mistakes, **don't try again live**, go straight to the notebook.
- *It loops or stalls:* cancel, switch to the notebook. The notebook is your safety net.

### Part B: The notebook (target: 4 min)

1. **Open `notebook.ipynb`**. Kernel: `Workshop (Python 3.12)`.
2. **Restart kernel and run all cells from the top.** Narrate as you go:
   - **Cell 2 (imports + client)**: "Two lines wire up `litellm` to the workshop proxy via `LITELLM_API_KEY` + `LITELLM_BASE_URL`. *That's the LLM backbone.* Note the `MODEL` is just a string, try `gpt-5` or `gemini-2.5-flash` later, the loop won't change."
   - **Cell 4 (sandbox)**: "Tools are gated. The agent can't touch anything outside `starter/`."
   - **Cell 6 (reset)**: "We re-break the file so the demo is reproducible."
   - **Cells 8 + 10 (tools + schemas)**: "Three tools. JSON Schemas tell the model how to call them."
   - **Cell 12 (system prompt + AGENTS.md)**: "This is project memory. We just paste `AGENTS.md` into the system prompt, same trick Claude Code does, same trick `.github/copilot-instructions.md` does."
   - **Cell 14 (loop)**: "This is the whole agent. Twenty-five lines."
   - **Cell 16 (run)**: kick it off. Watch the trace stream. Let participants read the `[tool_use]` and `[tool_result]` lines. **This is the moment.**
3. **Punchline**: "That's it. That's all there is. Copilot, Claude Code, Cursor, they're all this loop with more tools, better UX, and project memory."

**If the proxy fails:**
- Notebook ships with cells *not* pre-executed (intentionally, to keep the diff clean), so a live failure is visible.
- Fallback: walk through the code as a literate read-along. The notebook is *also* a teaching document, not just a runnable thing.
- If it's an auth error, the issue is `LITELLM_API_KEY` not being passed through to the kernel, this is the most common live failure. `os.environ.get('LITELLM_API_KEY')` in a fresh cell will tell you (don't print the value on the projector, just check it's truthy).

## Common questions and how to handle them

| Question | Short answer |
|---|---|
| "Why Copilot and not Claude Code / Cursor?" | "Lowest friction in Codespaces, and our LLM proxy gives Copilot AND the notebook access to the same Claude model. The skills transfer to other tools." |
| "Won't this be obsolete in a year?" | "The products will change. The six pieces won't." |
| "Is the model running locally?" | "No, behind an LLM proxy server that fronts Claude. We'll talk about hosting trade-offs in the open-source slot." |
| "What's an LLM proxy server?" | "A small server that exposes one API surface (Anthropic-compatible, here) over many model providers. It's how we give the room access to Claude without handing out 30 separate API keys." |
| "What's MCP?" | "A standard protocol for plugging tools into any agent. We'll build one in Block 4." |
| "How do I use this on my own data?" | "Office hours tomorrow." |

## What to skip if you're behind time

In order of expendability:

1. The "Axes that matter" slide (slide 4), can be a 30-second mention.
2. The third row of the comparison table on slide 6.
3. The "where does your data go?" slide (slide 7), collapse to the one-liner *"match model hosting to data sensitivity; when in doubt, don't paste it"* (but keep it if the audience handles sensitive data).

**Never skip:** the anatomy slide, the demo, or the bridge.
