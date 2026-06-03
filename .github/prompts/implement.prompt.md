---
agent: agent
description: 'Execute an approved plan phase by phase, verifying as you go, then write an implementation report to .agents/.'
tools: ['read', 'edit/editFiles', 'search/codebase', 'search', 'execute/runInTerminal']
---

# Implement (phase 3 of the research loop)

Execute an approved plan, one phase at a time, keeping progress visible.

Plan to implement: `${input:plan:path to the plan, e.g. .agents/plan-vscm-package.md}`.
If blank, look for the most recent `.agents/plan-*.md`.

## Getting started

1. Read the plan **completely**. Note any phases already checked off (`- [x]`)
   and resume from the first unchecked item.
2. Read every file the plan references, in full, before editing.
3. Understand how the changes fit the existing architecture and conventions
   (follow `AGENTS.md` and existing patterns — don't invent new ones).

## Per-phase loop

For each phase, in order:

1. Implement all tasks in the phase.
2. Check off completed tasks in the plan file (edit `- [ ]` → `- [x]`).
3. Run the phase's **automated verification** commands (e.g. `uv run pytest -q`).
4. Fix any failures before moving on — don't leave broken tests.
5. Pause and report automated results; list the **manual verification** items for
   the user. Wait for confirmation before the next phase, unless the user asked
   you to run phases consecutively (then verify automated after each, and pause
   for manual only at the end).

## Handling mismatches

If reality doesn't match the plan, **STOP** and present it clearly: what the plan
expected, what you found, why it matters, and 1-2 options. Let the user decide
rather than guessing.

## Final report (`.agents/implement-<slug>.md`)

When all phases are done, write a report (slug from the plan filename):

```
# Implementation: <goal>

Plan: [plan-<slug>.md](plan-<slug>.md)

## Phases completed
- Phase 1: <name> — done
- ...

## Files changed
- created: <paths>
- modified: <paths>

## Verification
### Automated
- ✅ `uv run pytest -q` — N passed
### Manual (pending human)
- [ ] <item>

## Issues encountered
<what came up and how it was resolved>

## Next steps
- Run `/validate <plan path>`
```

## Constraints

- Follow the plan's intent; adapt to reality but communicate every deviation.
- Complete one phase fully before starting the next.
- Do NOT check off manual-verification items — only the user confirms those.
- Keep edits within the plan's scope. New scope → back to `/plan`.

Next phase: `/validate` checks this against the plan.
