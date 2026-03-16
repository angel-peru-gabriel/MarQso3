"""PyWa application factory and handler registration."""

from __future__ import annotations

from flask import Flask
from pywa import WhatsApp, filters

from facturafast.app.config.settings import Settings
from facturafast.channels.whatsapp import handlers


def create_wa(flask_app: Flask, settings: Settings) -> WhatsApp:
    """Create the PyWa WhatsApp client."""
    kwargs: dict[str, object] = {
        "server": flask_app,
        "phone_id": settings.WA_PHONE_ID,
        "token": settings.WA_TOKEN,
        "verify_token": settings.WA_VERIFY_TOKEN,
        "webhook_endpoint": "/webhook",
    }
    if settings.WA_APP_SECRET:
        kwargs["app_secret"] = settings.WA_APP_SECRET
    return WhatsApp(**kwargs)


def register_handlers(wa: WhatsApp, deps: dict[str, object]) -> None:
    """Register the text handler for the WhatsApp channel."""

    @wa.on_message(filters.text)
    def on_message(_, msg) -> None:
        handlers.on_text_message(msg, deps)
