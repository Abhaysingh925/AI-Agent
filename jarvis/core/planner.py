from __future__ import annotations

from typing import Any


class Planner:
    """Create a basic plan for the executor to follow."""

    def __init__(self, brain: Any, prompts: Any) -> None:
        self.brain = brain
        self.prompts = prompts

    async def create_plan(self, user_input: str, context: Any) -> dict[str, Any]:
        """Return a lightweight plan structure for the request."""
        return {
            "goal": user_input,
            "steps": [{"action": "respond", "input": user_input}],
        }
