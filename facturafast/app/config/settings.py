"""Environment-backed settings for the application."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(slots=True)
class Settings:
    """Configuration values required by the application."""

    WA_TOKEN: str
    WA_PHONE_ID: str
    WA_VERIFY_TOKEN: str
    WA_APP_SECRET: str = ""
    SHEETS_ID: str = ""
    SHEETS_WORKSHEET: str = "Items"
    SHEETS_RANGE: str = "A:D"
    GOOGLE_APPLICATION_CREDENTIALS: str = ""
    PORT: int = 8000


def load_settings() -> Settings:
    """Load and validate the application settings from the environment."""
    load_dotenv()

    settings = Settings(
        WA_TOKEN=os.getenv("WA_TOKEN", "").strip(),
        WA_PHONE_ID=os.getenv("WA_PHONE_ID", "").strip(),
        WA_VERIFY_TOKEN=os.getenv("WA_VERIFY_TOKEN", "").strip(),
        WA_APP_SECRET=os.getenv("WA_APP_SECRET", "").strip(),
        SHEETS_ID=os.getenv("SHEETS_ID", "").strip(),
        SHEETS_WORKSHEET=os.getenv("SHEETS_WORKSHEET", "Items").strip() or "Items",
        SHEETS_RANGE=os.getenv("SHEETS_RANGE", "A:D").strip() or "A:D",
        GOOGLE_APPLICATION_CREDENTIALS=os.getenv(
            "GOOGLE_APPLICATION_CREDENTIALS",
            "",
        ).strip(),
        PORT=int(os.getenv("PORT", "8000")),
    )

    missing = [
        field_name
        for field_name in (
            "WA_TOKEN",
            "WA_PHONE_ID",
            "WA_VERIFY_TOKEN",
            "SHEETS_ID",
            "GOOGLE_APPLICATION_CREDENTIALS",
        )
        if not getattr(settings, field_name)
    ]
    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    credentials_path = Path(settings.GOOGLE_APPLICATION_CREDENTIALS).expanduser()
    if not credentials_path.is_file():
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS does not point to a file")

    return settings
