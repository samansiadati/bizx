from datetime import date
from pathlib import Path
from urllib.parse import urljoin


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


def get_file(file_name: str, file_path: str | Path = ".") -> Path:
    """
    Construct a local file path.

    Example:
        get_file("data.csv", "/tmp")
        -> Path("/tmp/data.csv")
    """
    return Path(file_path) / file_name


def get_url(file_name: str, file_url: str) -> str:
    """
    Construct a URL for a file.

    Example:
        get_url("data.csv", "https://example.com/data/")
        -> "https://example.com/data/data.csv"
    """
    return urljoin(file_url.rstrip("/") + "/", file_name)