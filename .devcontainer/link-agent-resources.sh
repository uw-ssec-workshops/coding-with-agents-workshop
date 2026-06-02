#!/usr/bin/env bash
set -euo pipefail

# Creates a browsable view of the installed agent CLI home directories inside the
# repo so workshop participants can open the SKILL.md / plugin files in the VS
# Code Explorer.
#
# The CLIs keep their real files in the home directory (~/.claude, ~/.copilot) as
# usual. Rather than symlinking the whole home dir (which would expose secrets),
# we create a real directory per tool and symlink each top-level entry into it,
# SKIPPING anything that looks like a credential/secret (settings.json,
# .credentials.json, config.json, *token*, *secret*, .env*, *.key, ...). The
# symlink folder is git-ignored.

# --- Output styling -------------------------------------------------------
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BOLD="\033[1m"
RESET="\033[0m"

STAGE="link-agent-resources"

say()  { printf "%b\n==> [%s] %s%b\n" "${BOLD}${GREEN}" "${STAGE}" "$1" "${RESET}"; }
info() { printf "      %s\n" "$1"; }
warn() { printf "%b  !   %s%b\n" "${YELLOW}" "$1" "${RESET}"; }

# Lifecycle commands run with the workspace folder as cwd.
LINK_DIR="${PWD}/agent-resources"

say "Linking agent plugins/skills into ${LINK_DIR}"
mkdir -p "${LINK_DIR}"

# is_secret <basename> — returns 0 (true) if the entry looks like a credential or
# secret and should NOT be exposed in the browsable view. Matching is
# case-insensitive against the basename.
is_secret() {
  local base_lower
  base_lower="$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')"
  case "${base_lower}" in
    # Known credential / auth-state files for Claude Code and Copilot CLI.
    settings.json|config.json|.claude.json|mcp-config.json) return 0 ;;
    .credentials.json|credentials.json) return 0 ;;
    # Generic secret-ish patterns.
    *secret*|*token*|*credential*|.env|.env.*|*.key|*.pem) return 0 ;;
  esac
  return 1
}

# link_dir_filtered <symlink-folder-name> <target-dir>
# Creates LINK_DIR/<name> as a REAL directory containing one symlink per
# top-level entry of <target-dir>, skipping entries flagged by is_secret. Safe to
# re-run: the destination is recreated each time (handles migration from an older
# whole-folder symlink without writing into the real home dir).
link_dir_filtered() {
  local name="$1"
  local target="$2"
  local dest="${LINK_DIR}/${name}"

  if [ ! -d "${target}" ]; then
    warn "skipped ${name}: directory not found (${target})"
    return 0
  fi

  # Remove any prior view (a plain symlink, or our own dir of symlinks). No
  # trailing slash, so removing a symlink does NOT touch its target.
  rm -rf "${dest}"
  mkdir -p "${dest}"

  local entry base
  shopt -s dotglob nullglob
  for entry in "${target}"/*; do
    base="$(basename "${entry}")"
    if is_secret "${base}"; then
      info "excluded ${name}/${base} (credential/secret)"
      continue
    fi
    ln -sfn "${entry}" "${dest}/${base}"
  done
  shopt -u dotglob nullglob

  info "linked ${name}/ from ${target} (secrets excluded)"
}

# Expose the CLI home dirs (minus secrets) so the full plugin/skill/agent
# structure is browsable. Skills live inside these (e.g. Claude:
# .claude/plugins/cache/<marketplace>/<plugin>/skills/.../SKILL.md; Copilot:
# .copilot/installed-plugins/... and .copilot/skills/...).
link_dir_filtered "claude" "${HOME}/.claude"
link_dir_filtered "copilot" "${HOME}/.copilot"

# Drop a short note so participants understand what they're looking at.
cat > "${LINK_DIR}/README.md" <<'EOF'
# Agent resources (browsable view)

The `claude/` and `copilot/` folders mirror the agent CLI home directories in the
container (`~/.claude`, `~/.copilot`) via per-entry **symlinks**, so you can
browse the available skills, plugins, and agents (e.g. `SKILL.md` files) in the
Explorer.

- `claude/`  — Claude Code home dir (plugins, skills, ...)
- `copilot/` — Copilot CLI home dir (installed-plugins, skills, agents, ...)

Credential/secret files (e.g. `settings.json`, `.credentials.json`,
`config.json`) are intentionally **not** linked here. This whole folder is also
git-ignored. Editing a linked file edits the real installed copy in the home
directory.
EOF
info "wrote ${LINK_DIR}/README.md"

printf "%b\n==> [%s] complete — agent resources are browsable in the Explorer.%b\n" "${BOLD}${GREEN}" "${STAGE}" "${RESET}"
