"""In-memory session storage placeholder."""

from __future__ import annotations

from dataclasses import dataclass, field

from facturafast.domain.models.user_session import UserSession


@dataclass(slots=True)
class InMemorySessionStore:
    """Simple in-memory session store for local development."""

    sessions: dict[str, UserSession] = field(default_factory=dict)

    def get(self, user_id: str) -> UserSession | None:
        """Return a stored session, if any."""
        return self.sessions.get(user_id)

    def save(self, session: UserSession) -> None:
        """Store the latest session state."""
        self.sessions[session.user_id] = session

