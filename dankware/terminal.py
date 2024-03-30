import os
from . import reset
from shutil import get_terminal_size

def cls() -> None:

    """
    Clear screen for multi-os
    """

    print(reset)
    if os.name == 'nt': _ = os.system('cls')
    elif os.name == 'posix': _ = os.system('clear')
    else: raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

def title(title: str) -> None:

    """
    Changes console window title
    """

    if os.name == 'nt': os.system(f"title {title}")
    elif os.name == 'posix': os.system(f"xdotool getactivewindow set_window --name {title}")
    else: raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

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
    """

    if os.name == 'nt': os.system(f'start {item}')
    elif os.name == 'posix': os.system(f'xdg-open {item}')
    else: raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")
