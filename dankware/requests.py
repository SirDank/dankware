import requests
from typing import Optional

from .exceptions import RateLimitError


def _get_headers(token: Optional[str] = None) -> dict[str, str]:
    """Get request headers with optional GitHub token."""
    headers = {"User-Agent": "dankware"}
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def _check_rate_limit(response: requests.Response) -> None:
    """Check for rate limit and raise appropriate exception."""
    if response.status_code == 403:
        if "rate limit exceeded" in response.text.lower():
            raise RateLimitError("GitHub API rate limit exceeded! Try again in an hour or use a token.")


def github_downloads(
    user_repo: str,
    token: Optional[str] = None,
    timeout: int = 10,
) -> tuple[str, ...]:
    """
    Extracts direct download urls from the latest release on github and returns it as a tuple

    - Example Input: USER_NAME/REPO_NAME ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    - Example Output: ['https://github.com/USER_NAME/REPO_NAME/releases/download/VERSION/EXAMPLE.TXT']

    Args:
        user_repo: Repository in format "USER/REPO".
        token: Optional GitHub token for higher rate limits.
        timeout: Request timeout in seconds.

    Returns:
        Tuple of download URLs.

    Raises:
        RateLimitError: If GitHub API rate limit is exceeded.
        RuntimeError: If request fails for other reasons.

    _____________________________________________________________________________________________________________________________________

    [ EXAMPLE ]
    ```python
    from dankware import github_downloads
    for _ in github_downloads("SirDank/dank.tool"): print(_)
    ```
    """

    response = requests.get(
        f"https://api.github.com/repos/{user_repo}/releases/latest",
        headers=_get_headers(token),
        timeout=timeout,
    )

    if response.status_code == 200:
        return tuple(data["browser_download_url"] for data in response.json()["assets"])

    _check_rate_limit(response)

    raise RuntimeError(f"Failed to get latest release from github: [{response.status_code}] {response.reason}")


def github_file_selector(
    user_repo: str,
    filter_mode: str,
    filter_iterable: list[str],
    token: Optional[str] = None,
) -> tuple[str, ...]:
    """

    This function is used to filter the output from github_downloads()

    - user_repo = 'USER_NAME/REPO_NAME' ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    - filter_mode = 'add' or 'remove'
    - filter_iterable = tuple of strings used to filter results

    _______________________________________________________________________________________________________________________________________________________________________

    [ EXAMPLE ]
    ```python
    from dankware import github_file_selector
    for file_url in github_file_selector("EssentialsX/Essentials", "remove", ('AntiBuild', 'Discord', 'GeoIP', 'Protect', 'XMPP')):
        print(file_url)
    ```

    _______________________________________________________________________________________________________________________________________________________________________

    Example output from github_downloads("EX_USER/EX_REPO"): [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
    ]

    _______________________________________________________________________________________________________________________________________________________________________

    Example Input: "EX_USER/EX_REPO", "add", ("EXAMPLE")

    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
    ]

    - Note: Only urls with file names containing "EXAMPLE" were returned.

    _______________________________________________________________________________________________________________________________________________________________________

    Example Input: "EX_USER/EX_REPO", "remove", ("EXAMPLE")

    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
    ]

    - Note: Only urls with file names not containing "EXAMPLE" were returned.

    """

    if filter_mode not in ("add", "remove"):
        raise ValueError(f"Invalid Filter Mode: {filter_mode} | Valid Modes: 'add', 'remove'")

    urls = []

    for file_url in github_downloads(user_repo, token=token):
        if filter_mode == "add":
            valid = False
        elif filter_mode == "remove":
            valid = True
        for name in filter_iterable:
            if name in file_url.split("/")[-1]:
                valid = not valid
                break
        if valid:
            urls.append(file_url)

    return tuple(urls)


def github_release_info(
    user_repo: str,
    token: Optional[str] = None,
    timeout: int = 10,
) -> dict:
    """
    Get full release information including tag, date, and changelog.

    Args:
        user_repo: Repository in format "USER/REPO".
        token: Optional GitHub token for higher rate limits.
        timeout: Request timeout in seconds.

    Returns:
        Dictionary with release information.

    Raises:
        RateLimitError: If GitHub API rate limit is exceeded.
        RuntimeError: If request fails.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.requests import github_release_info

    info = github_release_info("SirDank/dankware")
    print(info["tag_name"])  # e.g., "v4.0.0"
    print(info["published_at"])
    print(info["body"])  # Release notes/changelog
    ```
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
        user_repo: Repository in format "USER/REPO".
        current_version: Current version string (e.g., "1.0.0" or "v1.0.0").
        token: Optional GitHub token for higher rate limits.

    Returns:
        Tuple of (has_update, latest_version, download_url).

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.requests import github_check_update

    has_update, latest, url = github_check_update("SirDank/dankware", "3.6.0")
    if has_update:
        print(f"New version available: {latest}")
        print(f"Download: {url}")
    ```
    """
    info = github_release_info(user_repo, token=token)
    latest_version = info.get("tag_name", "").lstrip("v")
    current = current_version.lstrip("v")

    # Simple version comparison (works for semver)
    def parse_version(v: str) -> tuple[int, ...]:
        try:
            return tuple(int(x) for x in v.split("."))
        except ValueError:
            return (0,)

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
        user_repo: Repository in format "USER/REPO".
        file_path: Path to the file in the repository.
        branch: Branch name (default: "main").
        token: Optional GitHub token.
        timeout: Request timeout in seconds.

    Returns:
        File content as string.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.requests import github_get_raw_file

    content = github_get_raw_file("SirDank/dankware", "README.md")
    print(content)
    ```
    """
    url = f"https://raw.githubusercontent.com/{user_repo}/{branch}/{file_path}"

    response = requests.get(
        url,
        headers=_get_headers(token),
        timeout=timeout,
    )

    if response.status_code == 200:
        return response.text

    _check_rate_limit(response)

    raise RuntimeError(f"Failed to get file from github: [{response.status_code}] {response.reason}")
