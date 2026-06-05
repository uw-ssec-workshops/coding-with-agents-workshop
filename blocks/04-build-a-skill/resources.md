# Block 4: Further Reading

Curated. The first three are the docs you'll actually need; everything
else is "going further."

## The primitives we used

- **VS Code: [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)**: the official docs for the file format we just used (`.agent.md`). These were previously called "custom chat modes" (`.chatmode.md`) — same idea, current name. Bookmark this.
- **VS Code: [Prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)**: the simpler primitive (slash commands). Use these for repeated one-shot actions where a full custom agent is overkill. See `.github/prompts/` for worked examples.
- **VS Code: [Agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)**: a folder (`.github/skills/<name>/SKILL.md`) that bundles instructions, scripts, and resources for a multi-step capability, loaded on demand. See `.github/skills/experiment-log/`.
- **GitHub: [Custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses)**: `.github/copilot-instructions.md` is the project-wide equivalent of `AGENTS.md`; `.github/instructions/*.instructions.md` are path-scoped (an `applyTo` glob). Use them for conventions every chat should know about.

## Going further with Copilot

- **GitHub: [MCP for Copilot](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp)**: the next step up if you want to give Copilot brand-new tools (read from your database, query an internal API, etc.). Higher ceiling, more setup.
- **Anthropic: [Model Context Protocol](https://modelcontextprotocol.io/)**: the underlying open standard. Worth understanding if you want your tools to work in Copilot AND Claude Code AND Cursor.

## The same idea in other tools

- **Anthropic: [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)**: custom agents' closest cousin in Claude Code. The `rse-plugins` workflow that inspired Block 3 is built from these.
- **Cursor: [Custom rules and modes](https://docs.cursor.com/)**: for participants who use Cursor day-to-day.
- **Aider: [Conventions and prompts](https://aider.chat/docs/usage/conventions.html)**: the OSS alternative; same patterns, smaller surface area.

## Inspiration: full agent workflows built on these primitives

- **[`rse-plugins`](https://github.com/uw-ssec/rse-plugins)**: the research-plan-implement workflow Block 3's prompt files are adapted from. Read its source to see how the six-phase workflow is built from skills; we reimplemented its commands as Copilot prompt files in `.github/prompts/`.
- **[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: the most-quoted paper on agent design patterns. Read once a year.
- **[Cognition: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: the counter-cultural pushback. Worth reading before you build something baroque.

## Office hours and follow-up

- This workshop's repository is yours to keep. Fork it; bring your custom agents home.
- Office hours next day: come with the code or data you actually want to use this on.
- Mailing list for ongoing community: ask the workshop organizers, exact link to be confirmed.

---

If you find a great resource that should be here, open a PR.
