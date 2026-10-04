from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Context:
    """Runtime context shared across the agent pipeline."""

    user_id: str | None = None
    session_id: str | None = None
    user_input: str = ""
    memory: Any = None
    tools: Any = None
    llm: Any = None
    config: Any = None
    session: Any = None
    metadata: dict[str, Any] = field(default_factory=dict)
    history: list[dict[str, Any]] = field(default_factory=list)
    plan: dict[str, Any] | None = None

    def add_message(self, role: str, content: str) -> None:
        """Append a message to the conversation history."""
        self.history.append({"role": role, "content": content})
