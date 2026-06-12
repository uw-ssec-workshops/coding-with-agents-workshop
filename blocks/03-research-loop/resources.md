# Block 3: Further Reading

A small, curated list. Optimized for *applying* what we just demoed
(structured skill workflows, failure-mode awareness) to real research analysis.

## The workflow we used

- **[`.github/skills/`](../../.github/skills/)**: the seven skills that make up the research loop — `profile-dataset`, `plan-analysis`, `explore-data`, `statistical-tests`, `draft-report`, `validate-analysis`, `handoff` (each a `SKILL.md`). They ship in-repo, no plugin to install. Each is a templated Copilot skill the agent can auto-select or you can invoke by name — read them as the reference for Block 4.
- UW SSEC's [`rse-plugins`](https://github.com/uw-ssec/rse-plugins) is a separate, unrelated project that packages similar research-engineering skills as Claude Code plugins.

## Choosing and reporting statistical tests

- **[scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)**: the reference for the tests in the demo — `shapiro`, `friedmanchisquare`, `wilcoxon`, and friends. The module index doubles as a "which test exists?" map.
- **[statsmodels](https://www.statsmodels.org/stable/index.html)**: repeated-measures ANOVA (`AnovaRM`), and `stats.multitest.multipletests` for Holm/Bonferroni correction.
- **[Choosing the right statistical test (UCLA IDRE)](https://stats.oarc.ucla.edu/other/mult-pkg/whatstat/)**: a decision-table for matching a test to your design — exactly the judgment `plan-analysis` is trying to encode. The single best link for "I have this design, what test?"
- **[Lakens, *Calculating and Reporting Effect Sizes*](https://doi.org/10.3389/fpsyg.2013.00863)**: why a p-value alone isn't a result. Effect sizes + CIs are a workshop convention for a reason.

## Analysis in HCI specifically

- **[Cairns, *Doing Better Statistics in Human-Computer Interaction*](https://doi.org/10.1017/9781108685139)**: the practitioner book on getting HCI experiment analysis right (within-subjects designs, non-parametric tests, the mistakes everyone makes).
- **[Transparent Statistics in HCI](https://transparentstats.github.io/guidelines/)**: community guidelines spelling out reviewer expectations (report effect sizes, correct for multiple comparisons, don't dichotomize p). Good for "what will a reviewer want?"

## On agent failure modes

- **[Cognition AI: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: sober counterpoint to the "let's build a swarm" instinct. Reinforces "agents are coworkers, not magic."
- **[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: read this once a year. The vocabulary in the workshop comes mostly from here.
- **[Aider: How to use Aider effectively](https://aider.chat/docs/usage/tips.html)**: pragmatic field notes from one of the longest-running OSS coding agents — concentrated wisdom about scope, prompts, and when to intervene.

## On reproducibility and version control

- **[Software Carpentry](https://software-carpentry.org/lessons/) / [Code Refinery](https://coderefinery.org/lessons/)**: not agent-specific, but the practices that *make agent-driven analysis trustworthy* (small commits, version control hygiene, scripted analyses) are exactly what these lessons teach.
- **[The Turing Way](https://the-turing-way.netlify.app/)**: a community handbook on reproducible research — a good home base for "how should my analysis be organized so someone (or an agent) can re-run it?"

---

If you find a great resource that should be here, open a PR.
