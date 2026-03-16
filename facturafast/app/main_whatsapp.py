"""Bootstrap entrypoint for the PyWa-based WhatsApp application."""

from __future__ import annotations

from flask import Flask

from facturafast.app.config.logging import setup_logging
from facturafast.app.config.settings import Settings, load_settings
from facturafast.channels.whatsapp import pywa_app


def build_deps(settings: Settings) -> dict[str, object]:
    """Build the dependency container for the application."""
    return {"settings": settings}


def main() -> None:
    """Run the WhatsApp application server."""
    setup_logging()
    settings = load_settings()
    flask_app = Flask(__name__)
    wa = pywa_app.create_wa(flask_app, settings)
    deps = build_deps(settings)
    pywa_app.register_handlers(wa, deps)
    flask_app.run(host="0.0.0.0", port=settings.PORT)


if __name__ == "__main__":
    main()
