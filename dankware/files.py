# https://github.com/SirDank/dankware

"""
File utilities for dankware.
"""

import os
import hashlib
from pathlib import Path
from typing import Iterator


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
    from dankware.files import get_file_hash

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
    # Remove leading/trailing spaces and dots
    filename = filename.strip(". ")
    return filename or "unnamed"


def get_file_size(filepath: str) -> int:
    """
    Get file size in bytes.

    Args:
        filepath: Path to the file.

    Returns:
        File size in bytes.
    """
    return os.path.getsize(filepath)


def human_readable_size(size_bytes: int) -> str:
    """
    Convert bytes to human readable format.

    Args:
        size_bytes: Size in bytes.

    Returns:
        Human readable size string (e.g., "1.5 MB").
    """
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def list_files(directory: str, pattern: str = "*", recursive: bool = False) -> Iterator[Path]:
    """
    List files in a directory.

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


def read_text(filepath: str, encoding: str = "utf-8") -> str:
    """
    Read text file contents.

    Args:
        filepath: Path to the file.
        encoding: File encoding.

    Returns:
        File contents as string.
    """
    return Path(filepath).read_text(encoding=encoding)


def write_text(filepath: str, content: str, encoding: str = "utf-8") -> None:
    """
    Write text to file.

    Args:
        filepath: Path to the file.
        content: Content to write.
        encoding: File encoding.
    """
    Path(filepath).write_text(content, encoding=encoding)


def file_exists(filepath: str) -> bool:
    """Check if file exists."""
    return os.path.isfile(filepath)


def dir_exists(dirpath: str) -> bool:
    """Check if directory exists."""
    return os.path.isdir(dirpath)
