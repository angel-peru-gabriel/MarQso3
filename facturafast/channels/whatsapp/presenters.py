"""Presentation helpers for WhatsApp responses."""

from __future__ import annotations

from typing import Any

from facturafast.channels.whatsapp.types import OutgoingResponse


def present_response(pywa_message: Any, response: OutgoingResponse | None) -> None:
    """Translate an internal response into PyWa reply calls."""
    _ = pywa_message, response

