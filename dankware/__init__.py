# https://github.com/SirDank/dankware

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
)
# from .tkinter import file_selector, folder_selector

from colorama import Style, Fore, init

init(autoreset=True)

# ---

reset = Style.RESET_ALL

black = Fore.BLACK
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
magenta = Fore.MAGENTA
red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW

# ---

black_bright = Style.BRIGHT + Fore.BLACK
blue_bright = Style.BRIGHT + Fore.BLUE
cyan_bright = Style.BRIGHT + Fore.CYAN
green_bright = Style.BRIGHT + Fore.GREEN
magenta_bright = Style.BRIGHT + Fore.MAGENTA
red_bright = Style.BRIGHT + Fore.RED
white_bright = Style.BRIGHT + Fore.WHITE
yellow_bright = Style.BRIGHT + Fore.YELLOW

# ---

black_normal = Style.NORMAL + Fore.BLACK
blue_normal = Style.NORMAL + Fore.BLUE
cyan_normal = Style.NORMAL + Fore.CYAN
green_normal = Style.NORMAL + Fore.GREEN
magenta_normal = Style.NORMAL + Fore.MAGENTA
red_normal = Style.NORMAL + Fore.RED
white_normal = Style.NORMAL + Fore.WHITE
yellow_normal = Style.NORMAL + Fore.YELLOW

# ---

black_dim = Style.DIM + Fore.BLACK
blue_dim = Style.DIM + Fore.BLUE
cyan_dim = Style.DIM + Fore.CYAN
green_dim = Style.DIM + Fore.GREEN
magenta_dim = Style.DIM + Fore.MAGENTA
red_dim = Style.DIM + Fore.RED
white_dim = Style.DIM + Fore.WHITE
yellow_dim = Style.DIM + Fore.YELLOW

# https://no-color.org/

if "NO_COLOR" in os.environ:
    reset = ""
    black = ""
    blue = ""
    cyan = ""
    green = ""
    magenta = ""
    red = ""
    white = ""
    yellow = ""
    black_bright = ""
    blue_bright = ""
    cyan_bright = ""
    green_bright = ""
    magenta_bright = ""
    red_bright = ""
    white_bright = ""
    yellow_bright = ""
    black_normal = ""
    blue_normal = ""
    cyan_normal = ""
    green_normal = ""
    magenta_normal = ""
    red_normal = ""
    white_normal = ""
    yellow_normal = ""
    black_dim = ""
    blue_dim = ""
    cyan_dim = ""
    green_dim = ""
    magenta_dim = ""
    red_dim = ""
    white_dim = ""
    yellow_dim = ""

from .text import clr, align, fade, random_ip  # pylint: disable=wrong-import-position # noqa: E402
from .terminal import cls, title, rm_line, sys_open  # pylint: disable=wrong-import-position # noqa: E402
from .multithread import multithread  # pylint: disable=wrong-import-position # noqa: E402

# from .pillow import splash_screen
from .winreg import get_path  # pylint: disable=wrong-import-position # noqa: E402

if os.name == "nt":
    from .winreg import export_registry_keys
