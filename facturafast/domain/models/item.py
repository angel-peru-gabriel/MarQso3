"""Item domain model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Item:
    """Represents an item row from the catalog sheet."""

    qty: int
    desc: str
    unit_price: float

    @staticmethod
    def from_sheet_row(row: list[str]) -> "Item":
        """Build an item from a Google Sheets row."""
        if len(row) < 3:
            raise ValueError("Row must contain at least three columns")

        qty_text = str(row[0]).strip()
        desc = str(row[1]).strip()
        unit_price_text = str(row[2]).strip().replace(" ", "")

        if not qty_text or not desc or not unit_price_text:
            raise ValueError("Row contains empty required values")

        qty = int(float(qty_text.replace(",", ".")))
        normalized_price = (
            unit_price_text.replace("S/", "")
            .replace("$", "")
            .replace(",", ".")
        )
        unit_price = float(normalized_price)
        return Item(qty=qty, desc=desc, unit_price=unit_price)
