"""Adapters from PyWa messages into internal application DTOs."""

from __future__ import annotations

from typing import Any

from facturafast.channels.whatsapp.types import IncomingMessage, OutgoingResponse


def map_pywa_message(pywa_message: Any) -> IncomingMessage:
    """Translate a native PyWa message into the internal DTO."""
    _ = pywa_message
    return IncomingMessage(sender_id="", text="")


def handle_incoming_message(
    message: IncomingMessage,
    conversation_service: Any,
) -> OutgoingResponse | None:
    """Forward the DTO to the application service layer."""
    _ = message, conversation_service
    return None

