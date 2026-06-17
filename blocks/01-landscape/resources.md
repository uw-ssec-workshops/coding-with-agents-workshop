# Block 1: Further Reading

A small, curated list. Optimized for *durable* concepts, not the latest
tool announcement.

## The mechanics

- **Anthropic: [Building effective agents](https://www.anthropic.com/research/building-effective-agents)**: the cleanest explanation of agent loops, tools, and when *not* to use an agent. The vocabulary in our "anatomy of a coding agent" slide comes mostly from here.
- **OpenAI: [Function calling](https://platform.openai.com/docs/guides/function-calling)**: the tool-calling spec that LiteLLM (and the notebook) use. Even when the model is Claude, the wire format is OpenAI's.
- **LiteLLM: [Documentation](https://docs.litellm.ai/)**: the proxy and Python SDK we use. Most useful sections: "completion" (the function we call), "supported providers" (the model aliases you can swap into `MODEL`), and "proxy server" (how we set ours up).
- **Model Context Protocol: [Specification](https://modelcontextprotocol.io/)**: the open standard for plugging tools into agents. We'll build an MCP server in Block 4.

## The products we mentioned

- **GitHub: [Copilot in agent mode](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)**: the official docs for the tool we used in the live demo.
- **Anthropic: [Claude Code](https://docs.claude.com/en/docs/claude-code/overview)**: the CLI agent, popular in research labs that have Anthropic API access.
- **Cursor: [Documentation](https://docs.cursor.com/)**: useful even if you don't use Cursor; their rules and modes docs are well written.

## Project memory

- **[`AGENTS.md` proposal](https://agents.md/)**: the emerging convention for project-level instructions, supported by Claude Code, OpenCode, and others.
- **GitHub: [Custom instructions for Copilot](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses)**: `.github/copilot-instructions.md` and prompt files, the Copilot equivalent.

## When agents fail

- **[Cognition: Don't build multi-agents](https://cognition.ai/blog/dont-build-multi-agents)**: counter-cultural argument that you should keep agents simple, not stack them. Useful framing for Block 3's "common failure modes" discussion.

## On post-training (warm-up for Block 2)

- **OpenAI: [Aligning language models to follow instructions](https://openai.com/index/instruction-following/)**: short, accessible intro to instruction tuning.
- **Anthropic: [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)**: one approach to RLHF; not required reading, but a good companion to Block 2.

---

If you find a great resource that should be here, open a PR.
