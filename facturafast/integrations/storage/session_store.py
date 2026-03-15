"""Contracts for session persistence backends."""

from __future__ import annotations

from typing import Protocol

from facturafast.domain.models.user_session import UserSession


class SessionStore(Protocol):
    """Protocol for session persistence implementations."""

    def get(self, user_id: str) -> UserSession | None:
        """Return the session for the given user, if present."""

    def save(self, session: UserSession) -> None:
        """Persist the session for later retrieval."""

