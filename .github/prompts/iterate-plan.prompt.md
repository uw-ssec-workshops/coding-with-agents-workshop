---
agent: agent
description: 'Refine an existing plan in .agents/ with surgical edits based on feedback.'
tools: ['read', 'search/codebase', 'search', 'search/usages', 'edit/editFiles']
---

# Iterate Plan (refine an existing plan)

Update an existing implementation plan based on feedback or changed
requirements — **surgically**, without rewriting what already works.

Plan + changes: `${input:request:plan path and what to change, e.g. ".agents/plan-vscm-package.md split the CLI phase into two"}`.
If no plan path is given, list `.agents/plan-*.md` and ask which to edit.

## Iteration philosophy

- **Surgical** — precise edits to the sections that change; leave the rest alone.
- **Consistent** — new content matches the existing phase format and detail level.
- **Verified** — if a change introduces new technical requirements, read the code
  to ground it; don't guess at file paths or patterns.
- **Interactive** — confirm understanding before editing.

## Steps

1. **Read the existing plan completely** (don't edit from memory).
2. **Understand the request:** adding/removing phases, adjusting scope, updating
   success criteria, changing approach, incorporating experiment results,
   splitting a phase, reordering.
3. **Research only if needed** — structural changes (reorder, split) need none;
   new technical requirements need a quick code check.
4. **Confirm the approach** with the user before editing: summarize current
   structure, the proposed change, and what sections it touches.
5. **Make focused edits:**
    - Insert/modify only the affected phases or criteria.
    - Keep `file:line` references accurate (re-check the code if unsure).
    - Preserve the **Automated vs Manual** success-criteria split.
    - If scope grew/shrank, update the **What we're NOT doing** section too.
    - Renumber subsequent phases and fix cross-references if you insert/split.
6. **Report** the changes: what changed, in which sections, and the impact.

## Constraints

- The only file you edit is the plan in `.agents/`. Do not implement code here.
- **No open questions** may remain in the updated plan — resolve them by reading
  code or asking the user before finalizing.
- Don't reformat or rewrite sections that didn't need to change.

Next phase: `/implement` the updated plan.
