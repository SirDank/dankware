# https://github.com/SirDank/dankware

"""
System information utilities for dankware.
"""

import os
import platform
from typing import Optional


def get_system_info() -> dict[str, str]:
    """
    Get comprehensive system information.

    Returns:
        Dictionary containing system information.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.system import get_system_info

    info = get_system_info()
    print(info["platform"])  # "Windows" or "Linux"
    ```
    """
    return {
        "os": os.name,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
    }


def is_windows() -> bool:
    """Check if running on Windows."""
    return os.name == "nt"


def is_linux() -> bool:
    """Check if running on Linux."""
    return os.name == "posix" and platform.system() == "Linux"


def is_macos() -> bool:
    """Check if running on macOS."""
    return os.name == "posix" and platform.system() == "Darwin"


def is_64bit() -> bool:
    """Check if running on 64-bit architecture."""
    return platform.machine().endswith("64")


def get_environment(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Safely get an environment variable.

    Args:
        key: Environment variable name.
        default: Default value if not found.

    Returns:
        The environment variable value or default.
    """
    return os.environ.get(key, default)


def set_environment(key: str, value: str) -> None:
    """
    Set an environment variable.

    Args:
        key: Environment variable name.
        value: Value to set.
    """
    os.environ[key] = value


def get_username() -> str:
    """
    Get the current username.

    Returns:
        Current username.
    """
    if os.name == "nt":
        return os.environ.get("USERNAME", "unknown")
    return os.environ.get("USER", "unknown")


def get_home_dir() -> str:
    """
    Get the user's home directory.

    Returns:
        Path to home directory.
    """
    return os.path.expanduser("~")


def get_temp_dir() -> str:
    """
    Get the system temporary directory.

    Returns:
        Path to temp directory.
    """
    import tempfile

    return tempfile.gettempdir()
