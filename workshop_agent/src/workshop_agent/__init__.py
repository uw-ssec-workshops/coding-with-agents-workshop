"""workshop_agent, the agent loop from Block 1, packaged for reuse.

Block 1's `notebook.ipynb` is the pedagogical source-of-truth: the loop is
*the* artifact of that block, and learners read it cell by cell. This
package mirrors that logic so Blocks 2-4 can write `from workshop_agent
import run_agent` instead of re-pasting the loop, freeing those notebooks
to focus on what's new.

If you change the agent loop here, update Block 1's notebook to match
(or vice versa). They are intentionally equivalent.
"""

from workshop_agent.agent import (
    TOOLS,
    Sandbox,
    make_tool_handlers,
    run_agent,
)

__all__ = [
    "TOOLS",
    "Sandbox",
    "make_tool_handlers",
    "run_agent",
]
