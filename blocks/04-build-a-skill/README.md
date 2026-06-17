# Block 4: Build Your Own Skill (Capstone)

## Learning goals

By the end of this block, an attendee can:

1. Read a Copilot custom agent file and identify which line corresponds to which **anatomy concept** from Block 1 (LLM backbone, tool use, project memory, system prompt).
2. **Write** a custom agent end-to-end: pick a job, write a focused system prompt, choose a narrow tool list, save it to `.github/agents/`, and invoke it.
3. **Iterate** on an agent that almost works: tighten the prompt, add explicit constraints, narrow or broaden the tool list.
4. Map the same agent pattern to **other primitives** (Copilot prompt-file commands for one-shots, like `eda-summary` or `scaffold-package`; skills for multi-step capabilities, like the Block 3 research loop; MCP servers if they want to add new tools).

## What's in this folder

```
04-build-a-skill/
  README.md            # this file
  slides.md            # Marp slides
  instructor-notes.md  # speaker notes
  resources.md         # Copilot custom-agent docs, prompt files, skills, MCP
  exercise/
    README.md                            # participant-facing step-by-step
    my-agent.agent.md.template           # SKELETON to copy + fill in (the main task)
    my-prompt.prompt.md.template         # SKELETON for a prompt-file command (stretch B)
    my-skill.SKILL.md.template           # SKELETON for a skill (stretch A)
    my-instruction.instructions.md.template  # SKELETON for path-scoped instructions
    ideas.md                             # 30+ starter agent ideas
```

### Run the exercise

Participants follow [`exercise/README.md`](exercise/README.md). Instructors
circulate. The exercise's troubleshooting table covers the common
"my agent doesn't appear" / "agent runs but does the wrong thing" issues.
