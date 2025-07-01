import requests


def github_downloads(user_repo: str) -> tuple[str]:
    """
    Extracts direct download urls from the latest release on github and returns it as a tuple

    - Example Input: USER_NAME/REPO_NAME ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    - Example Output: ['https://github.com/USER_NAME/REPO_NAME/releases/download/VERSION/EXAMPLE.TXT']

    _____________________________________________________________________________________________________________________________________

    [ EXAMPLE ]
    ```python
    from dankware import github_downloads
    for _ in github_downloads("SirDank/dank.tool"): print(_)
    ```
    """

    # [NOTE] needs to be updated to not use api. Example: https://github.com/EssentialsX/Essentials/releases/expanded_assets/2.20.1

    response = requests.get(
        f"https://api.github.com/repos/{user_repo}/releases/latest",
        headers={"User-Agent": "dankware"},
        timeout=3,
    )

    if response.status_code == 200:
        return tuple(data["browser_download_url"] for data in response.json()["assets"])
    raise RuntimeError(
        f"Failed to get latest release from github: [{response.status_code}] {response.reason}"
    )


def github_file_selector(
    user_repo: str, filter_mode: str, filter_iterable: list[str]
) -> tuple[str]:
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
        raise ValueError(
            f"Invalid Filter Mode: {filter_mode} | Valid Modes: 'add', 'remove'"
        )

    urls = []

    for file_url in github_downloads(user_repo):
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
