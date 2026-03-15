"""Item domain model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Item:
    """Represents a saleable item."""

    code: str
    name: str
    price: float
    stock: int = 0

