from .core.client import HTTPClient
from .parsing.html import extract_attribute, extract_text, parse_html
from .parsing.json import find_duplicates, validate_record
from .storage.csv import save_csv
from .storage.json import save_json

__all__ = [
    "HTTPClient",
    "extract_attribute",
    "extract_text",
    "find_duplicates",
    "parse_html",
    "save_csv",
    "save_json",
    "validate_record"
]