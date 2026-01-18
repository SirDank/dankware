# https://github.com/SirDank/dankware

"""
dankware - Python package with various features!

A utility library providing terminal coloring, multithreading helpers,
Windows registry tools, GitHub release scrapers, and more.
"""

import os
from .traceback import err
from .datetime import get_duration
from .requests import github_downloads, github_file_selector
from .ctypes import (
    is_admin,
    hide_window,
    show_window,
    hide_window_for,
    minimise_window,
    maximise_window,
    restore_window,
    get_uuid,
)
# from .tkinter import file_selector, folder_selector

__version__ = "4.0.0"

# Import colors from dedicated module (avoids circular imports)
from .colors import (  # noqa: E402
    reset,
    black,
    red,
    green,
    yellow,
    blue,
    magenta,
    cyan,
    white,
    black_bright,
    red_bright,
    green_bright,
    yellow_bright,
    blue_bright,
    magenta_bright,
    cyan_bright,
    white_bright,
    black_normal,
    red_normal,
    green_normal,
    yellow_normal,
    blue_normal,
    magenta_normal,
    cyan_normal,
    white_normal,
    black_dim,
    red_dim,
    green_dim,
    yellow_dim,
    blue_dim,
    magenta_dim,
    cyan_dim,
    white_dim,
)

from .text import clr, align, fade, random_ip  # pylint: disable=wrong-import-position # noqa: E402
from .terminal import cls, title, rm_line, sys_open  # pylint: disable=wrong-import-position # noqa: E402
from .multithread import multithread  # pylint: disable=wrong-import-position # noqa: E402

# from .pillow import splash_screen
from .winreg import get_path  # pylint: disable=wrong-import-position # noqa: E402

if os.name == "nt":
    from .winreg import export_registry_keys

# New modules exports
from .exceptions import (  # pylint: disable=wrong-import-position # noqa: E402
    DankwareError,
    UnsupportedOSError,
    RateLimitError,
    ConfigurationError,
    DownloadError,
    RegistryError,
)
from .config import configure, get_config, reset_config  # pylint: disable=wrong-import-position # noqa: E402
from .decorators import retry, timed, deprecated  # pylint: disable=wrong-import-position # noqa: E402

# Define public API
__all__ = [
    # Version
    "__version__",
    # Text utilities
    "clr",
    "align",
    "fade",
    "random_ip",
    # Terminal utilities
    "cls",
    "title",
    "rm_line",
    "sys_open",
    # Multithreading
    "multithread",
    # Error handling
    "err",
    # Datetime
    "get_duration",
    # GitHub utilities
    "github_downloads",
    "github_file_selector",
    # Windows utilities
    "is_admin",
    "hide_window",
    "show_window",
    "hide_window_for",
    "minimise_window",
    "maximise_window",
    "restore_window",
    "get_uuid",
    "get_path",
    # Configuration
    "configure",
    "get_config",
    "reset_config",
    # Decorators
    "retry",
    "timed",
    "deprecated",
    # Exceptions
    "DankwareError",
    "UnsupportedOSError",
    "RateLimitError",
    "ConfigurationError",
    "DownloadError",
    "RegistryError",
    # Colors - reset
    "reset",
    # Colors - base
    "black",
    "blue",
    "cyan",
    "green",
    "magenta",
    "red",
    "white",
    "yellow",
    # Colors - bright
    "black_bright",
    "blue_bright",
    "cyan_bright",
    "green_bright",
    "magenta_bright",
    "red_bright",
    "white_bright",
    "yellow_bright",
    # Colors - normal
    "black_normal",
    "blue_normal",
    "cyan_normal",
    "green_normal",
    "magenta_normal",
    "red_normal",
    "white_normal",
    "yellow_normal",
    # Colors - dim
    "black_dim",
    "blue_dim",
    "cyan_dim",
    "green_dim",
    "magenta_dim",
    "red_dim",
    "white_dim",
    "yellow_dim",
]

# Conditional exports
if os.name == "nt":
    __all__.append("export_registry_keys")
