# Block 3: Further Reading

A small, curated list. Optimized for *applying* what we just demoed
(structured workflows, failure mode awareness) to real research code.

## The plugin we used

- **[`rse-plugins`](https://github.com/uw-ssec/rse-plugins)**: the Claude Code plugin we demoed live. Source code, install instructions, and per-command documentation. Built by the [UW Scientific Software Engineering Center](https://escience.washington.edu/software-engineering/ssec/).

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

The teammate who originally wrote the rse-plugins demo wrote a
[handout](https://github.com/uw-ssec/rse-plugins) and a 4-minute
[demo script](https://github.com/uw-ssec/rse-plugins), both of which
informed this block. They're useful as condensed reference if you want
the workflow without the workshop framing.

---

If you find a great resource that should be here, open a PR.
