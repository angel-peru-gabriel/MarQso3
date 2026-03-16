"""Presentation helpers for WhatsApp responses."""

from __future__ import annotations

from facturafast.channels.whatsapp.types import OutgoingResponse


def reply(msg, response: OutgoingResponse, deps: dict[str, object]) -> None:
    """Present an application response through the PyWa message API."""
    _ = deps
    if response.kind == "image" and response.image_bytes is not None:
        msg.reply_image(image=response.image_bytes, caption=response.caption)
        return
    msg.reply_text(response.text or "")
