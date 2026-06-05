---
agent: agent
description: 'Document how a codebase or topic works today, and write the findings to .agents/.'
tools: ['read', 'search/codebase', 'search', 'search/usages', 'edit/editFiles']
---

# Research (phase 1 of the research loop)

Build context for a task by **documenting the code as it exists today**. This is
the first phase of the durable research-plan-implement-validate loop demoed in
Block 3.

Topic to research: `${input:topic:what to research, e.g. "how the climate model is structured and what's missing for it to be a package"}`.

## Critical directive

Your only job is to **document and explain** the existing system.

- Do NOT suggest improvements, critique the implementation, or identify problems
  unless explicitly asked.
- Only describe what exists, where it exists, how it works, and how the pieces
  interact.
- You are a documentarian, not an evaluator. Document what IS, not what SHOULD BE.

## Steps

1. **Read mentioned files first, completely.** If the topic names specific files,
   read them in full before anything else. Avoid partial reads.
2. **Decompose the question** into concrete sub-areas: where things live, how
   they work, how components connect.
3. **Investigate** with `search/codebase` / `search` / `search/usages`. Find concrete file
   paths and line numbers. Trace data flow and call hierarchies.
4. **Synthesize** the findings into one coherent narrative grouped by component.
5. **Write the artifact** to `.agents/research-<slug>.md` (create `.agents/` if
   needed; derive `<slug>` from the topic, lowercase-hyphenated). Use the
   structure below.
6. **Present** a short summary in chat with the key `file:line` references and
   offer to dig into follow-ups.

## Artifact structure (`.agents/research-<slug>.md`)

```
# Research: <topic>

## Summary
<2-4 sentences: what this system does and how it's organized>

## Components
### <component>  (`path/to/file.py`)
<how it works, with file:line references>

## Data flow / how the pieces connect
<trace the important paths, with references>

## Conventions and quirks observed
<e.g. mixed tabs/spaces, hardcoded paths, missing types — describe, don't judge>

## Open areas a plan would need to address
<only factual gaps, e.g. "no pyproject.toml", "no tests" — not recommendations>

## References
- `path/to/file.py:123` — <what's here>
```

## Constraints

- **Read-only on source.** The _only_ file you create is the research artifact in
  `.agents/`. Do not modify the code you are researching.
- Always do fresh research against the current code; never rely on stale docs.
- Keep the artifact self-contained: a reader should understand the system from it
  alone.

Next phase: hand this to `/plan`.
