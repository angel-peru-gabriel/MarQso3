"""Placeholder service for future SUNAT use cases."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SunatService:
    """Placeholder without Selenium or external IO."""

    def execute_placeholder(self) -> None:
        """No-op placeholder for future SUNAT workflows."""
        return None

