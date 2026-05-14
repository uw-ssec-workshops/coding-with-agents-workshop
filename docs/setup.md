# Workshop Setup

Everything you need to do **before** the workshop, plus what to expect when you open your environment.

## Pre-workshop checklist

- [ ] Send your GitHub handle to the workshop coordinator so you can be added to the [`2026-viss-ai-workshop-participants`](https://github.com/orgs/schmidt-sciences/teams/2026-viss-ai-workshop-participants) team. Without this, GitHub Codespaces won't have an organization-paid allocation for you.
- [ ] Sign in to [github.com](https://github.com) and confirm you can see this repository.
- [ ] Open this repo and click **Code → Create codespace on main** to verify the Codespace builds successfully (you can stop it immediately afterward, you don't have to use it again until the workshop).
- [ ] (Optional) Install [VSCode](https://code.visualstudio.com/) locally if you'd prefer running Codespaces in the desktop client instead of the browser. Both work.
- [ ] Use a Chromium-based browser (Chrome, Edge, Arc, Brave) for the best Codespaces experience.

## What the Codespace gives you

When the Codespace finishes building, the `postCreate.sh` script automatically:

1. Runs `uv sync` to install the workshop's Python dependencies (including the `sci_units` and `workshop_agent` packages as path sources).
2. Registers a Jupyter kernel called `Workshop (Python 3.12)`.
3. Runs a sanity check confirming `litellm`, `sci_units`, and `workshop_agent` import.
4. Reports whether the workshop's LiteLLM proxy credentials are visible.
5. Confirms the same credentials are also exposed as `ANTHROPIC_*` env vars (used by the Claude Code extension in Block 3).
6. Installs the `ai-research-workflows` plugin from the [`rse-plugins`](https://github.com/uw-ssec/rse-plugins) marketplace (used in Block 3's demo — provides `/research`, `/plan`, `/implement`, `/validate`). Two `claude plugin ...` commands run back-to-back: one to register the marketplace, one to install the plugin itself. Falls back to printing the manual commands if the Claude Code CLI isn't on PATH yet. Requires Claude Code `>= 2.1.61`; older builds reject the plugin manifest.

You should see a final line that reads:

```
==> Done. Open blocks/01-landscape/demo/notebook.ipynb to get started.
```

If you don't, re-run the script manually with:

```bash
bash .devcontainer/postCreate.sh
```

## LLM proxy server credentials

The workshop runs a small **LLM proxy server** (built on LiteLLM) that gives participants access to Claude (and potentially other models, GPT, Gemini, etc.). Both **GitHub Copilot in your Codespace** and the **"agent in 50 lines" notebook** talk to the same proxy.

You need two environment variables:

| Variable | What it is |
|---|---|
| `LITELLM_API_KEY` | API key for the LLM proxy server (provided to you for the workshop) |
| `LITELLM_API_BASE` | URL of the proxy, e.g. `https://litellm.example.org` (provided to you for the workshop) |

The Codespace forwards both from your **Codespace user secrets**. To add them:

1. Go to your GitHub profile -> **Settings -> Codespaces -> Codespaces secrets -> New secret**.
2. Add `LITELLM_API_KEY` and `LITELLM_API_BASE` with the values you were given.
3. Scope each secret to this repository (`schmidt-sciences-workshop`).
4. Restart the Codespace (or run `source /etc/environment` in the terminal).

The Codespace's `devcontainer.json` automatically also exposes these same values as `ANTHROPIC_API_KEY` and `ANTHROPIC_BASE_URL` so the **Claude Code VS Code extension** (used in Block 3) talks to the same proxy with the same key. You only need to set the `LITELLM_*` secrets; the `ANTHROPIC_*` mapping happens for free.

The instructors will walk you through this live at the start of the workshop if you haven't done it yet.

To verify your credentials work:

```bash
uv run python -c "
import os, litellm
litellm.api_base = os.environ['LITELLM_API_BASE']
litellm.api_key = os.environ['LITELLM_API_KEY']
print(litellm.completion(model='claude-sonnet-4-5', max_tokens=16,
    messages=[{'role':'user','content':'ping'}]).choices[0].message.content)
"
```

You should see Claude reply (typically `pong` or similar). If the model alias is wrong, you'll get a clear error naming the available aliases.

## Running things outside Codespaces (advanced)

If you'd rather run locally:

1. Install [`uv`](https://docs.astral.sh/uv/) and Python 3.12.
2. Clone this repo.
3. Run `uv sync` then `bash .devcontainer/postCreate.sh`.
4. Export `LITELLM_API_KEY` and `LITELLM_API_BASE` in your shell.
5. Use any editor you like; if it's VSCode, install the `GitHub.copilot` and `ms-toolsai.jupyter` extensions.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `postCreate.sh` says "no LiteLLM proxy credentials detected" | Add `LITELLM_API_KEY` and `LITELLM_API_BASE` Codespace secrets and restart the Codespace. See above. |
| `litellm.completion(...)` raises `AuthenticationError` / 401 | `LITELLM_API_KEY` is wrong or expired. Double-check the value in your Codespace secrets. |
| `litellm.completion(...)` raises `BadRequestError` / "model not found" | The model alias on the proxy doesn't match. Update the `MODEL` constant at the top of the notebook (ask an instructor for the correct alias). |
| `litellm.completion(...)` hangs or `ConnectionError` | `LITELLM_API_BASE` is wrong or unreachable. `echo $LITELLM_API_BASE` in the terminal to confirm. |
| Jupyter kernel `Workshop (Python 3.12)` doesn't appear | Run `uv run python -m ipykernel install --user --name workshop --display-name "Workshop (Python 3.12)"` and reload the window. |
| Copilot Chat doesn't respond | Confirm you're signed in to GitHub from the Accounts menu and that the `GitHub.copilot-chat` extension is enabled. |
| `uv sync` fails | Delete `.venv/` and re-run. If still failing, paste the error in the workshop chat. |
| `pytest` complains about missing `sci_units` | Re-run `uv sync` from the repo root, `sci_units` is declared as a path source in `pyproject.toml`. |

## Day-of contacts

- **Anshul Tambay**: [anshul37@uw.edu](mailto:anshul37@uw.edu)
- **Tina Dang**: [tdang@schmidtsciences.org](mailto:tdang@schmidtsciences.org)
