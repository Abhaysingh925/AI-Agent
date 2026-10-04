from __future__ import annotations

import uuid
from typing import Dict

from core.context import Context


class SessionManager:
    """Manage in-memory sessions for the current runtime."""

    def __init__(self) -> None:
        self._sessions: Dict[str, Context] = {}
        self._active_context: Context | None = None
        self.session_id: str | None = None

    def create_session(self, user_id: str | None = None) -> Context:
        """Create a new session context."""
        session_id = str(uuid.uuid4())
        context = Context(user_id=user_id, session_id=session_id)
        self._sessions[session_id] = context
        self._active_context = context
        self.session_id = session_id
        return context

    def get_session(self, session_id: str) -> Context | None:
        """Retrieve an existing session by identifier."""
        return self._sessions.get(session_id)

    def list_sessions(self) -> list[Context]:
        """Return all active sessions."""
        return list(self._sessions.values())

    def update_user_input(self, user_input: str) -> None:
        """Track the latest user input for the active session."""
        if self._active_context is None:
            self.create_session()
        self._active_context.user_input = user_input

    def update_plan(self, plan: dict[str, object]) -> None:
        """Store a plan for the active session."""
        if self._active_context is None:
            self.create_session()
        self._active_context.plan = plan
