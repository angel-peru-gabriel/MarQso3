"""Utilities for rendering item tables into PNG images."""

from __future__ import annotations

import logging
from io import BytesIO

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from facturafast.domain.models.item import Item

logger = logging.getLogger(__name__)


def render_items_table_png(items: list[Item], title: str = "Items") -> bytes:
    """Render the items table as PNG bytes."""
    rows = [
        [
            str(item.qty),
            item.desc,
            f"{item.unit_price:.2f}",
            f"{item.qty * item.unit_price:.2f}",
        ]
        for item in items
    ]
    if not rows:
        rows = [["0", "Sin items", "0.00", "0.00"]]

    figure_height = max(2.5, 1.2 + len(rows) * 0.45)
    fig, ax = plt.subplots(figsize=(10, figure_height))
    ax.axis("off")
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)

    table = ax.table(
        cellText=rows,
        colLabels=["CANT", "DESCRIPCION", "P.U", "IMPORTE"],
        loc="center",
        cellLoc="center",
        colLoc="center",
        colWidths=[0.12, 0.5, 0.18, 0.2],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.4)

    for (row_index, col_index), cell in table.get_celld().items():
        if row_index == 0:
            cell.set_text_props(weight="bold", color="white")
            cell.set_facecolor("#2F5D8C")
        elif col_index == 1:
            cell.set_text_props(ha="left")

    buffer = BytesIO()
    fig.tight_layout()
    fig.savefig(buffer, format="png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    image_bytes = buffer.getvalue()
    logger.info("Rendered items table image with %s item(s)", len(items))
    return image_bytes
