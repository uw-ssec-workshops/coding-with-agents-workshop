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

What code (or data, or notebook) will your mode run against? Pick
whichever gets you to "running" fastest:

1. **Your own work** — a snippet of code, a notebook, a CSV from your lab, a transcript. This is the most useful target if you brought something. The chatmode pattern is identical regardless of domain (physical science, ML, behavioral / social science, bio, stats, qualitative work).
2. **The climate model** in [`blocks/03-research-loop/demo/starter/`](../../03-research-loop/demo/starter/), realistic research Python, has obvious style and structure issues, fits a wide range of skills.
3. **`sci_units`** in [`blocks/01-landscape/demo/starter/`](../../01-landscape/demo/starter/), small and simple, good for narrow modes.

If you didn't bring something, that's fine — use the climate model. If
the climate model feels far from your work, drop a notebook or CSV from
your lab into a scratch folder and target that. The point is the
*pattern*, not the example.

## 3. Pick a job (1 min)

What does your mode do? See [`ideas.md`](ideas.md) for ~30 starting ideas
across categories: code review, code generation, refactoring, climate-
specific, general research, behavioral / social science / stats,
experiment management, onboarding.

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

## 7. Stretch: take it further

If your mode is working and you've still got time (or you've built
chat modes before and want to push past the basics), pick one of these.
Each is ~10-20 min on its own, none are required, all are great
office-hours starting points if you don't finish.

### Stretch A — Port your mode to a Claude Code skill

The Block 3 panel uses Claude Code, which has its own skill format
(`.claude/skills/<name>/SKILL.md`). The fields are slightly different
(YAML frontmatter with `name` and `description`; markdown body) but the
*shape* is identical to a Copilot chatmode: persona + steps + tools +
output format.

1. Make `.claude/skills/<your-skill-name>/` at the repo root.
2. Create `SKILL.md` with `---\nname: <your-skill-name>\ndescription: <one line>\n---` frontmatter, then paste the body from your chatmode.
3. Open Claude Code in the integrated terminal; your skill is now available as a slash command.

Same six fields, different file path. That's the "tools are mostly UX
differences" claim from Block 1, made concrete.

### Stretch B — Chain two modes with a Copilot prompt file

Chat modes are good for one-job interactions. **Prompt files**
(`.github/prompts/*.prompt.md`) are good for one-shot orchestrations
("review this, then fix what you found").

1. Create `.github/prompts/review-and-fix.prompt.md`.
2. Write a body like: *"First, run `scientific-python-reviewer` against `${input:file}`. Then, based on the review, switch to `docstring-writer` and add the missing docstrings."*
3. Invoke from chat with `/review-and-fix file=path/to/code.py`.

This is what the rse-plugins workflow is doing under the hood:
slash commands chained into a pipeline.

### Stretch C — Sketch an MCP server stub for a new tool

Chat modes use existing tools (`readFiles`, `editFiles`, etc.). To give
your agent a *new* tool (e.g., "summarize results from this MLflow run",
"query our internal experiment DB"), you write an **MCP server**.

You won't ship a real one in 15 minutes, but you can sketch the
interface. In a scratch file, write:

```
Tool name: summarize_experiment
Inputs: { run_dir: string }
Outputs: { metrics: {...}, best_checkpoint: string, summary_md: string }
What it does (1-2 sentences): ...
```

Bring it to office hours; instructors can help wire it up against the
[MCP SDK](https://modelcontextprotocol.io). Especially useful for
**experiment management** workflows — wrap your run tracker, give the
agent a real tool, stop pasting metrics into chat.

## 8. Show it off

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
