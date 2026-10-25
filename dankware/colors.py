# https://github.com/SirDank/dankware

"""
ANSI color codes for dankware.

This module provides color constants using native ANSI escape codes,
respecting the NO_COLOR environment variable.
"""

import os
import sys

# Enable ANSI escape codes on Windows
if sys.platform == "win32":
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        # Enable ENABLE_VIRTUAL_TERMINAL_PROCESSING
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

# ---
# ANSI Escape Codes - Clean implementation with NO_COLOR support
# https://no-color.org/
# ---

_NO_COLOR = "NO_COLOR" in os.environ


def _color(code: str) -> str:
    """Return ANSI code respecting NO_COLOR environment variable."""
    return "" if _NO_COLOR else code


# Reset
reset = _color("\033[0m")

# Base colors (normal intensity)
black = _color("\033[30m")
red = _color("\033[31m")
green = _color("\033[32m")
yellow = _color("\033[33m")
blue = _color("\033[34m")
magenta = _color("\033[35m")
cyan = _color("\033[36m")
white = _color("\033[37m")

# Bright colors (high intensity)
black_bright = _color("\033[1;30m")
red_bright = _color("\033[1;31m")
green_bright = _color("\033[1;32m")
yellow_bright = _color("\033[1;33m")
blue_bright = _color("\033[1;34m")
magenta_bright = _color("\033[1;35m")
cyan_bright = _color("\033[1;36m")
white_bright = _color("\033[1;37m")

# Normal intensity (explicitly set)
black_normal = _color("\033[22;30m")
red_normal = _color("\033[22;31m")
green_normal = _color("\033[22;32m")
yellow_normal = _color("\033[22;33m")
blue_normal = _color("\033[22;34m")
magenta_normal = _color("\033[22;35m")
cyan_normal = _color("\033[22;36m")
white_normal = _color("\033[22;37m")

# Dim colors (low intensity)
black_dim = _color("\033[2;30m")
red_dim = _color("\033[2;31m")
green_dim = _color("\033[2;32m")
yellow_dim = _color("\033[2;33m")
blue_dim = _color("\033[2;34m")
magenta_dim = _color("\033[2;35m")
cyan_dim = _color("\033[2;36m")
white_dim = _color("\033[2;37m")
