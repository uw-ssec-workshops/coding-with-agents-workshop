# Dataset profile: text-entry study

> **Note:** Hand-crafted sample artifact, used as a live-demo fallback if the live
> `profile-dataset` skill misbehaves on the day. It is shaped like a real artifact
> so attendees can study it as a reference.

## Summary

A synthetic within-subjects HCI experiment. 30 participants each typed on three
on-screen keyboard interfaces (`qwerty`, `swipe`, `predictive`); we recorded
typing speed (`wpm`) and error rate. The data is long/tidy — **one row per
participant × interface** — so each participant contributes three rows. The unit
of observation is a single typing session.

## Shape & structure

- 90 rows × 5 columns. Long format. 30 participants × 3 interfaces = 90.
- First line of `data.csv` is a `#` comment (skipped by `comment="#"` /
  `skiprows=1`).

## Columns

| column | dtype | meaning | range / levels | missing |
|---|---|---|---|---|
| `participant_id` | str | participant label, repeated-measures key | `P01`–`P30` (3 rows each) | none |
| `interface` | categorical | keyboard condition | `qwerty`, `swipe`, `predictive` (30 each) | none |
| `presentation_order` | int | order this interface was shown | 1–3 (counterbalanced) | none |
| `wpm` | float | typing speed (primary outcome) | ~9.8–50.0 | none |
| `error_rate` | float | fraction of chars corrected (secondary) | ~0.00–0.31 | none |

## Study design (as stated in AGENTS.md)

- **Within-subjects / repeated measures:** every participant uses all three
  interfaces → the three rows per participant are paired, *not* independent.
- Factor `interface` (3 levels). Primary outcome `wpm`, secondary `error_rate`.
- H0: no difference in `wpm` across interfaces. H1: at least one differs.

## Observations a plan must account for

- **Rows are not independent** — repeated measures on `participant_id`. The
  analysis must use a within-subjects / paired test family.
- **A likely outlier:** participant `P07` on `swipe` has `wpm = 9.8`, far below the
  rest of the swipe distribution (the AGENTS.md notes a "dropped stylus" scenario).
  This will matter for the normality assumption.
- `presentation_order` is present, so an order/learning effect can be sanity-checked.

## References

- `starter/data.csv` — the dataset (load with `comment="#"`).
- `AGENTS.md` — study design, hypotheses, and analysis conventions.
