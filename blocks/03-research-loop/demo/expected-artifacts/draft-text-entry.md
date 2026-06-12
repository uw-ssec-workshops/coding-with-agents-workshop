# Draft: text-entry interface comparison

> **Note:** Hand-crafted sample artifact (live-demo fallback for the `draft-report`
> skill). Every number traces to [test-text-entry.md](test-text-entry.md). The
> `[CITATION NEEDED]` markers are intentional — the skill must never fabricate
> references.

## Methods

**Participants.** Thirty participants (P01–P30) completed the study. Each
participant contributed data for all three interface conditions.

**Design.** We used a within-subjects design with a single factor, *interface*,
at three levels: a standard on-screen QWERTY keyboard (`qwerty`), a gesture-typing
keyboard (`swipe`), and a keyboard with aggressive word prediction (`predictive`).
Presentation order was counterbalanced across participants to mitigate learning
and fatigue effects.

**Apparatus and measures.** For each interface, participants transcribed
standardized phrases. The primary measure was typing speed in words per minute
(`wpm`); character correction rate (`error_rate`) was recorded as a secondary
measure [CITATION NEEDED: standard text-entry evaluation protocol].

**Analysis.** Because the design is within-subjects, the three measurements per
participant are not independent, so we used repeated-measures methods. We assessed
normality of `wpm` within each interface using the Shapiro–Wilk test
[CITATION NEEDED: Shapiro & Wilk]. Normality was violated for the `swipe`
condition (W = 0.79, p < .0001), driven by one extreme low-speed session, so we
used the non-parametric **Friedman test** [CITATION NEEDED: Friedman] for the
omnibus comparison and **Wilcoxon signed-rank tests** for pairwise follow-ups,
with **Holm correction** for multiple comparisons [CITATION NEEDED: Holm]. We
report Kendall's W and matched-pairs rank-biserial correlations as effect sizes.
Alpha was .05.

## Analysis / Results

Typing speed differed significantly across the three interfaces (Friedman χ²(2) =
45.19, p < .001, Kendall's W = 0.75), a large effect indicating that participants
ranked the interfaces consistently. Descriptively, mean typing speed was highest
for QWERTY (M = 41.4 wpm), intermediate for swipe (M = 36.7), and lowest for
predictive (M = 34.5).

All three pairwise comparisons remained significant after Holm correction. QWERTY
was faster than swipe (Holm-adjusted p < .001, rank-biserial = +0.94) and faster
than predictive (adjusted p < .001, rank-biserial = +1.00), and swipe was faster
than predictive (adjusted p < .001, rank-biserial = +0.70). The ordering of typing
speed was therefore QWERTY > swipe > predictive.

These results are consistent with the manipulated interface affecting typing
speed within this sample. We do not make claims beyond the three interfaces tested.
[TODO: report the secondary error_rate analysis if it is in scope.]
