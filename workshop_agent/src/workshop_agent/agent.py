"""The agent loop, sandbox, tool handlers, and tool schemas.

Mirrors Block 1's `notebook.ipynb` so Blocks 2-4 can reuse the loop
without re-pasting it. See the notebook for the line-by-line walkthrough.
"""

from __future__ import annotations

import json
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any

import litellm

# ---------------------------------------------------------------------------
# Sandbox + tool handlers
# ---------------------------------------------------------------------------


class Sandbox:
    """A directory the agent is allowed to read, write, and run commands in.

    `safe_path` resolves a project-relative path inside the sandbox and
    refuses anything that escapes via `..` or absolute paths. This is the
    simplest possible isolation; real agents add process / syscall /
    network restrictions on top.
    """

    def __init__(self, root: Path) -> None:
        self.root = Path(root).resolve()
        if not self.root.exists():
            raise FileNotFoundError(f"sandbox root does not exist: {self.root}")

    def safe_path(self, rel_path: str) -> Path:
        p = (self.root / rel_path).resolve()
        if p != self.root and self.root not in p.parents:
            raise ValueError(f"path {rel_path!r} escapes sandbox {self.root}")
        return p


def make_tool_handlers(sandbox: Sandbox) -> dict[str, Callable[..., str]]:
    """Return the {tool_name: handler} dict bound to a sandbox."""

    def read_file(path: str) -> str:
        return sandbox.safe_path(path).read_text()

    def write_file(path: str, content: str) -> str:
        p = sandbox.safe_path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return f"wrote {len(content)} chars to {path}"

    def run_bash(command: str) -> str:
        result = subprocess.run(
            ["bash", "-lc", command],
            cwd=sandbox.root,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return (
            f"exit_code={result.returncode}\n"
            f"--- stdout ---\n{result.stdout}"
            f"--- stderr ---\n{result.stderr}"
        )

    return {"read_file": read_file, "write_file": write_file, "run_bash": run_bash}


# ---------------------------------------------------------------------------
# Tool schemas (OpenAI function-calling format, what the model sees)
# ---------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": (
                "Read a UTF-8 text file from the project. "
                "Use this to inspect source code, tests, configs, or AGENTS.md."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": (
                            "Project-relative path, e.g. 'src/sci_units/converters.py'"
                        ),
                    },
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": (
                "Overwrite a UTF-8 text file with new content. Use after you have "
                "decided on the change you want to make. The whole file is replaced."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Project-relative path"},
                    "content": {"type": "string", "description": "Full new file contents"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_bash",
            "description": (
                "Run a bash command from the project root. Useful for `pytest`, "
                "`ls`, `cat`, `grep`. Times out at 60 seconds."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "Bash command line"},
                },
                "required": ["command"],
            },
        },
    },
]


# ---------------------------------------------------------------------------
# The agent loop
# ---------------------------------------------------------------------------


def run_agent(
    *,
    model: str,
    messages: list[dict[str, Any]],
    tool_handlers: dict[str, Callable[..., str]],
    tools: list[dict[str, Any]] = TOOLS,
    max_steps: int = 10,
    max_tokens: int = 4096,
    on_step: Callable[[str], None] | None = print,
) -> list[dict[str, Any]]:
    """Drive the model in a tool-use loop until it stops calling tools.

    Returns the full message list at termination (useful for inspection).
    `on_step` is called once per printed line; pass `None` to silence.
    """

    def emit(line: str) -> None:
        if on_step is not None:
            on_step(line)

    for step in range(1, max_steps + 1):
        response = litellm.completion(
            model=model,
            messages=messages,
            tools=tools,
            max_tokens=max_tokens,
        )
        msg = response.choices[0].message
        finish = response.choices[0].finish_reason

        emit(f"\n--- step {step}  (finish_reason={finish}) ---")
        if msg.content:
            emit(f"[text]\n{msg.content}")
        for tc in msg.tool_calls or []:
            emit(f"[tool_call] {tc.function.name}({tc.function.arguments[:200]})")

        # Append the assistant's full message (text + tool_calls) so the
        # model sees its own decisions on the next turn.
        messages.append(msg.model_dump(exclude_none=True))

        if not msg.tool_calls:
            emit("\n=== agent finished ===")
            return messages

        for tc in msg.tool_calls:
            try:
                args = json.loads(tc.function.arguments)
                output = tool_handlers[tc.function.name](**args)
            except Exception as e:
                output = f"ERROR: {type(e).__name__}: {e}"
            preview = output if len(output) <= 300 else output[:300] + "..."
            emit(f"[tool_result]\n{preview}")
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": output})

    emit(f"\n=== hit max_steps={max_steps} without finishing ===")
    return messages
