"""General string and data utility functions."""


def uc_first(string: str | None) -> str:
    """Uppercase first character of a string."""
    text = str(string) if string is not None else ""
    return text[0].upper() + text[1:] if text else ""
