#!/usr/bin/env bash
set -euo pipefail

# --- Output styling -------------------------------------------------------
# Colors are emitted unconditionally (not gated on a tty) because the Docker
# build log (this script runs at image-build time) renders ANSI codes.
GREEN="\033[0;32m"
RED="\033[0;31m"
BOLD="\033[1m"
RESET="\033[0m"

STAGE="install-plugins"
TOTAL_STEPS=2

say()   { printf "%b\n==> [%s] (%s/%s) %s%b\n" "${BOLD}${GREEN}" "${STAGE}" "$1" "${TOTAL_STEPS}" "$2" "${RESET}"; }
log()   { printf "      [%s] %s\n" "${STAGE}" "$*"; }
error() { printf "%b      [%s] ERROR: %s%b\n" "${RED}" "${STAGE}" "$*" "${RESET}" >&2; }

say 1 "Installing GitHub Copilot CLI + rse-plugins"
if ! command -v copilot >/dev/null 2>&1; then
  log "Installing GitHub Copilot CLI..."
  curl -fsSL https://gh.io/copilot-install | bash
fi

if ! command -v copilot >/dev/null 2>&1; then
  error "copilot CLI not found after install attempt"
  exit 1
fi

log "Adding copilot CLI plugin marketplace: uw-ssec/rse-plugins"
copilot plugin marketplace add uw-ssec/rse-plugins

log "Installing copilot CLI plugin: ai-research-workflows@rse-plugins"
copilot plugin install ai-research-workflows@rse-plugins

log "Copilot CLI plugins installed."

say 2 "Installing Claude Code CLI + rse-plugins"
if ! command -v claude >/dev/null 2>&1; then
  log "Installing Claude Code CLI..."
  curl -fsSL https://claude.ai/install.sh | bash
fi

if ! command -v claude >/dev/null 2>&1; then
  error "claude CLI not found after install attempt"
  exit 1
fi

log "Adding Claude Code plugin marketplace: uw-ssec/rse-plugins"
claude plugin marketplace add uw-ssec/rse-plugins

log "Installing Claude Code plugin: ai-research-workflows@rse-plugins"
claude plugin install ai-research-workflows@rse-plugins

log "Claude Code plugins installed."

printf "%b\n==> [%s] complete — Copilot CLI and Claude Code plugins installed.%b\n" "${BOLD}${GREEN}" "${STAGE}" "${RESET}"
