#!/usr/bin/env bash
set -euo pipefail

# --- Output styling -------------------------------------------------------
# Colors are emitted unconditionally (not gated on a tty) because the
# devcontainer / Codespaces "starting container" log renders ANSI codes.
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BOLD="\033[1m"
RESET="\033[0m"

STAGE="post-start"
TOTAL_STEPS=4

say()  { printf "%b\n==> [%s] (%s/%s) %s%b\n" "${BOLD}${GREEN}" "${STAGE}" "$1" "${TOTAL_STEPS}" "$2" "${RESET}"; }
info() { printf "      %s\n" "$1"; }
warn() { printf "%b  !   %s%b\n" "${YELLOW}" "$1" "${RESET}"; }

SESSION_DIR="${XDG_RUNTIME_DIR:-$HOME/.cache/llmoxie}"
SESSION_FILE="${SESSION_DIR}/session_id"
VSIX_PATH="${HOME}/.cache/oai-compatible-copilot/oai-compatible-copilot-sandbox.vsix"

say 1 "Initializing LLMoxie session"
mkdir -p "${SESSION_DIR}"
chmod 700 "${SESSION_DIR}"

if [ ! -f "${SESSION_FILE}" ]; then
  TMP_SESSION_FILE="$(mktemp "${SESSION_DIR}/session_id.XXXXXX")"
  trap 'rm -f "${TMP_SESSION_FILE}"' EXIT

  cat /proc/sys/kernel/random/uuid > "${TMP_SESSION_FILE}"

  chmod 600 "${TMP_SESSION_FILE}"
  mv "${TMP_SESSION_FILE}" "${SESSION_FILE}"
  trap - EXIT
fi

chmod 600 "${SESSION_FILE}" || true

SESSION_ID="$(cat "${SESSION_FILE}")"
SHORT_SESSION_ID="${SESSION_ID%%-*}"
info "Session: ${SHORT_SESSION_ID}..."

say 2 "Checking OAI-compatible Copilot VSIX artifact"
if [ -f "${VSIX_PATH}" ]; then
  info "VSIX present: ${VSIX_PATH}"
else
  warn "VSIX not found at ${VSIX_PATH}"
fi

say 3 "Checking LLMoxie gateway credentials"
if [ -n "${LITELLM_BASE_URL:-}" ]; then
  info "LITELLM_BASE_URL: configured"
else
  warn "LITELLM_BASE_URL is not set"
fi

if [ -n "${LITELLM_API_KEY:-}" ]; then
  info "LITELLM_API_KEY: detected"
else
  warn "LITELLM_API_KEY is not set"
fi

if [ -n "${OAI_API_KEY:-}" ]; then
  info "OAI_API_KEY alias: detected"
else
  warn "OAI_API_KEY is not set; the LLMoxie Copilot extension may not authenticate"
fi

say 4 "Configuring Claude Code for the LLMoxie gateway"
# Claude Code reads env vars from ~/.claude/settings.json. The auth token and
# base URL come from the Codespace secrets (LITELLM_API_KEY / LITELLM_BASE_URL)
# rather than being committed to the repo. Regenerated every start so secret
# rotation propagates. Any pre-existing settings keys are preserved.
CLAUDE_DIR="${HOME}/.claude"
CLAUDE_SETTINGS="${CLAUDE_DIR}/settings.json"
mkdir -p "${CLAUDE_DIR}"

EXISTING_SETTINGS='{}'
if [ -f "${CLAUDE_SETTINGS}" ] && jq -e . "${CLAUDE_SETTINGS}" >/dev/null 2>&1; then
  EXISTING_SETTINGS="$(cat "${CLAUDE_SETTINGS}")"
elif [ -f "${CLAUDE_SETTINGS}" ]; then
  warn "Existing ${CLAUDE_SETTINGS} is not valid JSON — replacing it"
fi

printf '%s' "${EXISTING_SETTINGS}" | jq \
  --arg base "${LITELLM_BASE_URL:-}" \
  --arg token "${LITELLM_API_KEY:-}" \
  '.env = ((.env // {}) + {
      ANTHROPIC_BASE_URL: $base,
      ANTHROPIC_AUTH_TOKEN: $token,
      CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS: "1"
   })' > "${CLAUDE_SETTINGS}.tmp"
mv "${CLAUDE_SETTINGS}.tmp" "${CLAUDE_SETTINGS}"
chmod 600 "${CLAUDE_SETTINGS}"

if [ -n "${LITELLM_BASE_URL:-}" ] && [ -n "${LITELLM_API_KEY:-}" ]; then
  info "Wrote ${CLAUDE_SETTINGS} (ANTHROPIC_BASE_URL + ANTHROPIC_AUTH_TOKEN from secrets)"
else
  warn "Wrote ${CLAUDE_SETTINGS}, but LITELLM_BASE_URL/LITELLM_API_KEY are empty — Claude Code will not authenticate"
fi

printf "%b\n==> [%s] complete — container is ready.%b\n" "${BOLD}${GREEN}" "${STAGE}" "${RESET}"
