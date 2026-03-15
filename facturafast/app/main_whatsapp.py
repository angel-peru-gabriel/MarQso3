"""Bootstrap entrypoint for the PyWa-based WhatsApp application."""

from __future__ import annotations

from facturafast.app.config.logging import configure_logging
from facturafast.app.config.settings import Settings, load_settings
from facturafast.channels.whatsapp.pywa_app import create_pywa_app


def create_application(settings: Settings | None = None) -> object | None:
    """Create and wire the application objects."""
    configure_logging()
    resolved_settings = settings or load_settings()
    return create_pywa_app(settings=resolved_settings)


def main() -> None:
    """CLI entrypoint placeholder."""
    create_application()


if __name__ == "__main__":
    main()

