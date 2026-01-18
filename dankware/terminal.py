import os
import subprocess
from . import reset
from shutil import get_terminal_size

from .exceptions import UnsupportedOSError


def cls() -> None:
    """
    Clear screen for multi-os
    """

    print(reset)
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], shell=False, check=False)
    elif os.name == "posix":
        subprocess.run(["clear"], shell=False, check=False)
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def title(title_text: str) -> None:
    """
    Changes console window title

    Args:
        title_text: The new window title.
    """

    if os.name == "nt":
        # Use ctypes for more reliable title setting on Windows
        import ctypes

        ctypes.windll.kernel32.SetConsoleTitleW(title_text)
    elif os.name == "posix":
        # Use ANSI escape sequence for terminal title
        print(f"\033]0;{title_text}\007", end="", flush=True)
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def rm_line() -> None:
    """
    Deletes previous line
    """

    print("\033[A" + " " * (get_terminal_size().columns - 6) + "\033[A")


def sys_open(item: str) -> None:
    """
    Can do the following:
    - Open the url on the default browser on windows / linux
    - Open directory
    - Start file

    Args:
        item: Path to file/directory or URL to open.
    """

    if os.name == "nt":
        # Use os.startfile on Windows for better security
        os.startfile(item)  # type: ignore  # Windows only
    elif os.name == "posix":
        subprocess.run(["xdg-open", item], shell=False, check=False)
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")
