"""Low-level Google Sheets client implementation."""

from __future__ import annotations

import gspread
from google.oauth2.service_account import Credentials
from gspread import Worksheet
from gspread.exceptions import WorksheetNotFound

from facturafast.app.config.settings import Settings

GOOGLE_SCOPES = (
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
)


def open_worksheet(settings: Settings) -> Worksheet:
    """Open the configured worksheet from Google Sheets."""
    credentials = Credentials.from_service_account_file(
        settings.GOOGLE_APPLICATION_CREDENTIALS,
        scopes=GOOGLE_SCOPES,
    )
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key(settings.SHEETS_ID)
    try:
        return spreadsheet.worksheet(settings.SHEETS_WORKSHEET)
    except WorksheetNotFound:
        return spreadsheet.sheet1


def read_rows(settings: Settings) -> list[list[str]]:
    """Read rows from the configured Google Sheet range."""
    worksheet = open_worksheet(settings)
    if settings.SHEETS_RANGE:
        return worksheet.get(settings.SHEETS_RANGE)
    return worksheet.get_all_values()
