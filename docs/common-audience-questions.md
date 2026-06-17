# Common Audience Questions

A single place for the audience questions instructors are most likely to field,
with short, deliverable answers. Organized by block and grounded in each block's
`slides.md`. Use these as quick reference during Q&A; they intentionally repeat
the framing from the slides so you can answer without flipping back.

> These were consolidated out of the per-block `instructor-notes.md` files so
> there's one list to skim before you present.

---

## Block 1: The AI Coding Agent Landscape

| Question | Short answer |
|---|---|
| Isn't this just fancy autocomplete? | No. The models are mostly the same as 18 months ago. What changed is the **loop** wrapped around them, the 'harness' that lets the model read the codebase, plan, edit files, run tests, and iterate. This workshop is mostly about that loop. |
| Which tool should I use: Copilot, Claude Code, Cursor, OpenCode...? | It depends on **your constraints**, not on benchmarks. Weigh cost (subscription vs metered API vs self-hosted), capability, integration (IDE vs CLI vs cloud), model hosting, and privacy. For science, model hosting and privacy usually matter more than they do in industry. |
| If I learn one tool, do I have to relearn everything for the next one? | No. They're the same six pieces (LLM backbone, agent loop, tools, project memory, MCP servers, skills/prompts), just with different wrappers. Once you understand the pieces, switching tools is mostly a config exercise. |
| What is MCP? | Model Context Protocol. A standard way to plug external data sources and tools into any agent without rewriting the agent. It's how you extend what tools an agent can reach. |
| What's the difference between `AGENTS.md`, `copilot-instructions.md`, and `.cursor/rules`? | Same concept, **project memory** loaded into the system prompt, just a different filename per tool. It's where you put conventions every chat should know. |
| Where does my code and data go when I use an agent? | To whoever hosts the model. Always ask: who hosts it, is the data governed (human subjects, PII, IRB, HIPAA), is it licensed or proprietary, and is it logged or trained on? Enterprise and proxy tiers usually don't retain or train; consumer tiers often do. |
| Can I use an agent on sensitive or restricted data? | Match the **model hosting** to the **sensitivity of the data**. When in doubt, don't send it as context. A redacted snippet or a synthetic sample is often enough for the agent to help. The workshop's LLM proxy is deliberate: it keeps requests inside a controlled gateway rather than a consumer endpoint. |
| Do I need a paid Copilot subscription to follow along? | Not here. The Codespace ships a custom OAI-compatible Copilot extension pointed at the workshop's gateway, so you pick the workshop's models in the picker with no subscription. |

---

## Block 2: How It Actually Works (Post-Training & Tool Calling)

| Question | Short answer |
|---|---|
| What's the difference between a base model and the model I actually use? | A **base** (pre-trained) model just predicts the next token. It's a fluent autocomplete with no notion of following instructions, stopping, or calling tools. Everything that makes a coding agent *useful* is added in **post-training** (SFT, RLHF, tool-use FT). |
| Why does it follow my instructions at all? | Supervised fine-tuning (SFT) on `(prompt, ideal response)` pairs. It learns the *format* of 'user asks, assistant answers' instead of pattern-matching the prompt. That's the Q1 answer. |
| Why does it stop when done instead of rambling or looping? | RLHF. It learned from human preference labels what counts as helpful, when to refuse, and when it's done enough to stop. 'Knowing when to stop' is a learned preference, not a hard rule. That's the Q2 answer. |
| Why does it actually *call* a tool instead of just describing what it would do? | Tool-use fine-tuning on traces that include tool calls. It learns both the **wire format** (emit valid JSON tool calls) and the **meta-skill** (when to call a tool vs answer directly). That's the Q3 answer. |
| Is RLHF the same as Constitutional AI? | Constitutional AI is a *variant* of RLHF where the preferences come from a model graded against a written constitution, not from human raters. Same shape, less human labor. |
| What's the difference between RLHF and DPO? | DPO skips the explicit reward model and directly optimizes the policy from preference pairs. Often equally effective, much simpler to implement. |
| What's agentic RL exactly? | Reinforcement learning where the trajectory is multi-turn tool use and the reward is task completion (e.g., 'did the tests pass?'). It's how recent agent products got reliably good at long workflows. |
| Why do all the models behave so similarly? | Anthropic, OpenAI, Google, Meta, and DeepSeek all run a similar pipeline with different data and reward signals. Train very different models toward overlapping skills and they converge on overlapping behaviors, which is why `MODEL = "..."` is just a swappable string. That's the Q4 answer. |
| Will GPT / Claude / Gemini eventually all be the same? | The shape of behavior is converging fast. The remaining differences are speed, cost, and the few capabilities each lab over-invests in. Expect the model layer to feel like a commodity within a couple of years. |
| Should I fine-tune for my codebase? | Almost never to start. Try prompt and tool-schema iteration first (that's Block 4). Fine-tuning is a heavier, later step for behavior the prompt genuinely can't reach. |
| What's a token, and how big is the context window? | A token is roughly ¾ of a word (or a few characters of code). Windows are large (~100K to 1M tokens) but not infinite, and agent runs fill them fast. One big file read or a noisy traceback can cost thousands of tokens. |
| When my agent misbehaves, how do I think about fixing it? | Ask: is this a **training problem** (the model just can't do this) or a **prompt problem** (it could if I told it better)? The prompt side (system message, `AGENTS.md`, tool schemas, task description, loaded docs) is the only lever you control. |

---

## Block 3: Agent-Driven Research Software Engineering

| Question | Short answer |
|---|---|
| Where do these skills come from? | They're seven markdown files in `.github/skills/`: `profile-dataset/SKILL.md`, `plan-analysis/SKILL.md`, and so on. Each is frontmatter (name, description, tools) plus a templated prompt. We ship them in-repo so the whole workshop stays in one tool. |
| Do I invoke a skill by name, or does the agent pick it? | Both. The `description`'s `Use when…` clause is what the agent matches a generic ask against. Naming the skill (`/plan-analysis`) is just the explicit version, handy for a live demo. |
| Do I have to run all seven skills every time? | No, pick the pattern. Full study: profile → plan → explore → test → draft → validate. Already know the data: plan → test. Quick look: just `explore-data`, or chat against `AGENTS.md`. |
| Did the agent pick the right statistical test? | That's the whole point of `plan-analysis` + `validate-analysis`. The demo's design is within-subjects, so the answer is a repeated-measures or Friedman family. An independent t-test or one-way ANOVA is the trap, and `validate-analysis` is what catches it. |
| Can the agent's plan just be wrong? | Often. Hand-edit the plan (it's plain markdown) or re-run `plan-analysis`. And `validate-analysis` is non-optional for anything you'd put in a paper. |
| How do I carry context across a long session? | Run the `handoff` skill. It writes a self-contained markdown doc to `docs/`, then you start a fresh chat pointed at that file. That's the context-compaction lever from the failure-mode slide. |
| What goes in `AGENTS.md`? | Your research context: study design ('this is within-subjects'), stats conventions ('alpha = .05', 'always report effect size'), 'never invent citations', file-format conventions, pipeline DAGs. It's the one file you'll edit most, and it's portable across tools. |
| What's the difference between fast and durable mode? | Same agents, same skills, different dial. Fast = exploratory spikes, chat against `AGENTS.md`, throwaway. Durable = an analysis headed for a paper, all phases, `validate-analysis` non-negotiable. Pick the loop length to match the half-life of the result. |
| What is prompt injection, and should I worry about it for research? | The agent follows instructions in *everything* it reads and can't fully separate yours from instructions buried in content (a README, a web page, even a CSV header). Mitigate with read-only skills for untrusted data, no auto-approve on edits or shell, and treating agent output as untrusted until you've read it. |
| How do I stay in control of an agent that edits my files? | git is your safety net. Commit before you start, read the diff (not the 'Done!' chat) to see exactly what changed, commit the `docs/` artifacts alongside the code, and commit per phase so a bad later phase rolls back cleanly. `git log docs/` becomes an auditable lab notebook. |
| Could I run this same workflow in Claude Code or Cursor? | Yes. The *pattern* (named skills, markdown artifacts in `docs/`) is portable; the file format differs per tool. We keep everything in Copilot Chat here for consistency. |

---

## Block 4: Build Your Own Skill

| Question | Short answer |
|---|---|
| What's the difference between a custom agent and a prompt file? | Custom agent = persistent persona for the whole conversation, picked from the agent dropdown. Prompt file = one-shot `/slash` command. Use prompt files for repeated quick actions, agents for sustained tasks. |
| What's a skill, then? | A skill is a folder (`.github/skills/<name>/SKILL.md`) that can bundle scripts and resources, loaded on demand. Use it for a multi-step capability, not a single prompt. See the Block 3 research-loop skills. |
| Which primitive should I reach for? | Pick the smallest one that does the job, usually a prompt file or a skill, not a whole agent. They compose: an agent (`research-data-scientist`) can drive the seven skills in order. |
| Can I have multiple agents active at once? | One at a time per chat. But you can switch mid-conversation, and agents can hand off to each other. |
| Does the agent use the LiteLLM proxy? | Yes. Copilot uses the same env vars regardless of agent. The model you see in the picker comes from your Copilot settings. |
| Can I use this with another tool (Cursor, Claude Code)? | Yes. They have their own equivalents (Cursor rules and modes, Claude Code skills). The pattern transfers; the file format differs slightly. We keep the whole workshop in Copilot Chat for consistency. |
| Where do I save the agent to use it on my own repo? | Same place: `.github/agents/<name>.agent.md` in that repo. The file is portable; commit it and your collaborators get it too. |
| How do I test an agent without running a real query? | You can't, really. The iteration loop is: edit prompt → reload → run → observe → edit. Same as prompt engineering anywhere. |
| My agent doesn't appear in the picker. What's wrong? | Check the filename is `*.agent.md` in `.github/agents/`, then run **Developer: Reload Window**. If it loads but errors, it's usually a YAML frontmatter problem: missing quotes around the description or a malformed `tools` list. |
| My agent runs but does the wrong thing. | Almost always the system-prompt steps are too vague. Tighten step 1, add a 'What you do NOT do' constraint, and if it loops, add 'After at most 5 tool calls, summarize and stop.' |
