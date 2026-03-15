"""Application service for audit events."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class AuditService:
    """Placeholder service for audit/event recording."""

    events: list[dict[str, object]] = field(default_factory=list)

    def record(self, event_name: str, payload: dict[str, object] | None = None) -> None:
        """Store an audit event in memory."""
        self.events.append({"event_name": event_name, "payload": payload or {}})

