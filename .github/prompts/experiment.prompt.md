---
agent: agent
description: 'Compare 2-3 approaches with real prototype code and write an evidence-based recommendation to .agents/.'
tools: ['read', 'edit/editFiles', 'search/codebase', 'search', 'execute/runInTerminal']
---

# Experiment (optional: compare approaches)

**Optional** phase — use only when the best approach is genuinely uncertain. Try
multiple approaches with real code, record honest observations, and recommend one.

What to compare: `${input:question:the decision to resolve, e.g. "argparse vs click for the vscm CLI"}`.

## Principles

- **Actually run code.** Write minimal prototypes and execute them — don't
  theorize. Use a scratch dir (`.experiments/<slug>/`) or a throwaway branch.
- **Be honest about trade-offs.** Every approach has downsides; document failures
  as well as successes. Don't cherry-pick.
- **Stay focused.** 2-3 _distinct_ approaches (architectural differences, not
  config tweaks). Test one decision at a time.

## Steps

1. Read any related `.agents/research-*.md` / `.agents/plan-*.md` completely.
2. State the hypothesis and per-approach success criteria.
3. For each approach: describe it (pros/cons/complexity), write a prototype, run
   it, and record observations (what worked, what didn't, metrics).
4. Build a comparison matrix and make a clear, honest recommendation.
5. Write the artifact to `.agents/experiment-<slug>.md`.

## Artifact structure (`.agents/experiment-<slug>.md`)

```
# Experiment: <question>

## Goal & hypothesis
<the question, why it matters, expected outcome, success criteria>

## Approaches
### Approach 1: <name>
- Description / Pros / Cons / Complexity (Low|Med|High)
### Approach 2: <name>
...

## Experiments run
### Approach 1
- Code tested: `path` or snippet
- Execution: `<commands>`
- Results: ✅ worked / ❌ didn't / ⚠️ caveat
- Metrics: <latency, LOC, deps, ...>

## Comparison matrix
| Criterion | Approach 1 | Approach 2 | Approach 3 |
|---|---|---|---|
| Performance | ... | ... | ... |
| Complexity | ... | ... | ... |
| Maintainability | ... | ... | ... |
| Integration ease | ... | ... | ... |

## Key insights & failed assumptions
<what you learned, surprises>

## Recommendation
**Use <approach>** because <reason>. Trade-offs accepted: <...>
Why not the others: <...>

## When to use an alternative
If <condition>, prefer <approach> because <reason>.

## References
- [Research: <topic>](research-<slug>.md)
- [Plan: <goal>](plan-<slug>.md)
```

## Constraints

- Keep prototypes out of the real source tree (scratch dir / throwaway branch);
  this phase explores, it does not ship.
- If the answer is obvious from existing patterns, **say so and skip** — don't
  manufacture an experiment.

Next phase: feed the recommendation into `/plan` or `/iterate-plan`.
