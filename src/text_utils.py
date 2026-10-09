"""Utilities for cleaning and formatting text strings."""


def clean_name(raw):
    """Tidies a messy name string by removing extra whitespace and converting to title case."""
    return " ".join(raw.split()).title()
    pass
