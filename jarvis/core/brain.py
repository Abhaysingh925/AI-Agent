from __future__ import annotations

from typing import Any


class Brain:
    """Small orchestrator that turns a plan and execution result into a reply."""

    def __init__(self, llm_router: Any, memory: Any, prompts: Any) -> None:
        self.llm_router = llm_router
        self.memory = memory
        self.prompts = prompts

    async def generate_response(self, user_input: str, plan: Any, result: Any, context: Any) -> str:
        """Generate a simple conversational response for the current request."""
        return f"Handled: {user_input} ({result.get('status', 'ok')})"
