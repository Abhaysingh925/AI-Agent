from __future__ import annotations


class ToolRegistry:
    """Registry for tools that the agent can use."""

    def __init__(self) -> None:
        self.tools: dict[str, object] = {}

    def load_tools(self) -> None:
        """Load built-in tools into the registry."""
        self.tools = {}
