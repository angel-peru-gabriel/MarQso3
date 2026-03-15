"""Invoice domain model."""

from __future__ import annotations

from dataclasses import dataclass, field

from facturafast.domain.models.item import Item


@dataclass(slots=True)
class Invoice:
    """Represents an invoice aggregate placeholder."""

    invoice_number: str
    customer_name: str
    items: list[Item] = field(default_factory=list)

