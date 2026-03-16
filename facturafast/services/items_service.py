"""Application service for the WhatsApp 'items' flow."""

from __future__ import annotations

from facturafast.domain.models.item import Item
from facturafast.integrations.items import google_sheets_repo
from facturafast.shared.utils import table_image_renderer


def fetch_items(deps: dict[str, object]) -> list[Item]:
    """Fetch items from the configured Google Sheet."""
    settings = deps["settings"]
    return google_sheets_repo.fetch_items(settings)


def render_items_image(items: list[Item], deps: dict[str, object]) -> bytes:
    """Render the current items list as an image."""
    _ = deps
    return table_image_renderer.render_items_table_png(items, title="Items")
