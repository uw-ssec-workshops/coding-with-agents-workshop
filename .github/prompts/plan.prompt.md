---
agent: agent
description: 'Turn research into a phased, testable implementation plan written to .agents/.'
tools: ['read', 'search/codebase', 'search', 'search/usages', 'edit/editFiles']
---

# Plan (phase 2 of the research loop)

Produce a detailed, **testable** implementation plan. A plan is a technical
specification that bridges understanding and execution, not a vague task list.

What to plan: `${input:goal:what to build, e.g. "package the climate model as an installable vscm package following AGENTS.md"}`.

## Context first

1. Read any research doc in `.agents/` that matches the goal
   (`.agents/research-*.md`) **completely**, plus any files it references.
2. If no research exists, say so and suggest running `/research` first, but
   proceed if the user prefers.
3. Read `AGENTS.md` if present — it carries the project's conventions.

## Be skeptical and interactive

- Verify assumptions against actual code; don't guess.
- Ask the user only **product/judgment** questions (scope, priorities, ambiguous
  behavior). Never ask things you can answer by reading the code.
- Propose the phase breakdown and get a quick nod before writing full detail.

## Write the artifact (`.agents/plan-<slug>.md`)

Create `.agents/` if needed; derive `<slug>` from the goal. Fill every section:

```
# Plan: <goal>

## Overview
<what, why, high-level how>

## Current state
<relevant existing code, with file:line references>

## Desired end state
<what success looks like concretely>

## What we're NOT doing
<explicit scope boundaries to prevent scope creep>

## Implementation approach
<technical strategy + key decisions (rationale, trade-off, alternative);
patterns to follow with `path:line` references>

## Implementation phases
### Phase 1: <name>
**Objective:** <what this phase accomplishes>
- [ ] <specific task with file path and what changes>
- [ ] ...
**Verification:** <how to confirm this phase>

### Phase 2: <name>
...

## Success criteria
### Automated verification
- [ ] `uv run pytest -q` passes
- [ ] `uv run python -c "import <pkg>"` succeeds
- [ ] file `<path>` exists
### Manual verification
- [ ] <things a human must eyeball>

## Testing strategy
<unit / integration / manual tests to add, and any test-data setup>

## References
- [Research: <topic>](research-<slug>.md)
- [Experiment: <approach>](experiment-<slug>.md) *(if one was run)*
- `path/to/file.py:123` — <why it matters>
```

## Constraints

- **The only file you write is the plan** in `.agents/`. Do not implement
  anything here.
- **No open questions in the final plan.** Resolve every decision (by reading
  code or asking the user) before finalizing.
- Success criteria MUST be split into **Automated** (runnable commands / file
  checks) and **Manual** (human judgment). This split is what makes `/validate`
  possible.
- Be specific: "add JWT validation in `auth.py:45` following `session.py:23`",
  not "add authentication".

Next phase: `/implement` executes this plan; `/validate` checks it.
