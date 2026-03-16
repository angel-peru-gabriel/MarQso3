"""Intent routing for incoming conversation messages."""

from __future__ import annotations

import logging

from facturafast.channels.whatsapp.types import IncomingMessage, OutgoingResponse
from facturafast.services import items_service

logger = logging.getLogger(__name__)


def handle_incoming(
    incoming: IncomingMessage,
    deps: dict[str, object],
) -> OutgoingResponse:
    """Route an incoming message to the matching application use case."""
    normalized_text = incoming.text.strip().lower()
    logger.info("Routing incoming message '%s' from %s", normalized_text, incoming.user_id)

    if normalized_text == "items":
        items = items_service.fetch_items(deps)
        png = items_service.render_items_image(items, deps)
        return OutgoingResponse(
            kind="image",
            image_bytes=png,
            caption="Items",
            text=None,
        )

    return OutgoingResponse(
        kind="text",
        text="Escribe 'items' para ver la tabla.",
        image_bytes=None,
        caption=None,
    )
