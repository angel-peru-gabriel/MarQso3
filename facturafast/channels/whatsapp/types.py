"""Minimal internal DTOs for the WhatsApp channel."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class IncomingMessage:
    """Internal representation of an incoming WhatsApp message."""

    sender_id: str
    text: str
    message_id: str = ""
    sender_name: str = ""


@dataclass(slots=True)
class OutgoingResponse:
    """Internal representation of a response to present on WhatsApp."""

    text: str = ""
    image_bytes: bytes | None = None
    image_caption: str = ""

