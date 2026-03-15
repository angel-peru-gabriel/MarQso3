"""Low-level Google Sheets client placeholder."""

from __future__ import annotations


class SheetsClient:
    """Minimal contract for a future Google Sheets client."""

    def fetch_values(self, range_name: str) -> list[list[str]]:
        """Fetch raw values for the provided range."""
        _ = range_name
        return []

