"""Application service for the WhatsApp 'items' flow."""

from __future__ import annotations

from dataclasses import dataclass

from facturafast.channels.whatsapp.types import OutgoingResponse


@dataclass(slots=True)
class ItemsService:
    """Coordinate item retrieval and response rendering."""

    items_repository: object | None = None
    table_renderer: object | None = None

    def build_items_response(self) -> OutgoingResponse | None:
        """Build the response for the items command."""
        return None

