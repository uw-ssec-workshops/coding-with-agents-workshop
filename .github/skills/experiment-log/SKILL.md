---
name: experiment-log
description: 'Read an experiment run directory (metrics, config, logs), summarize the run, and append a structured entry to a markdown lab notebook. Use when the user finishes a training run, simulation, or sweep and wants it recorded and compared against previous runs.'
---

# Experiment log

This skill turns a finished run into a durable, comparable lab-notebook
entry. It is the **experiment management** phase of the research lifecycle:
the loop of *launch → read results → write down what happened → decide the
next run*.

Unlike a one-shot prompt, a skill can bundle helper scripts and resources.
This one ships a small formatter (`scripts/new_entry.py`) so the notebook
entries are always shaped the same way.

## When to use this skill

Use it when a run has produced output on disk — a directory with some mix of
`config.{json,yaml}`, `metrics.{json,jsonl,csv}`, `stdout.log`, checkpoints —
and the user wants it (a) summarized and (b) recorded in a lab notebook for
later comparison.

## Inputs

- **run directory**: the folder for the run to log (e.g. `runs/2026-06-03-baseline/`).
- **notebook path** (optional): the markdown lab notebook to append to.
  Default: `LAB_NOTEBOOK.md` at the repo root (create it if missing).

## Steps

1. **Read the run.** List the run directory. Read the config file, the metrics
   file, and the tail of any log. Do not load gigabyte checkpoints — read
   metadata only.
2. **Extract the essentials**: run name/id, date, key hyperparameters that
   differ from defaults, headline metrics (final + best), wall-clock or steps,
   and whether it succeeded, diverged, or crashed.
3. **Compare to history.** Read the existing notebook. If prior entries exist,
   say how this run compares to the most relevant one (better/worse on the
   headline metric, and by how much).
4. **Write the entry.** Append a dated, structured entry to the notebook. You
   may either write the markdown directly, or — to keep formatting consistent —
   call the bundled script:

   ```bash
   uv run python .github/skills/experiment-log/scripts/new_entry.py \
     --notebook LAB_NOTEBOOK.md \
     --run-id 2026-06-03-baseline \
     --metric "val_loss=0.183 (best 0.171 @ epoch 12)" \
     --params "lr=3e-4, batch=64, seed=0" \
     --status success \
     --note "Baseline. Beats last week's run (0.20) by ~9%."
   ```

5. **Confirm and suggest next.** Show the appended entry and propose the next
   1-3 runs worth trying, with a one-line hypothesis for each.

## Constraints

- Append only. **Never rewrite or delete** existing notebook entries — the lab
  notebook is an audit trail.
- Do not invent metrics. If a number is not in the run output, mark it `?`.
- Keep each entry scannable: a human should grasp the run in ~10 seconds.
- If the run directory is ambiguous or missing the files you need, ask the
  user which directory and what the headline metric is before writing.

## Entry format

```
### <date> — <run-id>  [success | diverged | crashed]
- **Params:** <only what differs from defaults>
- **Result:** <headline metric, final + best>
- **vs previous:** <comparison, or "first run">
- **Note:** <one or two sentences: what you were testing, what you learned>
- **Next:** <what to try next>
```
