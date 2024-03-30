import os
import time
from concurrent.futures import ThreadPoolExecutor

if os.name == 'nt':
    import ctypes
elif os.name == 'posix':
    import pwd # pylint: disable=import-error

def is_admin() -> bool:

    """
    Checks if executed with admin privileges and returns True if found else False
    """

    if os.name == 'nt':
        try: return ctypes.windll.shell32.IsUserAnAdmin()
        except: return False
    elif os.name == 'posix':
        return pwd.getpwuid(os.getuid())[0] in ('root', '0') # pylint: disable=no-member
    else:
        raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

'''
def run_as_admin() -> None:
    
    """
    Executes the script with admin privileges
    """
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #sys.exit(clr("\n  > Exiting original un-elevated script...",2))
'''

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hide_window() -> None:

    """
    Hides console window
    
    Related to:
        - show_window()
    """

    if os.name == 'nt':
        hWnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(hWnd, 0)
    elif os.name == 'posix':
        os.system("xdotool getactivewindow windowminimize")
    else:
        raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

def show_window() -> None:

    """
    Shows console window
    
    Related to:
        - hide_window()
    """

    if os.name == 'nt':
        hWnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(hWnd, 1)
    elif os.name == 'posix':
        os.system("xdotool getactivewindow windowactivate")
    else:
        raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

def hide_window_for(duration: int = 3) -> None:

    """
    Hides console window for the given duration
    
    Related to:
        - hide_window()
        - show_window()
    """

    def tmp():
        hide_window()
        time.sleep(duration)
        show_window()

    ThreadPoolExecutor(1).submit(tmp)

def minimise_window() -> None:

    """
    Minimises console window
    
    Related to:
        - maximise_window()
        - restore_window()
    """

    if os.name == 'nt':
        user32 = ctypes.WinDLL('user32')
        user32.ShowWindow(user32.GetForegroundWindow(), 6)
    elif os.name == 'posix':
        os.system("xdotool getactivewindow windowminimize")
    else:
        raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

def maximise_window() -> None:

    """
    Maximises console window
    
    Related to:
        - minimise_window()
        - restore_window()
    """

    if os.name == 'nt':
        user32 = ctypes.WinDLL('user32')
        user32.ShowWindow(user32.GetForegroundWindow(), 3)
    elif os.name == 'posix':
        os.system("xdotool getactivewindow windowactivate windowmaximize")
    else:
        raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

def restore_window() -> None:

    """
    Restores console window to its original size
    
    Related to:
        - minimise_window()
        - maximise_window()
    """

    if os.name == 'nt':
        user32 = ctypes.WinDLL('user32')
        user32.ShowWindow(user32.GetForegroundWindow(), 9)
    elif os.name == 'posix':
        os.system("xdotool getactivewindow windowactivate windowrestore")
    else:
        raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")
