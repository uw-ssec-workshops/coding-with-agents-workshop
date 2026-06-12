"""Generate the synthetic HCI text-entry dataset for the Block 3 demo.

This is *demo scaffolding*, not the thing the agent analyzes. It produces
``data.csv``: a within-subjects (repeated-measures) study in which every
participant types on all three on-screen keyboard interfaces. Re-running this
script with the same seed reproduces the committed CSV exactly.

Design baked in on purpose (these are the teaching traps):

* Within-subjects -> rows are NOT independent. An independent-samples test
  (one-way ANOVA / Welch t-test) is the wrong family here.
* ``wpm`` is right-skewed with one injected outlier, so the normality
  assumption of a repeated-measures ANOVA fails -> the analysis should fall
  back to the Friedman test + Wilcoxon signed-rank post-hoc.
* Three conditions -> pairwise post-hoc needs multiple-comparison correction.

Run:  uv run python make_data.py
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
N_PARTICIPANTS = 30
INTERFACES = ("qwerty", "swipe", "predictive")

# Mean words-per-minute per interface (qwerty fastest, predictive slowest).
INTERFACE_WPM = {"qwerty": 42.0, "swipe": 38.0, "predictive": 34.0}
# Mean character-correction rate per interface (predictive auto-corrects most).
INTERFACE_ERR = {"qwerty": 0.04, "swipe": 0.07, "predictive": 0.05}

OUTPUT = Path(__file__).resolve().parent / "data.csv"
HEADER_COMMENT = (
    "# Synthetic data for the 'Coding with AI Agents' workshop "
    "(Block 3, HCI text-entry study). Not real participants. "
    "Load with pandas.read_csv(comment='#') or skiprows=1."
)


def build() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)

    # Per-participant typing skill (random intercept): induces the
    # within-participant correlation that makes the data repeated-measures.
    skill = rng.normal(0.0, 6.0, size=N_PARTICIPANTS)

    # Counterbalance the order each participant sees the interfaces in: cycle
    # through the 6 possible orderings so order is roughly balanced.
    orderings = list(itertools.permutations(INTERFACES))

    rows: list[dict[str, object]] = []
    for p in range(N_PARTICIPANTS):
        pid = f"P{p + 1:02d}"
        order = orderings[p % len(orderings)]
        for interface in INTERFACES:
            base = INTERFACE_WPM[interface] + skill[p]
            # Right-skewed positive noise (gamma) so distributions are not normal.
            noise = rng.gamma(shape=2.0, scale=1.6) - 3.2
            wpm = base + noise
            err = float(
                np.clip(rng.normal(INTERFACE_ERR[interface], 0.015), 0.0, 0.4)
            )
            rows.append(
                {
                    "participant_id": pid,
                    "interface": interface,
                    "presentation_order": order.index(interface) + 1,
                    "wpm": round(float(wpm), 1),
                    "error_rate": round(err, 3),
                }
            )

    df = pd.DataFrame(rows)

    # Inject one clear outlier: P07 has a disastrous run on the swipe keyboard
    # (a dropped stylus). This is what should fail the normality check.
    mask = (df["participant_id"] == "P07") & (df["interface"] == "swipe")
    df.loc[mask, "wpm"] = 9.8
    df.loc[mask, "error_rate"] = 0.31

    return df


def main() -> None:
    df = build()
    with OUTPUT.open("w", newline="") as fh:
        fh.write(HEADER_COMMENT + "\n")
        df.to_csv(fh, index=False)
    print(f"wrote {len(df)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
