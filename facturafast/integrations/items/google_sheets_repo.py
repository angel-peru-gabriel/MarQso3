"""Repository backed by Google Sheets."""

from __future__ import annotations

import logging

from facturafast.app.config.settings import Settings
from facturafast.domain.models.item import Item
from facturafast.integrations.items import sheets_client

logger = logging.getLogger(__name__)


def fetch_items(settings: Settings) -> list[Item]:
    """Fetch item rows from Google Sheets and map them to domain objects."""
    rows = sheets_client.read_rows(settings)
    logger.info("Read %s row(s) from Google Sheets", len(rows))

    if not rows:
        return []

    start_index = 0
    first_row = [cell.strip().upper() for cell in rows[0]]
    if any(header in {"CANT", "DESCRIPCION", "P.U"} for header in first_row):
        start_index = 1

    items: list[Item] = []
    for row in rows[start_index:]:
        if not any(str(cell).strip() for cell in row):
            continue
        try:
            items.append(Item.from_sheet_row(row))
        except ValueError:
            continue

    logger.info("Mapped %s valid item(s) from Google Sheets", len(items))
    return items
