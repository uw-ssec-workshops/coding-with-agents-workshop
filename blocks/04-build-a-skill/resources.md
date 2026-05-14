# Block 4: Further Reading

Curated. The first three are the docs you'll actually need; everything
else is "going further."

## The primitives we used

- **GitHub: [Custom chat modes](https://docs.github.com/en/copilot/customizing-copilot/custom-chat-modes)**: the official docs for the file format we just used. Bookmark this.
- **GitHub: [Prompt files](https://docs.github.com/en/copilot/customizing-copilot/prompt-files)**: the simpler primitive (slash commands). Use these for repeated one-shot actions where a full chat mode is overkill.
- **GitHub: [Custom instructions](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses)**: `.github/copilot-instructions.md` is the project-wide equivalent of `AGENTS.md`. Use it for conventions every chat should know about.

## Going further with Copilot

- **GitHub: [MCP for Copilot](https://docs.github.com/en/copilot/customizing-copilot/mcp)**: the next step up if you want to give Copilot brand-new tools (read from your database, query an internal API, etc.). Higher ceiling, more setup.
- **Anthropic: [Model Context Protocol](https://modelcontextprotocol.io/)**: the underlying open standard. Worth understanding if you want your tools to work in Copilot AND Claude Code AND Cursor.

## The same idea in other tools

- **Anthropic: [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)**: chat modes' closest cousin in Claude Code. The Block 3 demo used these (via the `rse-plugins` plugin).
- **Cursor: [Custom rules and modes](https://docs.cursor.com/)**: for participants who use Cursor day-to-day.
- **Aider: [Conventions and prompts](https://aider.chat/docs/usage/conventions.html)**: the OSS alternative; same patterns, smaller surface area.

## Inspiration: full agent workflows built on these primitives

- **[`rse-plugins`](https://github.com/uw-ssec/rse-plugins)**: the Claude Code plugin we demoed in Block 3. Read its source to see how a 6-phase research-plan-implement workflow is built from skills.
- **[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: the most-quoted paper on agent design patterns. Read once a year.
- **[Cognition: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: the counter-cultural pushback. Worth reading before you build something baroque.

## Office hours and follow-up

- This workshop's repository is yours to keep. Fork it; bring your chat modes home.
- Office hours next day: come with the code or data you actually want to use this on.
- Mailing list for ongoing community: ask the workshop organizers, exact link to be confirmed.

---

If you find a great resource that should be here, open a PR.
