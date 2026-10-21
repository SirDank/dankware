# https://github.com/SirDank/dankware

"""
File utilities for dankware.
"""

import hashlib
from pathlib import Path
from typing import Iterator

__all__ = [
    "get_file_hash",
    "ensure_dir",
    "safe_filename",
    "human_readable_size",
    "list_files",
]


def get_file_hash(filepath: str, algorithm: str = "sha256") -> str:
    """
    Calculate file hash.

    Args:
        filepath: Path to the file.
        algorithm: Hash algorithm (md5, sha1, sha256, sha512).

    Returns:
        Hexadecimal hash string.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware import get_file_hash

    hash_value = get_file_hash("myfile.txt", "sha256")
    print(hash_value)
    ```
    """
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_dir(path: str) -> Path:
    """
    Ensure directory exists, create if not.

    Args:
        path: Path to the directory.

    Returns:
        Path object for the directory.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def safe_filename(filename: str) -> str:
    """
    Sanitize filename for safe filesystem use.

    Args:
        filename: Original filename.

    Returns:
        Sanitized filename safe for all filesystems.
    """
    invalid_chars = '<>:"/\\|?*\0'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    filename = filename.strip(". ")
    return filename or "unnamed"


def human_readable_size(size_bytes: int | float) -> str:
    """
    Convert bytes to human readable format.

    Args:
        size_bytes: Size in bytes.

    Returns:
        Human readable size string (e.g., "1.50 MB").
    """
    size = float(size_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"


def list_files(directory: str, pattern: str = "*", recursive: bool = False) -> Iterator[Path]:
    """
    List files in a directory matching a pattern.

    Args:
        directory: Directory path.
        pattern: Glob pattern to match files.
        recursive: Whether to search recursively.

    Yields:
        Path objects for matching files.
    """
    p = Path(directory)
    if recursive:
        yield from p.rglob(pattern)
    else:
        yield from p.glob(pattern)
