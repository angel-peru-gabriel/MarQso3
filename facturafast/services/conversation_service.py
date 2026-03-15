"""Intent routing for incoming conversation messages."""

from __future__ import annotations

from dataclasses import dataclass

from facturafast.channels.whatsapp.types import IncomingMessage, OutgoingResponse


@dataclass(slots=True)
class ConversationService:
    """Route incoming messages to the proper application service."""

    items_service: object | None = None
    sunat_service: object | None = None
    audit_service: object | None = None

    def handle_message(self, message: IncomingMessage) -> OutgoingResponse | None:
        """Handle an incoming message."""
        _ = message
        return None

