"""Utilities for rendering tabular data into an image."""

from __future__ import annotations

from collections.abc import Sequence


def render_table_image(rows: Sequence[Sequence[str]], title: str = "") -> bytes:
    """Render a table into image bytes in a future implementation."""
    _ = rows, title
    return b""

