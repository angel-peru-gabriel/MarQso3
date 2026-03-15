"""Formatting helpers shared across the application."""

from __future__ import annotations


def normalize_command(text: str) -> str:
    """Normalize a command-like incoming message."""
    return text.strip().lower()

