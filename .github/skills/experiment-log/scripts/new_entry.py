"""Append a structured experiment entry to a markdown lab notebook.

Bundled helper for the `experiment-log` agent skill. Keeping the formatting in
a tiny script (rather than asking the model to format prose every time) is the
whole point of a skill shipping its own assets: the entries stay consistent and
the agent just supplies the fields.

Usage
-----
uv run python .github/skills/experiment-log/scripts/new_entry.py \
    --notebook LAB_NOTEBOOK.md \
    --run-id 2026-06-03-baseline \
    --metric "val_loss=0.183 (best 0.171 @ epoch 12)" \
    --params "lr=3e-4, batch=64, seed=0" \
    --status success \
    --note "Baseline run." \
    --next "Try lr=1e-3."
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

STATUSES = ("success", "diverged", "crashed")

_NOTEBOOK_HEADER = "# Lab notebook\n\nAppend-only log of experiment runs. Newest entries at the bottom.\n"


def render_entry(
    run_id: str,
    metric: str,
    params: str,
    status: str,
    note: str,
    next_steps: str,
    when: date | None = None,
) -> str:
    """Render a single notebook entry as a markdown block.

    Parameters
    ----------
    run_id : str
        Identifier for the run (often a date-prefixed slug).
    metric : str
        Headline metric(s), final and best.
    params : str
        The parameters that differ from the project defaults.
    status : str
        One of ``"success"``, ``"diverged"``, or ``"crashed"``.
    note : str
        One or two sentences on what was tested and learned.
    next_steps : str
        What to try next.
    when : datetime.date, optional
        Entry date. Defaults to today.

    Returns
    -------
    str
        A markdown block ending in a blank line.
    """
    when = when or date.today()
    return (
        f"### {when.isoformat()} — {run_id}  [{status}]\n"
        f"- **Params:** {params}\n"
        f"- **Result:** {metric}\n"
        f"- **Note:** {note}\n"
        f"- **Next:** {next_steps}\n\n"
    )


def append_entry(notebook: Path, entry: str) -> None:
    """Append ``entry`` to ``notebook``, creating the file with a header if needed."""
    if not notebook.exists():
        notebook.write_text(_NOTEBOOK_HEADER + "\n", encoding="utf-8")
    with notebook.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notebook", type=Path, default=Path("LAB_NOTEBOOK.md"))
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--metric", required=True)
    parser.add_argument("--params", default="(defaults)")
    parser.add_argument("--status", choices=STATUSES, default="success")
    parser.add_argument("--note", default="")
    parser.add_argument("--next", dest="next_steps", default="")
    args = parser.parse_args()

    entry = render_entry(
        run_id=args.run_id,
        metric=args.metric,
        params=args.params,
        status=args.status,
        note=args.note,
        next_steps=args.next_steps,
    )
    append_entry(args.notebook, entry)
    print(f"Appended entry for {args.run_id!r} to {args.notebook}")


if __name__ == "__main__":
    main()
