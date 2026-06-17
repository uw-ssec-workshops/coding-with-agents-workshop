# Exercise: Build Your Own Custom Agent

By the end of this exercise you will have **a working Copilot
custom agent you wrote yourself**, runnable from the chat panel in this
Codespace.

The worked examples in [`.github/agents/`](../../../.github/agents/)
(`scientific-python-reviewer` and `docstring-writer`) are your reference.
Read them, copy patterns, then make something different.

You won't get the prompt right on the first try, and you're not meant to.
Steps 1–3 set you up; steps 4–6 are where you edit, run, and adjust until
the agent behaves.

## 1. Setup (1 min)

Copy the template into the agents directory. The name shows up in the
agent picker, so pick a sensible one.

```bash
cp blocks/04-build-a-skill/exercise/my-agent.agent.md.template \
   .github/agents/my-agent.agent.md
```

(Replace `my-agent` with whatever you want to call your agent. Examples:
`error-explainer`, `style-checker`, `assumption-checker`.)

## 2. Pick a target (1 min)

What code (or data, or notebook) will your agent run against? Pick
whichever gets you to "running" fastest:

**Your own work** — a snippet of code, a notebook, a CSV from your lab, a transcript. This is the most useful target if you brought something. The pattern is identical regardless of domain (physical science, ML, behavioral / social science, bio, stats, qualitative work).

No code of your own? Use `sci_units` or the Block 3 dataset, or drop a
notebook or CSV from your lab into a scratch folder. The point is the
*pattern*, not the example.

## 3. Pick a job (1 min)

What does your agent do? See [`ideas.md`](ideas.md) for 30+ starting ideas
across categories: code review, code generation, refactoring, HCI /
experiment analysis, general research, behavioral / social science / stats,
experiment management, onboarding.

Or invent your own. The good first ones are **narrow** ("review against
one specific guideline", "explain one specific kind of error") rather than
ambitious ("become a full agent for my project").

## 4. Edit the agent (8-10 min)

Your first pass doesn't have to be complete, just enough to run.
Open `.github/agents/my-agent.agent.md` and fill in the TODOs:

| Field | Guidance |
|---|---|
| `name` | The identifier shown in the agent picker. Match the filename minus `.agent.md`. |
| `description` | One line. Shows next to the name. Make it scannable. |
| `tools` | Start narrow. `['read', 'search/codebase']` is read-only and safe. Add `edit/editFiles` only if your agent needs to modify code. Add `execute/runInTerminal` only if it needs to run shell (e.g., `pytest`). |
| Persona / what you do | A few sentences setting role, then a numbered list of steps. Be specific. Vague prompts produce vague behavior. |
| What you do NOT do | The constraints are as important as the instructions. "Do not edit files outside `tests/`" is a real safety lever. |
| Output format | Show an example of what good output looks like. Concrete examples beat abstract descriptions. |

**Pattern to copy:** look at `.github/agents/scientific-python-reviewer.agent.md` for a read-only agent and `.github/agents/docstring-writer.agent.md` for an agent that edits files.

## 5. Try it (3-5 min)

Run the agent and watch what it actually does, noting anything it got wrong.

1. Open Copilot Chat (the icon in the activity bar, or `Ctrl/Cmd+Shift+I`).
2. Click the **agent picker** at the top of the chat panel (it usually shows "Ask" or "Agent" by default).
3. Select your agent name. If you don't see it, see [Troubleshooting](#troubleshooting).
4. Type a query that exercises your agent.

Example queries depending on what you built:
- For a reviewer: *"Review `blocks/01-landscape/demo/starter/src/sci_units/converters.py`."*
- For a docstring writer: *"Add docstrings to `blocks/01-landscape/demo/starter/src/sci_units/converters.py`."*
- For an assumption checker: *"Check the normality assumption on `blocks/03-research-loop/demo/starter/data.csv`."*
- For an error explainer: *"Explain this traceback: <paste>."*

## 6. Iterate (back to step 4)

Did your agent do what you expected? If not, match what you saw to a fix:

- **Behavior too vague?** Tighten the steps in your system prompt.
- **Wrong tool used?** Adjust the `tools` list.
- **Output format off?** Add a more concrete example to the "Output format" section.
- **Agent being too cautious or too eager?** Add explicit "do NOT" constraints.

Change one thing at a time, then re-run. Two or three passes is normal;
stop when it's good enough to be useful. This is the same prompt
engineering behind the Block 3 research-loop skills in `.github/skills/`.

## 7. Stretch: take it further

If your agent is working and you've still got time, pick one of these.
Each is ~10-20 min, none are required, all are good office-hours starting
points. Expect to iterate on these the same way as steps 4–6.

### Stretch A — Promote your agent to a Copilot skill

A **skill** (`.github/skills/<name>/SKILL.md`) is the next primitive up
from an agent: it can bundle scripts and resources and load on demand.
The fields are slightly different (YAML frontmatter with `name` and
`description`; markdown body) but the *shape* is identical to a Copilot
agent: persona + steps + tools + output format. See the worked
Block 3 research-loop skills in [`.github/skills/`](../../../.github/skills/).

1. Make `.github/skills/<your-skill-name>/` at the repo root.
2. Copy the skeleton into it and fill in the TODOs (or paste the body from your agent):

```bash
mkdir -p .github/skills/my-skill
cp blocks/04-build-a-skill/exercise/my-skill.SKILL.md.template \
   .github/skills/my-skill/SKILL.md
```

3. Reload the window; ask for it in plain language (or `/`-invoke it) in Copilot Chat.

Same handful of fields, different file path. That's the "primitives are
just structured prompts" claim from Block 1, made concrete.

### Stretch B — Chain two agents with a Copilot prompt file

Agents are good for one-job interactions. **Prompt files**
(`.github/prompts/*.prompt.md`) are good for one-shot orchestrations
("review this, then fix what you found"). The `.github/prompts/` folder
already has a few worked commands to copy from.

1. Copy the skeleton into the prompts directory:

```bash
cp blocks/04-build-a-skill/exercise/my-prompt.prompt.md.template \
   .github/prompts/review-and-fix.prompt.md
```

2. Fill in the body — e.g. *"First, review `${input:target}` against Scientific Python guidelines. Then add the missing docstrings."*
3. Invoke from chat with `/review-and-fix target=path/to/code.py`.

Prompt files are the one-shot cousin of the Block 3 research-loop skills:
where a skill is a multi-step capability the agent auto-selects, a prompt
file is a templated `/slash` command you fire deliberately.

### Stretch C — Add path-scoped instructions

The fourth primitive. **Instructions** (`.github/instructions/*.instructions.md`)
aren't invoked at all — Copilot auto-injects them whenever a file matching their
`applyTo` glob is in context. They're the place for "always do X in files like
this" rules. See the worked examples in
[`.github/instructions/`](../../../.github/instructions/).

1. Copy the skeleton into the instructions directory:

```bash
cp blocks/04-build-a-skill/exercise/my-instruction.instructions.md.template \
   .github/instructions/my-rules.instructions.md
```

2. Set `applyTo` to the files your rules govern (e.g. `"**/tests/**/*.py"`) and
   fill in the bullet list of conventions.
3. Open a matching file and start a chat — the rules apply with no invocation.

## 8. Show it off

If your agent works and you have a few minutes left, share it:
- Volunteer for the show-and-tell (instructor will ask).
- Paste the agent into the workshop chat / Slack / wherever.
- Save it to your own GitHub fork to keep using after the workshop.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Agent doesn't appear in the picker | Confirm filename ends in `.agent.md` and lives in `.github/agents/`. Click the picker, then "Configure Custom Agents", or run **Developer: Reload Window**. |
| Agent appears but won't load | Check the YAML frontmatter, common issues are missing quotes around the description or a malformed `tools` list. The first two lines should be `---` exactly. |
| Agent runs but ignores your prompt rules | The system prompt is too vague. Make the numbered steps more specific. Add a "do NOT" line for behaviors you've seen go wrong. |
| Agent tries to edit files but isn't allowed | Add `'edit/editFiles'` to the `tools` list in frontmatter. |
| Agent runs forever | Add a max-iterations note in the system prompt: *"After at most 5 tool calls, summarize what you've done and stop."* |

If something else breaks, ask an instructor, that's exactly what they're
circulating for.
