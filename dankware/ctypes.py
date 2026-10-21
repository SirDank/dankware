# https://github.com/SirDank/dankware

"""
Window manipulation and system privilege utilities.
"""

import os
import threading
import time
from subprocess import DEVNULL, STDOUT, check_output

from .exceptions import UnsupportedOSError

if os.name == "nt":
    import ctypes

__all__ = [
    "is_admin",
    "hide_window",
    "show_window",
    "hide_window_for",
    "minimise_window",
    "maximise_window",
    "restore_window",
    "get_uuid",
]


def is_admin() -> bool:
    """
    Check if the script is running with administrator/root privileges.

    Returns:
        bool: True if elevated, False otherwise.
    """
    if os.name == "nt":
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except Exception:
            return False
    elif os.name == "posix":
        from pwd import getpwuid

        return getpwuid(os.getuid())[0] in ("root", "0")
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def hide_window() -> None:
    """Hide the console window."""
    if os.name == "nt":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)
    elif os.name == "posix":
        os.system("xdotool getactivewindow windowminimize")
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def show_window() -> None:
    """Show the console window."""
    if os.name == "nt":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 1)
    elif os.name == "posix":
        os.system("xdotool getactivewindow windowactivate")
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def hide_window_for(duration: int | float = 3) -> None:
    """
    Hide the console window asynchronously for the given duration in seconds.

    Args:
        duration: Duration in seconds to stay hidden.
    """

    def _worker():
        hide_window()
        time.sleep(duration)
        show_window()

    thread = threading.Thread(target=_worker, daemon=True)
    thread.start()


def minimise_window() -> None:
    """Minimise the console window."""
    if os.name == "nt":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 6)
    elif os.name == "posix":
        os.system("xdotool getactivewindow windowminimize")
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def maximise_window() -> None:
    """Maximise the console window."""
    if os.name == "nt":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 3)
    elif os.name == "posix":
        os.system("xdotool getactivewindow windowactivate windowmaximize")
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def restore_window() -> None:
    """Restore the console window to its original size."""
    if os.name == "nt":
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 9)
    elif os.name == "posix":
        os.system("xdotool getactivewindow windowactivate windowrestore")
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def get_uuid() -> str:
    """
    Get system UUID.

    Returns:
        str: System UUID string.
    """
    if os.name == "nt":
        return str(
            check_output(
                [
                    "powershell.exe",
                    "-ExecutionPolicy",
                    "bypass",
                    "-command",
                    "(Get-CimInstance -Class Win32_ComputerSystemProduct).UUID",
                ],
                stderr=STDOUT,
                stdin=DEVNULL,
                creationflags=0x08000000,
            )
            .decode()
            .strip()
        )
    elif os.name == "posix":
        return str(
            check_output(
                ["sudo", "dmidecode", "-s", "system-uuid"],
                stderr=STDOUT,
                stdin=DEVNULL,
            )
            .decode()
            .strip()
        )
    else:
        raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")
