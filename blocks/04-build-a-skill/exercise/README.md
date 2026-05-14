# Exercise: Build Your Own Chat Mode

By the end of this exercise (~15 min) you will have **a working Copilot
chat mode you wrote yourself**, runnable from the chat panel in this
Codespace.

The two worked examples in [`.github/chatmodes/`](../../../.github/chatmodes/)
(`scientific-python-reviewer` and `docstring-writer`) are your reference.
Read them, copy patterns, then make something different.

## 1. Setup (1 min)

Copy the template into the workshop's chatmodes directory. Pick a sensible
name, it'll show up in the chat mode picker.

```bash
cp blocks/04-build-a-skill/exercise/my-mode.chatmode.md.template \
   .github/chatmodes/my-mode.chatmode.md
```

(Replace `my-mode` with whatever you want to call your mode. Examples:
`error-explainer`, `style-checker`, `ssp-explainer`.)

## 2. Pick a target (1 min)

What code will your mode run against? Default options, in order of
relevance to the workshop:

1. **The climate model** in [`blocks/03-research-loop/demo/starter/`](../../03-research-loop/demo/starter/), realistic research Python, has obvious style and structure issues, fits a wide range of skills.
2. **`sci_units`** in [`blocks/01-landscape/demo/starter/`](../../01-landscape/demo/starter/), small and simple, good for narrow modes.
3. **Your own code**: paste a snippet into a scratch file, or open a folder you brought.

## 3. Pick a job (1 min)

What does your mode do? See [`ideas.md`](ideas.md) for ~15 starting ideas
across categories: code review, code generation, refactoring, climate-
specific, general research, onboarding.

Or invent your own. The good first ones are **narrow** ("review against
one specific guideline", "explain one specific kind of error") rather than
ambitious ("become a full agent for my project").

## 4. Edit the mode (8-10 min)

Open `.github/chatmodes/my-mode.chatmode.md` and fill in the TODOs:

| Field | Guidance |
|---|---|
| `description` | One line. Shows in the mode picker. Make it scannable. |
| `tools` | Start narrow. `['readFiles', 'codebase']` is read-only and safe. Add `editFiles` only if your mode needs to modify code. Add `runCommands` only if it needs to run shell (e.g., `pytest`). |
| Mode name (heading) | Match the filename minus `.chatmode.md`. |
| Persona / what you do | A few sentences setting role, then a numbered list of steps. Be specific. Vague prompts produce vague behavior. |
| What you do NOT do | The constraints are as important as the instructions. "Do not edit files outside `tests/`" is a real safety lever. |
| Output format | Show an example of what good output looks like. Concrete examples beat abstract descriptions. |

**Pattern to copy:** look at `.github/chatmodes/scientific-python-reviewer.chatmode.md` for a read-only mode and `.github/chatmodes/docstring-writer.chatmode.md` for a mode that edits files.

## 5. Try it (3-5 min)

1. Open Copilot Chat (the icon in the activity bar, or `Ctrl/Cmd+Shift+I`).
2. Click the **mode picker** at the top of the chat panel (it usually shows "Ask" or "Agent" by default).
3. Select your mode name. If you don't see it, see [Troubleshooting](#troubleshooting).
4. Type a query that exercises your mode.

Example queries depending on what you built:
- For a reviewer: *"Review `blocks/03-research-loop/demo/starter/climate_model.py`."*
- For a docstring writer: *"Add docstrings to `blocks/01-landscape/demo/starter/src/sci_units/converters.py`."*
- For an error explainer: *"Explain this traceback: <paste>."*

## 6. Iterate

Did your mode do what you expected? If not, that's the point.

- **Behavior too vague?** Tighten the steps in your system prompt.
- **Wrong tool used?** Adjust the `tools` list.
- **Output format off?** Add a more concrete example to the "Output format" section.
- **Mode being too cautious or too eager?** Add explicit "do NOT" constraints.

This iteration loop, *write, run, observe, adjust the prompt*, is the
same loop the rse-plugins authors used to build the polished Block 3
demo. You're doing real prompt engineering.

## 7. (Stretch) Show it off

If your mode works and you have a few minutes left, share it:
- Volunteer for the show-and-tell (instructor will ask).
- Paste the mode into the workshop chat / Slack / wherever.
- Save it to your own GitHub fork to keep using after the workshop.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Mode doesn't appear in the picker | Confirm filename ends in `.chatmode.md` and lives in `.github/chatmodes/`. Click the picker, then "Configure Modes", or run **Developer: Reload Window**. |
| Mode appears but won't load | Check the YAML frontmatter, common issues are missing quotes around the description or a malformed `tools` list. The first two lines should be `---` exactly. |
| Mode runs but ignores your prompt rules | The system prompt is too vague. Make the numbered steps more specific. Add a "do NOT" line for behaviors you've seen go wrong. |
| Mode tries to edit files but isn't allowed | Add `'editFiles'` to the `tools` list in frontmatter. |
| Mode runs forever | Add a max-iterations note in the system prompt: *"After at most 5 tool calls, summarize what you've done and stop."* |

If something else breaks, ask an instructor, that's exactly what they're
circulating for.
