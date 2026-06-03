#!/usr/bin/env bash
set -euo pipefail

# --- Output styling -------------------------------------------------------
# Colors are emitted unconditionally (not gated on a tty) because the Docker
# build log (this script runs at image-build time) renders ANSI codes.
GREEN="\033[0;32m"
RED="\033[0;31m"
BOLD="\033[1m"
RESET="\033[0m"

STAGE="install-copilot-cli"
TOTAL_STEPS=1

say()   { printf "%b\n==> [%s] (%s/%s) %s%b\n" "${BOLD}${GREEN}" "${STAGE}" "$1" "${TOTAL_STEPS}" "$2" "${RESET}"; }
log()   { printf "      [%s] %s\n" "${STAGE}" "$*"; }
error() { printf "%b      [%s] ERROR: %s%b\n" "${RED}" "${STAGE}" "$*" "${RESET}" >&2; }

# We deliberately install NO agent plugins here. The workshop's research-loop
# workflow (/research, /plan, /iterate-plan, /experiment, /implement, /validate,
# /handoff) ships in-repo as Copilot prompt files under .github/prompts/, so it
# works in Copilot Chat with no marketplace plugin to install or keep in sync.

say 1 "Installing GitHub Copilot CLI"
if ! command -v copilot >/dev/null 2>&1; then
  log "Installing GitHub Copilot CLI..."
  curl -fsSL https://gh.io/copilot-install | bash
fi

if ! command -v copilot >/dev/null 2>&1; then
  error "copilot CLI not found after install attempt"
  exit 1
fi

log "GitHub Copilot CLI installed."

printf "%b\n==> [%s] complete — Copilot CLI installed.%b\n" "${BOLD}${GREEN}" "${STAGE}" "${RESET}"
