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

## Aside: why can a network learn any of this?

Pre-training, SFT, RLHF, every stage in this block assumes one thing: that a neural network _can_ represent the function you are training it toward. That assumption has a name.

**Universal Approximation Theorem** (Cybenko 1989, Hornik 1991): a network with a non-linear activation and enough neurons can approximate _any_ continuous function to arbitrary precision.

- "Next token given context", "helpful reply given prompt", "tool call given task", all just functions.
- The **non-linearity** (ReLU, etc.) is the key ingredient. Stack only linear layers and the whole thing collapses back into a single straight line.
- **Depth** is what makes it _efficient_: deep nets compose simple features into complex ones, instead of needing astronomically many neurons in one layer.

> Universality only says the function _exists_ inside the network. Training is the bet that gradient descent can _find_ it, and that it _generalizes_ to new inputs. It usually does. That empirical fact is the miracle the rest of this block stands on.

<!--
Speaker notes:
- OPTIONAL aside (~60-90s). If you're on time it's a nice "zoom out". If you're behind, skip it entirely, nothing downstream depends on it.
- Do NOT get into the math. The whole pitch in one line: "a big enough net with a non-linear squiggle can bend itself to fit any curve."
- The payoff is the blockquote. Mirror the pre-training framing: universality is *necessary, not sufficient*. Existence is not findability, and findability is not generalization.
- If asked "then why not just use one giant hidden layer?": depth buys *efficiency*, not new expressive power. A shallow net could match it but might need an impractical number of neurons.
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
- Don't get drawn into "and how does fine-tuning work?", wave at backprop, loss functions, and move on.
-->

---

## SFT for coding: what the data looks like

A single training example is just a `(prompt, response)` pair. For coding agents, contractors write thousands of these:

```
PROMPT:
Write a Python function `running_mean(xs, k)` that returns the
length-k moving average of a list of floats. Handle k > len(xs)
by returning an empty list.

RESPONSE:
def running_mean(xs: list[float], k: int) -> list[float]:
    if k <= 0 or k > len(xs):
        return []
    out = []
    s = sum(xs[:k])
    out.append(s / k)
    for i in range(k, len(xs)):
        s += xs[i] - xs[i - k]
        out.append(s / k)
    return out
```

The model learns the **shape**: read the spec, write typed code, handle the edge case the prompt mentioned, stop. Multiply by ~hundreds of thousands of examples across languages, frameworks, and difficulty levels.

<!--
Speaker notes:
- Walk through the example. Point out: typed signature, edge case from the spec, O(n) instead of naive O(nk), no extra commentary.
- That's not the model "being smart", that's the model imitating what a contractor wrote.
- Open-source analogues people may have heard of: CodeAlpaca, Magicoder/OSS-Instruct, the SFT split of OpenCodeInterpreter. Mention only if asked.
- Key takeaway: the *style* of agent output (concise, typed, edge-case-aware) is literally a learned imitation of how the SFT contractors wrote.
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

## RLHF for coding: what the data looks like

A single training example is a `(prompt, response_A, response_B, label)` tuple. The label is a human's pick of which response is better.

```
PROMPT:
My pytest run hangs forever on test_ingest. What should I do?

RESPONSE A:                          RESPONSE B:
Run `pytest -x test_ingest` to       You should rewrite your test
fail fast, then add `--timeout=10`   suite using async fixtures and
(pytest-timeout). If it still        switch to pytest-asyncio. Also
hangs, the culprit is usually a      consider migrating off pytest
network call or a fixture waiting    entirely. Here is a 200-line
on a lock; isolate with `-k` and     refactor that does that...
add `-s` to see prints.

LABEL: A > B   (focused, answers the question, stops)
```

What the model learns from millions of these:

- **Stay on the asked question** (don't propose a rewrite when asked to debug).
- **Match the user's scope** (one failing test, not the whole suite).
- **Stop when the answer is complete** instead of padding.

**That's the "knowing when to stop" behavior**, learned as a preference, not a rule.

<!--
Speaker notes:
- Walk through both responses out loud. Audience laughs at B - we've all gotten that response.
- Emphasize: nobody told the model "don't propose 200-line refactors". It learned that humans rate the focused answer higher.
- Public analogues if asked: HH-RLHF (Anthropic), UltraFeedback, the preference splits in Llama-2/3 papers.
- Tie back to Q2: the *reason* a coding agent eventually says "done" instead of looping is RLHF preference data like this.
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

## Tool-use FT: the meta-skill, side by side

Start with the simplest version of a training example: **one prompt in, one assistant turn out**. Same system prompt, same tools, two different user prompts:

```
─── Example A ──────────────────────────────────────
system: tools = [run_bash, read_file, write_file]
user:   What does the `-x` flag do in pytest?

A: It stops the test run after the first failure
   instead of running the whole suite. Useful when
   you want a fast feedback loop while debugging.
────────────────────────────────────────────────────

─── Example B ──────────────────────────────────────
system: tools = [run_bash, read_file, write_file]
user:   How many tests are in this repo right now?

A: ↳ tool_call: {"name": "run_bash",
                 "params": {"cmd": "pytest --collect-only -q | tail -1"}}

tool:   137 tests collected

A: 137 tests.
────────────────────────────────────────────────────
```

The **only** thing that changes the assistant's first move is the prompt:

- **A** is answerable from training knowledge → answer directly, **don't** call a tool.
- **B** requires reading the actual repo state → **must** call a tool.

This is the **meta-skill**: knowing which prompts cross the line into "I need to actually go look." Trained on thousands of paired examples like these.

<!--
Speaker notes:
- Start here so the audience sees the simplest possible case before the multi-turn trajectory on the next slide.
- The point to hammer: tools aren't called *because they exist in the system prompt*. They're called when the prompt requires fresh information the model can't have.
- Common confusion to head off: "but couldn't the model just guess 137?" Yes, and a base model would. The whole point of this training stage is teaching it not to.
- If asked: yes, this is also why agents sometimes call tools they shouldn't (over-eager tool use is a known failure mode and a major RLHF target).
- Bridge to next slide: "OK, that's the easy case — one tool call. Now let's see what a *real* coding trajectory looks like."
-->

---

## Tool-use FT: a full multi-turn trajectory

Now scale up. A real example is a full **trajectory** — the model emits a tool call, reads the result, decides what to do next, and keeps going until the task is done. Lines starting with `A:` (the assistant) are the only ones the model is **trained to emit**; `system`, `user`, and `tool` lines are context the model is trained to **read and condition on**.

```
system: You are a coding agent. Tools available:
        [{"name": "run_bash", "params": {"cmd": "string"}},
         {"name": "read_file", "params": {"path": "string"}},
         {"name": "write_file", "params": {"path": "...", "content": "..."}}]

user:   The test_parse_date test is failing. Please fix it.

A: I'll start by running the test to see the error.
   ↳ tool_call: {"name": "run_bash",
                 "params": {"cmd": "pytest -x test_parse.py::test_parse_date"}}

tool:   FAILED test_parse.py::test_parse_date
        AssertionError: expected datetime(2024,1,2), got datetime(2024,2,1)

A: Day/month swap. Let me read the parser.
   ↳ tool_call: {"name": "read_file", "params": {"path": "parser.py"}}

tool:   def parse_date(s): return datetime.strptime(s, "%m/%d/%Y")

A: Format string has month before day; input is DD/MM/YYYY.
   ↳ tool_call: {"name": "write_file",
                 "params": {"path": "parser.py",
                            "content": "def parse_date(s): return datetime.strptime(s, '%d/%m/%Y')"}}

tool:   ok

A: ↳ tool_call: {"name": "run_bash", "params": {"cmd": "pytest -x test_parse.py"}}
tool:   1 passed

A: Fixed. The format string had month and day swapped. Tests now pass.
```

The trajectory teaches **wire format** (valid JSON, right schema), **multi-step meta-skill** (run → read → reason → write → re-run), and **termination** (stop after the green test, don't keep poking).

<!--
Speaker notes:
- This is the meatier follow-up to the side-by-side slide. Walk down the trajectory line by line. Note the structure: hypothesis → tool call → observation → updated hypothesis.
- Call out: every assistant turn is either a tool call OR a final answer. That binary is *learned* here.
- Public analogues if asked: ToolBench, Gorilla, the agentic SFT data described in the Llama-3.1 and DeepSeek-Coder-V2 papers.
- Bridge to the convergence slide: "Now imagine generating thousands of these trajectories, scoring whether the final test passed, and using *that* as RL reward. That's agentic RL — the bleeding edge from earlier."
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
