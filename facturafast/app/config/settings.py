"""Environment-backed settings for the application."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(slots=True)
class Settings:
    """Configuration values required by the application."""

    wa_token: str = ""
    wa_phone_id: str = ""
    wa_verify_token: str = ""
    wa_app_secret: str = ""
    sheets_id: str = ""
    sheets_worksheet: str = "Items"
    sheets_range: str = "A:D"
    google_application_credentials: str = ""
    port: int = 8000


def load_settings() -> Settings:
    """Load settings from environment variables."""
    load_dotenv()
    return Settings(
        wa_token=os.getenv("WA_TOKEN", ""),
        wa_phone_id=os.getenv("WA_PHONE_ID", ""),
        wa_verify_token=os.getenv("WA_VERIFY_TOKEN", ""),
        wa_app_secret=os.getenv("WA_APP_SECRET", ""),
        sheets_id=os.getenv("SHEETS_ID", ""),
        sheets_worksheet=os.getenv("SHEETS_WORKSHEET", "Items"),
        sheets_range=os.getenv("SHEETS_RANGE", "A:D"),
        google_application_credentials=os.getenv(
            "GOOGLE_APPLICATION_CREDENTIALS",
            "",
        ),
        port=int(os.getenv("PORT", "8000")),
    )

