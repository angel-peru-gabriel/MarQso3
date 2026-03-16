"""Minimal internal DTOs for the WhatsApp channel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class IncomingMessage:
    """Internal representation of an incoming WhatsApp message."""

    user_id: str
    text: str
    message_id: str | None = None


@dataclass(slots=True)
class OutgoingResponse:
    """Internal representation of an outbound WhatsApp response."""

    kind: Literal["text", "image"]
    text: str | None = None
    image_bytes: bytes | None = None
    caption: str | None = None
