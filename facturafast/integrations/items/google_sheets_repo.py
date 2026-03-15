"""Repository placeholder backed by Google Sheets."""

from __future__ import annotations

from dataclasses import dataclass

from facturafast.domain.models.item import Item
from facturafast.integrations.items.sheets_client import SheetsClient


@dataclass(slots=True)
class GoogleSheetsItemsRepository:
    """Translate Google Sheets rows into domain items."""

    sheets_client: SheetsClient | None = None

    def list_items(self) -> list[Item]:
        """Return the current catalog of items."""
        return []

