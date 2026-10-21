# https://github.com/SirDank/dankware

"""
GitHub release and asset fetching utilities.
"""

import re
from typing import Any, Optional

import requests

from .exceptions import RateLimitError

__all__ = [
    "github_downloads",
    "github_file_selector",
    "github_release_info",
    "github_check_update",
    "github_get_raw_file",
]


def _get_headers(token: Optional[str] = None) -> dict[str, str]:
    """Get request headers with optional GitHub token."""
    headers = {"User-Agent": "dankware"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def _check_rate_limit(response: requests.Response) -> None:
    """Check for rate limit and raise appropriate exception."""
    if response.status_code == 403 and "rate limit exceeded" in response.text.lower():
        raise RateLimitError("GitHub API rate limit exceeded! Try again in an hour or use a token.")


def github_downloads(
    user_repo: str,
    token: Optional[str] = None,
    timeout: int = 10,
) -> tuple[str, ...]:
    """
    Extract direct download URLs from the latest GitHub release.

    Args:
        user_repo: Repository in format 'USER/REPO'.
        token: Optional GitHub token for higher rate limits.
        timeout: Request timeout in seconds.

    Returns:
        Tuple of download URLs.

    Raises:
        RateLimitError: If GitHub API rate limit is exceeded.
        RuntimeError: If request fails.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware import github_downloads

    for url in github_downloads("SirDank/dankware"):
        print(url)
    ```
    """
    response = requests.get(
        f"https://api.github.com/repos/{user_repo}/releases/latest",
        headers=_get_headers(token),
        timeout=timeout,
    )

    if response.status_code == 200:
        return tuple(data["browser_download_url"] for data in response.json().get("assets", []))

    _check_rate_limit(response)
    raise RuntimeError(f"Failed to get latest release from github: [{response.status_code}] {response.reason}")


def github_file_selector(
    user_repo: str,
    filter_mode: str,
    filter_iterable: list[str] | tuple[str, ...],
    token: Optional[str] = None,
) -> tuple[str, ...]:
    """
    Filter download URLs returned by github_downloads().

    Args:
        user_repo: Repository in format 'USER/REPO'.
        filter_mode: 'add' (keep matches) or 'remove' (exclude matches).
        filter_iterable: Keywords to filter URLs against.
        token: Optional GitHub token.

    Returns:
        Filtered tuple of download URLs.

    Raises:
        ValueError: If filter_mode is not 'add' or 'remove'.
    """
    if filter_mode not in ("add", "remove"):
        raise ValueError(f"Invalid Filter Mode: {filter_mode} | Valid Modes: 'add', 'remove'")

    urls = []
    for file_url in github_downloads(user_repo, token=token):
        filename = file_url.split("/")[-1]
        matches = any(name in filename for name in filter_iterable)
        if filter_mode == "add" and matches:
            urls.append(file_url)
        elif filter_mode == "remove" and not matches:
            urls.append(file_url)

    return tuple(urls)


def github_release_info(
    user_repo: str,
    token: Optional[str] = None,
    timeout: int = 10,
) -> dict[str, Any]:
    """
    Get full release metadata including tag, name, changelog body, and assets.

    Args:
        user_repo: Repository in format 'USER/REPO'.
        token: Optional GitHub token.
        timeout: Request timeout in seconds.

    Returns:
        Dictionary of release information.

    Raises:
        RateLimitError: If rate limit exceeded.
        RuntimeError: If request fails.
    """
    response = requests.get(
        f"https://api.github.com/repos/{user_repo}/releases/latest",
        headers=_get_headers(token),
        timeout=timeout,
    )

    if response.status_code == 200:
        data = response.json()
        return {
            "tag_name": data.get("tag_name", ""),
            "name": data.get("name", ""),
            "published_at": data.get("published_at", ""),
            "body": data.get("body", ""),
            "html_url": data.get("html_url", ""),
            "author": data.get("author", {}).get("login", ""),
            "prerelease": data.get("prerelease", False),
            "draft": data.get("draft", False),
            "assets": [
                {
                    "name": asset.get("name", ""),
                    "download_url": asset.get("browser_download_url", ""),
                    "size": asset.get("size", 0),
                    "download_count": asset.get("download_count", 0),
                }
                for asset in data.get("assets", [])
            ],
        }

    _check_rate_limit(response)
    raise RuntimeError(f"Failed to get release info from github: [{response.status_code}] {response.reason}")


def github_check_update(
    user_repo: str,
    current_version: str,
    token: Optional[str] = None,
) -> tuple[bool, str, str]:
    """
    Check if a newer version is available on GitHub.

    Args:
        user_repo: Repository in format 'USER/REPO'.
        current_version: Current version string (e.g. '3.6.0' or 'v4.0.0').
        token: Optional GitHub token.

    Returns:
        Tuple of (has_update, latest_version, html_url).
    """
    info = github_release_info(user_repo, token=token)
    latest_version = info.get("tag_name", "").lstrip("v")
    current = current_version.lstrip("v")

    def parse_version(v: str) -> tuple[int, ...]:
        parts = re.findall(r"\d+", v)
        return tuple(int(x) for x in parts) if parts else (0,)

    has_update = parse_version(latest_version) > parse_version(current)
    download_url = info.get("html_url", "")
    return has_update, latest_version, download_url


def github_get_raw_file(
    user_repo: str,
    file_path: str,
    branch: str = "main",
    token: Optional[str] = None,
    timeout: int = 10,
) -> str:
    """
    Get raw file content from a GitHub repository.

    Args:
        user_repo: Repository in format 'USER/REPO'.
        file_path: Path to file in repository.
        branch: Branch name (default: 'main').
        token: Optional GitHub token.
        timeout: Request timeout in seconds.

    Returns:
        File content as string.
    """
    url = f"https://raw.githubusercontent.com/{user_repo}/{branch}/{file_path}"
    response = requests.get(url, headers=_get_headers(token), timeout=timeout)

    if response.status_code == 200:
        return response.text

    _check_rate_limit(response)
    raise RuntimeError(f"Failed to get file from github: [{response.status_code}] {response.reason}")
