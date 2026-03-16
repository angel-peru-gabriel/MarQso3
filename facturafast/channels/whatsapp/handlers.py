"""Adapters from PyWa messages into internal application DTOs."""

from __future__ import annotations

import logging

from facturafast.channels.whatsapp import presenters
from facturafast.channels.whatsapp.types import IncomingMessage
from facturafast.services import conversation_service

logger = logging.getLogger(__name__)


def on_text_message(msg, deps: dict[str, object]) -> None:
    """Translate a PyWa text message into the application flow."""
    incoming = IncomingMessage(
        user_id=msg.from_user.wa_id,
        text=msg.text or "",
        message_id=getattr(msg, "id", None),
    )
    logger.info("Received WhatsApp text message from %s", incoming.user_id)
    response = conversation_service.handle_incoming(incoming, deps)
    presenters.reply(msg, response, deps)
