# https://github.com/SirDank/dankware

"""
Download utilities for dankware.
"""

import os
import requests
from typing import Optional, Callable

from rich.progress import (
    Progress,
    DownloadColumn,
    TransferSpeedColumn,
    BarColumn,
    TextColumn,
    TimeRemainingColumn,
)

from .exceptions import DownloadError
from .files import safe_filename, ensure_dir


def download_file(
    url: str,
    destination: str,
    progress: bool = True,
    chunk_size: int = 8192,
    timeout: int = 30,
    headers: Optional[dict[str, str]] = None,
) -> str:
    """
    Download a file with optional progress bar.

    Args:
        url: URL to download from.
        destination: Path to save the file. Can be a directory or full file path.
        progress: Whether to show a progress bar.
        chunk_size: Size of chunks to download.
        timeout: Request timeout in seconds.
        headers: Optional HTTP headers.

    Returns:
        Path to the downloaded file.

    Raises:
        DownloadError: If download fails.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.download import download_file

    path = download_file(
        "https://example.com/file.zip",
        "downloads/",
        progress=True
    )
    ```
    """
    try:
        req_headers = {"User-Agent": "dankware"}
        if headers:
            req_headers.update(headers)

        response = requests.get(url, stream=True, timeout=timeout, headers=req_headers)
        response.raise_for_status()

        # Determine filename
        if os.path.isdir(destination):
            # Extract filename from URL or Content-Disposition
            content_disposition = response.headers.get("Content-Disposition", "")
            if "filename=" in content_disposition:
                filename = content_disposition.split("filename=")[-1].strip("\"'")
            else:
                filename = url.split("/")[-1].split("?")[0]
            filename = safe_filename(filename) or "download"
            filepath = os.path.join(destination, filename)
        else:
            ensure_dir(os.path.dirname(destination))
            filepath = destination

        total = int(response.headers.get("content-length", 0))

        if progress and total > 0:
            with Progress(
                TextColumn("[bold blue]{task.description}"),
                BarColumn(),
                DownloadColumn(),
                TransferSpeedColumn(),
                TimeRemainingColumn(),
            ) as prog:
                task = prog.add_task("Downloading...", total=total)
                with open(filepath, "wb") as f:
                    for chunk in response.iter_content(chunk_size=chunk_size):
                        if chunk:
                            f.write(chunk)
                            prog.update(task, advance=len(chunk))
        else:
            with open(filepath, "wb") as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)

        return filepath

    except requests.RequestException as e:
        raise DownloadError(f"Failed to download {url}: {e}") from e


def download_multiple(
    urls: list[str],
    destination_dir: str,
    progress: bool = True,
    on_complete: Optional[Callable[[str, str], None]] = None,
) -> list[str]:
    """
    Download multiple files.

    Args:
        urls: List of URLs to download.
        destination_dir: Directory to save files.
        progress: Whether to show progress.
        on_complete: Optional callback(url, filepath) after each download.

    Returns:
        List of paths to downloaded files.
    """
    ensure_dir(destination_dir)
    downloaded = []

    for url in urls:
        filepath = download_file(url, destination_dir, progress=progress)
        downloaded.append(filepath)
        if on_complete:
            on_complete(url, filepath)

    return downloaded
