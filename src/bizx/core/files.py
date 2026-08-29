from datetime import date
from pathlib import Path


def updated_nm(initial: str, frmt: str) -> str:
    """
    Generate a date-stamped report filename.

    Example:
        updated_nm("schema", "txt")
        -> "schema_report_20260828.txt"
    """
    today = date.today()
    return f"{initial}_report_{today:%Y%m%d}.{frmt}"


def make_report(file_name: str, content: str) -> None:
    """
    Write text content to a file.
    """
    Path(file_name).write_text(content, encoding="utf-8")