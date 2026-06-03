---
agent: agent
description: 'Write a self-contained handoff doc to .agents/ so a fresh chat can resume the work.'
tools: ['read', 'search/codebase', 'search', 'execute/runInTerminal', 'edit/editFiles']
---

# Handoff (transfer context to a new session)

Write a **thorough but concise** handoff so a fresh Copilot Chat (with none of
this conversation's context) can pick the work up cleanly. This is the
context-compaction lever for long sessions.

Optional focus note: `${input:note:anything to emphasize in the handoff (blank = summarize the whole session)}`.

## Steps

1. **Gather git state:** current branch, short commit hash, and a summary of
   uncommitted changes (`git status`, `git diff --stat`).
2. **Find workflow artifacts** in `.agents/` (`research-*`, `plan-*`,
   `experiment-*`, `implement-*`, prior `handoff-*`).
3. **Review the session:** what was worked on, the current workflow phase, and
   which artifacts were produced or referenced.
4. **Write** `.agents/handoff-YYYY-MM-DD-HH-MM-<slug>.md` using the structure
   below.
5. **Present** a short summary plus the one line the next session should paste to
   resume.

## Artifact structure (`.agents/handoff-<timestamp>-<slug>.md`)

```
# Handoff: <brief description>

Date: <YYYY-MM-DD HH:MM> · Branch: <branch> · Commit: <short hash>

## Task(s)
| Task | Status | Notes |
|---|---|---|
| <task> | ✅ done / 🔄 in progress / 📋 planned | <note> |

Current workflow phase: Research | Plan | Iterate | Experiment | Implement | Validate

## Workflow artifacts
- [plan-<slug>.md](plan-<slug>.md) — <what it is>
(omit artifact types that don't exist)

## Critical references
- `path/to/file.ext` — why the next session must read it first

## Recent changes
- `path/to/file.ext:lines` — what changed

## Learnings
- <non-obvious insight, gotcha, or pattern that matters>

## Next steps
1. [ ] <specific next action>
**Recommended next command:** `/research` | `/plan` | `/iterate-plan` | `/experiment` | `/implement` | `/validate`
```

## Writing guidelines

- More information, not less — this structure is the minimum.
- Prefer `path/to/file.ext:line` references over pasted code blocks (only paste
  code for an active bug or a critical pattern).
- Cross-link the `.agents/` artifacts by filename so the next session can read them.
- Always state the recommended next command for where the work sits.
