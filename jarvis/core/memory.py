from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MemoryEntry:
    user_input: str
    plan: dict[str, Any] | None = None
    result: dict[str, Any] | None = None
    error: str | None = None
    session_id: str | None = None


class MemorySystem:
    """In-memory storage for interactions and agent state."""

    def __init__(self) -> None:
        self.entries: list[MemoryEntry] = []

    async def store_interaction(self, **kwargs: Any) -> None:
        """Persist a new interaction entry."""
        self.entries.append(MemoryEntry(**kwargs))
