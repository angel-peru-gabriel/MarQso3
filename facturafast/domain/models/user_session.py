"""User session domain model."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class UserSession:
    """Represents conversational state for a WhatsApp user."""

    user_id: str
    current_intent: str = ""
    metadata: dict[str, str] = field(default_factory=dict)

