from __future__ import annotations

from typing import Any


class Executor:
    """Execute a plan using the registered tools."""

    def __init__(self, tool_registry: Any, memory: Any) -> None:
        self.tool_registry = tool_registry
        self.memory = memory

    async def execute_plan(self, plan: dict[str, Any], context: Any) -> dict[str, Any]:
        """Return a simple success payload for the plan."""
        return {"status": "ok", "plan": plan, "message": "Plan executed successfully."}
