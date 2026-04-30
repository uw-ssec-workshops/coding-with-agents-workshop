#!/usr/bin/env bash
# Post-create setup for the Coding with AI Agents workshop.
# Runs once when a Codespace (or local devcontainer) is first built.
set -euo pipefail

GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RED="\033[0;31m"
RESET="\033[0m"

say() { printf "%b%s%b\n" "$1" "$2" "$RESET"; }

say "$GREEN" "==> Syncing Python environment with uv"
# `sci_units` is declared as a path source in pyproject.toml, so this also
# installs the demo package in editable mode.
uv sync

say "$GREEN" "==> Registering Jupyter kernel 'workshop'"
uv run python -m ipykernel install --user --name workshop --display-name "Workshop (Python 3.12)"

say "$GREEN" "==> Sanity check: Python + litellm + sci_units + workshop_agent imports"
uv run python - <<'PY'
import importlib.metadata
import sys
print(f"  python:         {sys.version.split()[0]}")
print(f"  litellm:        {importlib.metadata.version('litellm')}")
import sci_units
print(f"  sci_units:      {sci_units.__file__}")
import workshop_agent
print(f"  workshop_agent: {workshop_agent.__file__}")
PY

say "$GREEN" "==> Sanity check: LiteLLM proxy credentials"
if [ -n "${LITELLM_API_KEY:-}" ] && [ -n "${LITELLM_API_BASE:-}" ]; then
  say "$GREEN" "  found LITELLM_API_KEY + LITELLM_API_BASE"
  say "$GREEN" "  api_base: ${LITELLM_API_BASE}"
elif [ -n "${LITELLM_API_KEY:-}" ]; then
  say "$YELLOW" "  found LITELLM_API_KEY but no LITELLM_API_BASE."
  say "$YELLOW" "  the notebook will fail to reach the proxy, set LITELLM_API_BASE."
else
  say "$YELLOW" "  no LiteLLM proxy credentials detected yet."
  say "$YELLOW" "  See docs/setup.md for how to provide them before running the notebook."
fi

say "$GREEN" "==> Sanity check: Claude Code env vars (mapped from LITELLM_*)"
if [ -n "${ANTHROPIC_API_KEY:-}" ] && [ -n "${ANTHROPIC_BASE_URL:-}" ]; then
  say "$GREEN" "  ANTHROPIC_BASE_URL: ${ANTHROPIC_BASE_URL}"
  say "$GREEN" "  Claude Code (Block 3 demo) will use the same proxy as the notebooks."
elif [ -n "${LITELLM_API_KEY:-}" ]; then
  say "$YELLOW" "  ANTHROPIC_* not visible. devcontainer remoteEnv mapping may have failed."
  say "$YELLOW" "  Try restarting the Codespace; if that doesn't help, see docs/setup.md."
fi

say "$GREEN" "==> Installing the rse-plugins Claude Code plugin (Block 3 demo)"
if command -v claude >/dev/null 2>&1; then
  if claude plugin marketplace add https://github.com/uw-ssec/rse-plugins 2>/dev/null; then
    say "$GREEN" "  rse-plugins marketplace added"
  else
    say "$YELLOW" "  rse-plugins install failed (or already added). Re-run with:"
    say "$YELLOW" "    claude plugin marketplace add https://github.com/uw-ssec/rse-plugins"
  fi
else
  say "$YELLOW" "  claude CLI not on PATH. The Claude Code VS Code extension"
  say "$YELLOW" "  will prompt to install it on first launch; then re-run:"
  say "$YELLOW" "    claude plugin marketplace add https://github.com/uw-ssec/rse-plugins"
fi

say "$GREEN" "==> Done. Open blocks/01-landscape/demo/notebook.ipynb to get started."
