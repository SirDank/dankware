###################################################################################

#                            https://github.com/SirDank                            

###################################################################################

from .traceback import err
from .datetime import get_duration
from .requests import github_downloads, github_file_selector
from .ctypes import is_admin, hide_window, show_window, hide_window_for, minimise_window, maximise_window, restore_window
#from .tkinter import file_selector, folder_selector

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

black_dim = Style.DIM + Fore.BLACK
blue_dim = Style.DIM + Fore.BLUE
cyan_dim = Style.DIM + Fore.CYAN
green_dim = Style.DIM + Fore.GREEN
magenta_dim = Style.DIM + Fore.MAGENTA
red_dim = Style.DIM + Fore.RED
white_dim = Style.DIM + Fore.WHITE
yellow_dim = Style.DIM + Fore.YELLOW

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

black_bright = Style.BRIGHT + Fore.BLACK
blue_bright = Style.BRIGHT + Fore.BLUE
cyan_bright = Style.BRIGHT + Fore.CYAN
green_bright = Style.BRIGHT + Fore.GREEN
magenta_bright = Style.BRIGHT + Fore.MAGENTA
red_bright = Style.BRIGHT + Fore.RED
white_bright = Style.BRIGHT + Fore.WHITE
yellow_bright = Style.BRIGHT + Fore.YELLOW

from .text import clr, align, fade, random_ip
from .terminal import cls, title, rm_line, sys_open
from .multithread import multithread
#from .pillow import splash_screen
from .winreg import get_path

import os
if os.name == 'nt':
    from .winreg import export_registry_keys
