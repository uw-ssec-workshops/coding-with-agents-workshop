---
marp: true
theme: default
paginate: true
size: 16:9
title: 'Block 2 - How It Actually Works'
description: 'Coding with AI Agents - 2026 Interdisciplinary Science Summit'
style: |
    @import "slides.css";
---

<!-- _class: lead -->

# How It Actually Works

## Block 2: Post-Training and Tool Calling

_A primer on why the loop you just saw is even possible._

<!--
Speaker notes:
- 30 seconds. Hand-off from Block 1 demo.
- Set expectation: this block is the most conceptual of the four. Stick with us, by the end you'll have a mental model that outlasts any product release.
-->

---

## Where we left off: four questions

Block 1 ended with an agent that, given one prompt, did four things we mostly took for granted:

- **Q1.** It **followed our instructions** at all. _Why?_
- **Q2.** It **acted helpfully** and **stopped when done** instead of rambling or looping. _Why?_
- **Q3.** It **called `run_bash`** instead of describing what it would do. _Why?_
- **Q4.** The same loop worked with **Claude, GPT, or Gemini**. _Why?_

> None of these are things the model picked up by reading the internet.
> Each has a name in the post-training pipeline.

<!--
Speaker notes:
- Read all four questions slowly. Make eye contact.
- Frame the rest of the block: "we're going to answer Q1 through Q4 in order, each gets one slide."
- This slide is the contract. The next 25 minutes pay it off.
-->

---

## Pre-training: a fluent autocomplete

A **base** large language model is trained to predict the next token in
a corpus of text. That's it. After pre-training, the model is great at
_continuing_ text in the style of what it just read.

What that does NOT give you:

- Following instructions ("write a function" -> base model writes more _prompts_ in the same style)
- Helpful behavior, refusals, knowing when to stop
- Calling tools, the concept doesn't exist in pre-training data
- Stable identity ("you are a helpful assistant", the base model has no idea what that means)

Everything that makes a coding agent _useful_ is grafted on **after** pre-training.

<!--
Speaker notes:
- The "Translate to French: Hello" example is the punchiest concrete demo. Say it out loud:
  - prompt: "Translate to French: Hello\n"
  - base model continuation: "Translate to Spanish: Hello\nTranslate to German: Hello\n..."
- Audience laughs. Good. The point landed.
- Hammer it: pre-training is necessary, not sufficient. Everything else is post-training.
-->

---

## Stage 1: SFT (instruction tuning)

**Supervised fine-tuning** on a curated set of `(prompt, ideal response)` pairs.

- Source: human contractors writing demonstrations, plus distilled from larger models, plus filtered web data.
- Volume: tens of thousands to low millions of pairs.
- Outcome: the model learns the **format** of "user asks, assistant answers." It now follows instructions instead of pattern-matching them.

**This is what answers Q1.** _(Why does it follow our prompt at all?)_

<!--
Speaker notes:
- Emphasize: SFT is a relatively cheap and small fine-tune. The base model already "knows" everything; SFT just teaches it the dialogue format.
- This is also why a small open-source SFT dataset (Alpaca, etc.) can turn a base model into a chatty one.
- Don't get drawn into "and how does fine-tuning work?", wave at backprop, move on.
-->

---

## Stage 2: RLHF (preference learning)

Two steps:

1. **Reward model:** collect pairs of model responses with a human label of "A is better than B". Train a small model to predict that preference.
2. **RL:** use that reward model to push the policy (the LLM) toward higher-scoring outputs. PPO is the classic algorithm; **DPO** is the simpler modern alternative that skips the explicit reward model.

Outcome: the model learns **what humans find helpful**, when to refuse, and, crucially for agents, **when it has done enough and can stop**.

**This is what answers Q2.** _(Why did it stop instead of looping forever?)_

> Trade-off: too much RLHF and the model becomes overly cautious or sycophantic. Lab releases live or die on this dial.

<!--
Speaker notes:
- DPO fans in the audience will appreciate the mention. Don't get into the math; just say "fewer moving parts than PPO + reward model, often equally good."
- The "when to stop" framing is the workshop-relevant one. Coding agents that don't stop are useless.
- This is also where models get their "personality" / refusal behavior. Constitutional AI is one variant.
-->

---

## Stage 3: Tool-use fine-tuning

Train on **traces** that include tool calls:

```
system: tools = [read_file, write_file, run_bash]
user:   "fix the failing test"
assistant: <tool_call: run_bash("pytest")>
tool:   <result: 2 failed>
assistant: <tool_call: read_file("test_x.py")>
tool:   <result: ...>
assistant: "I see the bug. Fixing now..."
```

The model learns **two things at once**:

- The **wire format**, emit valid JSON tool calls in the right place.
- The **meta-skill**, when to call a tool versus when to respond directly.

**Bleeding edge: agentic RL.** RL applied over multi-turn tool-use trajectories with task-completion reward. This is what major labs are pouring resources into in 2025-2026. It's why Claude Code, Cursor, and Copilot agent mode have gotten so much better in the last 18 months.

**This is what answers Q3.** _(Why did it call `run_bash` instead of just describing it?)_

<!--
Speaker notes:
- The trace example is concrete. Walk through it. Point at each line.
- "Wire format vs meta-skill" is the punchy two-part framing. Repeat it.
- Agentic RL is the answer to "why are agents getting better so fast in 2026?", it's not bigger models, it's better RL signal.
-->

---

## Why this is convergent

| Lab          | Pre-training | SFT | Preference learning      | Tool-use FT      |
| ------------ | ------------ | --- | ------------------------ | ---------------- |
| Anthropic    | yes          | yes | RLHF + Constitutional AI | yes + agentic RL |
| OpenAI       | yes          | yes | RLHF, RLAIF              | yes + agentic RL |
| Google       | yes          | yes | RLHF                     | yes              |
| Meta (Llama) | yes          | yes | DPO                      | partial          |
| DeepSeek     | yes          | yes | RL on reasoning (R1)     | partial          |

Different data. Different reward signals. Different sequencing.

**Same shape.**

> When you train very different models to do _overlapping skills_, they
> converge on _overlapping behaviors_. That's why `MODEL = "..."` is
> just a string. **Answers Q4.**

<!--
Speaker notes:
- This is the slide where "all coding agents work the same way under the hood" gets its proof. Linger.
- Tee up the demo: "We're about to swap MODEL and watch the same loop drive a different brain."
-->

---

## Trained in vs in the prompt

The actionable mental model:

| Trained in (the model already knows) | In the prompt (you control)     |
| ------------------------------------ | ------------------------------- |
| Dialogue format                      | System message                  |
| Helpful tone, refusals               | Project memory (`AGENTS.md`)    |
| Tool-call wire format                | Specific tool schemas           |
| When to stop                         | Current task description        |
| Knowledge up to training cutoff      | Documents you load into context |

When debugging an agent, ask:

> _"Is this a **training problem** (model X just can't do this), or a
> **prompt problem** (it could if I told it better)?"_

**Most issues are prompt problems.** That's the whole reason Block 4 exists.

<!--
Speaker notes:
- This is the most actionable slide of the whole block. Bookmark it for participants.
- Concrete example: "if Claude won't follow your style guide, it's not because Claude lacks taste, it's because you didn't put the style guide in AGENTS.md."
- Almost every agent failure people complain about online turns out to be a prompt problem on inspection.
-->

---

## Demo: Same loop, different brain

We are going to import the **Block 1 agent loop** as a one-line import (`from workshop_agent import run_agent`) and run it against multiple models on the LiteLLM proxy.

What to watch for:

- The same code drives Claude, GPT, Gemini.
- Different models pick different _first_ tools, take different numbers of turns, write the fix slightly differently.
- They all converge on the same **outcome** (passing tests).
- That's convergent post-training, made tactile.

Bonus, if there's time: re-run the agent with deliberately **vague tool descriptions**. Watch behavior degrade. Prompt levers are real.

<!--
Speaker notes:
- Switch to VS Code. Open blocks/02-how-it-works/demo/notebook.ipynb.
- Reset Block 1's starter file before this slide, see instructor-notes pre-block checklist.
- Run all cells. Narrate the proxy discovery cell explicitly: "this is a defensive move, in case GPT or Gemini aren't on the proxy."
-->

---

## Bridge to Block 3

You now have the model:

- It learned a **format** (SFT)
- It learned **preferences** (RLHF)
- It learned a **tool protocol** and **when to call** (tool-use FT)
- It came out _similar_ to other models trained the same way (convergence)

That same training history also tells you **how it can fail**:

- Context window full -> forgets what it was doing
- Niche language not in training data -> hallucinates plausible nonsense
- Reward-hacked on "be confident" -> won't admit it doesn't know
- Trained on short trajectories -> loops on long ones

**Block 3 turns these into a taxonomy with mitigations.**

<!--
Speaker notes:
- Hard hand-off. Don't linger.
- Last sentence: "Block 3 turns these into a taxonomy with mitigations." Stop talking.
-->
