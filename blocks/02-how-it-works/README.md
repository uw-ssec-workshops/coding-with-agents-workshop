# Block 2: How It Actually Works (Post-Training and Tool Calling)

## Learning goals

By the end of this block, an attendee can:

1. Explain why a **base** language model, without post-training, can't follow instructions, can't choose helpful actions, and can't call tools, even though it has read most of the internet.
2. Name and distinguish the four post-training stages, **pre-training, SFT, RLHF / preference learning, tool-use fine-tuning**, and say what each one teaches the model.
3. Describe **agentic RL** in one sentence and explain why every major lab is investing in it for coding agents in 2025-2026.
4. Apply the **"trained in" vs "in the prompt"** mental model to triage agent failures (is this a training problem or a prompt problem?).
5. Predict that swapping the model on the workshop's LiteLLM proxy will *mostly* work for the same loop, and explain *why* that's true (convergent post-training).
6. Explain what a **context window** is, what consumes it during an agent run, and why "the model silently forgot my instructions" is an architectural limit, not a bug.

## What's in this folder

```
02-how-it-works/
  README.md            # this file
  slides.md            # Marp slides
  resources.md         # curated further reading
  demo/
    notebook.ipynb     # "Same loop, different brain", model swap experiment
```