# Pre-Block Checklists


## Block 1: The AI Coding Agent Landscape

- [ ] Open the demo workspace at `blocks/01-landscape/demo/starter`.
- [ ] Confirm the `sci_units` converters file is reset to the **buggy** state and the tests are **failing** — that's the starting point the demo fixes. Verify in the terminal: `uv run pytest -v` should show red.
- [ ] Open **Copilot Chat** and switch to **Agent** mode. Confirm a workshop model is selected (Claude Sonnet 4.6 / Haiku 4.5).
- [ ] Have the demo prompt copied to a scratch buffer: *"There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change."*
- [ ] Have the demo notebook ready as the Part B fallback (kernel: `Python Environments`).

## Block 2: How It Actually Works (Post-Training & Tool Calling)

- [ ] Restore the code changes in Block 1's starter file (revert the fix from the Block 1 demo) so the repo is back to a clean state.

## Block 3: Agent-Driven Research Software Engineering

- [ ] Confirm the agent can see the skills: they ship in [`.github/skills/`](.github/skills/). If the agent doesn't pick them up, run **Developer: Reload Window**.
- [ ] Confirm the stats stack is installed: in the terminal, `uv run python -c "import pandas, scipy, statsmodels; print('ok')"`. (They're declared in the root `pyproject.toml`.)
- [ ] In the integrated terminal (at the repo root): `rm -rf blocks/03-research-loop/demo/docs/`. We want a clean slate so artifacts appear *during* the demo. (Explicit path so you never touch the repo's top-level `docs/`.) **Don't run any skill yet** — the demo starts with you running `profile-dataset` live in front of the room (slide 5).
- [ ] Have **all the prompts copied to a scratch buffer** (text file, sticky note, Slack DM to yourself, wherever you can paste fast). The exact prompts are in the instructor notes.
- [ ] Open `blocks/03-research-loop/demo/expected-artifacts/` in a side tab as the **fallback** in case the live demo fails.

## Block 4: Build Your Own Skill (capstone)

- [ ] Confirm both worked-example agents appear in the Copilot agent picker. (Open the chat panel, click the agent dropdown, look for `scientific-python-reviewer` and `docstring-writer`.) If not: **Developer: Reload Window**.