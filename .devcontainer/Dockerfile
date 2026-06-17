# Base image intentionally uses "base" (not python) because the Python
# interpreter and all dependencies are managed via uv, not system Python.
FROM mcr.microsoft.com/devcontainers/base:dev-ubuntu26.04

# Use bash for RUN so pipefail is supported.
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# curl, git, jq, tar, and ca-certificates are provided by the
# mcr.microsoft.com/devcontainers/base image, so no apt install step is needed.

# Install uv from the official, version-pinned uv image. The astral-sh/uv image
# ships statically-linked `uv`/`uvx` binaries, so copying them in is both
# reproducible (pinned tag) and avoids a curl|sh bootstrap.
COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /uvx /usr/local/bin/

ENV VSCODE_HOME=/home/vscode \
    VSCODE_USER=vscode \
    SHELL=/bin/bash \
    PATH=/home/vscode/.local/bin:${PATH}

USER ${VSCODE_USER}
# No WORKDIR is set intentionally: at runtime the devcontainer mounts the repo
# at /workspaces/<repo-name>, which differs per fork/repo, and every build step
# below uses absolute paths (/tmp/...) or cd. Hardcoding a repo-specific WORKDIR
# would be misleading and wrong for repos with a different name.

RUN echo 'eval "$(uv generate-shell-completion bash)"' >> ${VSCODE_HOME}/.bashrc

# Pre-populate uv's package cache (and its managed CPython) so that
# onCreateCommand's `uv sync` resolves from disk instead of hitting the network.
# The editable path dependencies (sci-units, workshop-agent) are copied in as
# well because `uv sync --locked` validates the lock against them; without their
# sources present uv reports the lock as out-of-date and fails. The temporary
# .venv is discarded because the real one is created inside the Docker volume
# mount at container-create time.
COPY --chown=${VSCODE_USER}:${VSCODE_USER} pyproject.toml uv.lock README.md /tmp/uv-warmup/
COPY --chown=${VSCODE_USER}:${VSCODE_USER} blocks/01-landscape/demo/starter /tmp/uv-warmup/blocks/01-landscape/demo/starter
COPY --chown=${VSCODE_USER}:${VSCODE_USER} workshop_agent /tmp/uv-warmup/workshop_agent
RUN cd /tmp/uv-warmup \
    && uv sync --locked \
    && rm -rf /tmp/uv-warmup

# Pre-download and verify the OAI-compatible Copilot VSIX so that
# postCreateCommand can skip the network fetch on first container create.
COPY --chown=${VSCODE_USER}:${VSCODE_USER} .devcontainer/oai-compatible-copilot-vsix.env /tmp/oai-compatible-copilot-vsix.env
COPY --chown=${VSCODE_USER}:${VSCODE_USER} .devcontainer/post-create.sh /tmp/post-create.sh
RUN bash /tmp/post-create.sh \
    && rm -f /tmp/post-create.sh /tmp/oai-compatible-copilot-vsix.env
