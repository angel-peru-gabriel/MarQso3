"""PyWa application factory and handler registration placeholders."""

from __future__ import annotations

from typing import Any

from facturafast.app.config.settings import Settings


def register_handlers(pywa_client: Any) -> Any:
    """Register WhatsApp handlers on the provided PyWa client."""
    return pywa_client


def create_pywa_app(*, settings: Settings) -> Any:
    """Create the PyWa application instance."""
    _ = settings
    return register_handlers(pywa_client=None)

