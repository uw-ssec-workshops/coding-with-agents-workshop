# Block 3: Further Reading

A small, curated list. Optimized for *applying* what we just demoed
(structured workflows, failure mode awareness) to real research code.

## The workflow we used

- **[`.github/prompts/`](../../.github/prompts/)**: the seven prompt files that make up the research loop — `research`, `plan`, `iterate-plan`, `experiment`, `implement`, `validate`, `handoff` (`.prompt.md` each). The demo runs four of them; all seven ship in-repo, no plugin to install. Each is a templated Copilot Chat slash command — read them as the reference for Block 4.
- **[`rse-plugins`](https://github.com/uw-ssec/rse-plugins)**: the research-plan-implement-validate workflow our prompt files are adapted from, built by the [UW Scientific Software Engineering Center](https://escience.washington.edu/software-engineering/ssec/). The upstream version is a Claude Code / Copilot CLI plugin; we reimplemented its commands and artifact templates as in-repo Copilot prompt files. Read its source for the original (and richer) per-phase guidance.

## Conventions for scientific Python packages

- **[Scientific Python project guidelines](https://scientific-python.org/specs/)**: the SPECs (recommendations on package layout, build systems, deprecation policy, version support) that the demo's `AGENTS.md` references. The single best place to send a scientist who's about to make their first installable package.
- **[Scientific Python development guide](https://learn.scientific-python.org/development/)**: the practitioner-facing companion: how to set up tests, CI, type checking, docs.
- **[`pyOpenSci` packaging guide](https://www.pyopensci.org/python-package-guide/)**: alternative perspective with a stronger emphasis on community review and onboarding new contributors.

## On agent failure modes

- **[Cognition AI: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: sober counterpoint to the "let's build a swarm" instinct. Reinforces "agents are coworkers, not magic."
- **[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: read this once a year. The vocabulary in the workshop comes mostly from here.
- **[Aider: How to use Aider effectively](https://aider.chat/docs/usage/tips.html)**: pragmatic field notes from one of the longest-running OSS coding agents. The "tips" page is concentrated wisdom about scope, prompts, and when to intervene.

## On the use cases tour

- **[GitHub: Copilot best practices for research](https://docs.github.com/copilot)**: official docs. Skip the marketing; look at the "tips" sub-pages.
- **[Software Carpentry / Code Refinery](https://software-carpentry.org/lessons/)**: not agent-specific, but the practices that *make agent-driven development work* (small commits, tests, version control hygiene) are exactly what these lessons teach.

## Companion to the demo

The team behind `rse-plugins` wrote a
[handout](https://github.com/uw-ssec/rse-plugins) and a 4-minute
[demo script](https://github.com/uw-ssec/rse-plugins), both of which
informed this block. They're useful as condensed reference if you want
the workflow without the workshop framing.

---

If you find a great resource that should be here, open a PR.
