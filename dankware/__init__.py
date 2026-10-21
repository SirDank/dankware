# https://github.com/SirDank/dankware

"""
dankware - Python package with various features!

A utility library providing terminal coloring, multithreading helpers,
file utilities, downloaders, Windows tools, and GitHub release scrapers.
"""

import os

from .colors import (
    black,
    black_bright,
    black_dim,
    black_normal,
    blue,
    blue_bright,
    blue_dim,
    blue_normal,
    cyan,
    cyan_bright,
    cyan_dim,
    cyan_normal,
    green,
    green_bright,
    green_dim,
    green_normal,
    magenta,
    magenta_bright,
    magenta_dim,
    magenta_normal,
    red,
    red_bright,
    red_dim,
    red_normal,
    reset,
    white,
    white_bright,
    white_dim,
    white_normal,
    yellow,
    yellow_bright,
    yellow_dim,
    yellow_normal,
)
from .ctypes import (
    get_uuid,
    hide_window,
    hide_window_for,
    is_admin,
    maximise_window,
    minimise_window,
    restore_window,
    show_window,
)
from .datetime import get_duration
from .decorators import retry
from .download import download_file, download_multiple
from .exceptions import (
    DankwareError,
    DownloadError,
    RateLimitError,
    UnsupportedOSError,
)
from .files import (
    ensure_dir,
    get_file_hash,
    human_readable_size,
    list_files,
    safe_filename,
)
from .multithread import multithread
from .requests import (
    github_check_update,
    github_downloads,
    github_file_selector,
    github_get_raw_file,
    github_release_info,
)
from .terminal import cls, rm_line, sys_open, title
from .text import align, clr, fade, random_ip
from .traceback import err
from .winreg import get_path

if os.name == "nt":
    from .winreg import export_registry_keys as export_registry_keys

__version__ = "4.0.0"

__all__ = [
    "__version__",
    # Text
    "clr",
    "align",
    "fade",
    "random_ip",
    # Terminal
    "cls",
    "title",
    "rm_line",
    "sys_open",
    # Multithreading
    "multithread",
    # Error traceback
    "err",
    # Datetime
    "get_duration",
    # GitHub
    "github_downloads",
    "github_file_selector",
    "github_release_info",
    "github_check_update",
    "github_get_raw_file",
    # Files
    "get_file_hash",
    "ensure_dir",
    "safe_filename",
    "human_readable_size",
    "list_files",
    # Downloads
    "download_file",
    "download_multiple",
    # Decorators
    "retry",
    # Exceptions
    "DankwareError",
    "UnsupportedOSError",
    "RateLimitError",
    "DownloadError",
    # System / Windows ctypes
    "is_admin",
    "hide_window",
    "show_window",
    "hide_window_for",
    "minimise_window",
    "maximise_window",
    "restore_window",
    "get_uuid",
    "get_path",
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

if os.name == "nt":
    __all__.append("export_registry_keys")
