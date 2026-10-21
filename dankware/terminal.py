# https://github.com/SirDank/dankware

"""
Terminal and console utilities.
"""

import os
import subprocess
from shutil import get_terminal_size

from .colors import reset
from .exceptions import UnsupportedOSError

__all__ = ["cls", "title", "rm_line", "sys_open"]


def cls() -> None:
    """Clear screen across Windows and POSIX."""
    print(reset)
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], shell=False, check=False)
    elif os.name == "posix":
        subprocess.run(["clear"], shell=False, check=False)
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def title(title_text: str) -> None:
    """
    Change console window title.

    Args:
        title_text: The new window title.
    """
    if os.name == "nt":
        import ctypes

        ctypes.windll.kernel32.SetConsoleTitleW(title_text)
    elif os.name == "posix":
        print(f"\033]0;{title_text}\007", end="", flush=True)
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def rm_line() -> None:
    """Erase previous terminal line."""
    print("\033[A" + " " * (get_terminal_size().columns - 6) + "\033[A")


def sys_open(item: str) -> None:
    """
    Open a URL, directory, or file with the system default handler.

    Args:
        item: Path or URL to open.
    """
    if os.name == "nt":
        os.startfile(item)  # type: ignore  # Windows only
    elif os.name == "posix":
        subprocess.run(["xdg-open", item], shell=False, check=False)
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")
