"""
> Please read the documentation on https://github.com/SirDank/dankware before using this module!
"""

###################################################################################

#                            https://github.com/SirDank                            

###################################################################################

import os
import sys
import time
import random
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# colorama colours
reset = Style.RESET_ALL

black = Fore.BLACK + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT

black_normal = Fore.BLACK + Style.NORMAL
blue_normal = Fore.BLUE + Style.NORMAL
cyan_normal = Fore.CYAN + Style.NORMAL
green_normal = Fore.GREEN + Style.NORMAL
magenta_normal = Fore.MAGENTA + Style.NORMAL
red_normal = Fore.RED + Style.NORMAL
white_normal = Fore.WHITE + Style.NORMAL
yellow_normal = Fore.YELLOW + Style.NORMAL

black_dim = Fore.BLACK + Style.DIM
blue_dim = Fore.BLUE + Style.DIM
cyan_dim = Fore.CYAN + Style.DIM
green_dim = Fore.GREEN + Style.DIM
magenta_dim = Fore.MAGENTA + Style.DIM
red_dim = Fore.RED + Style.DIM
white_dim = Fore.WHITE + Style.DIM
yellow_dim = Fore.YELLOW + Style.DIM

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def multithread(function: callable, threads: int = 1, *args, progress_bar: bool = True) -> None:
    
    """
    Run the given function in multiple threads with the specified inputs.
    
    ________________________________________________________________________

    - function: The function to run in multiple threads.
    - threads: The number of threads to use.
    - *args: Input(s) for the function. Can be a tuple / list / single value.
    - progress_bar: Whether to display a progress bar.
    """
    
    from rich.live import Live
    from rich.panel import Panel
    from rich.table import Table
    from shutil import get_terminal_size
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn, TimeElapsedColumn


    try:
        
        if threads < 1:
            raise ValueError("The number of threads must be a positive integer!")

        executor = ThreadPoolExecutor(max_workers=threads)

        if not args:
            futures = tuple(executor.submit(function) for _ in range(threads))
        else:

            input_lists = []

            for arg in args:
                if isinstance(arg, list) or isinstance(arg, tuple):
                    input_lists.append(arg)
                else:
                    input_lists.append([arg] * threads)
                
            futures = tuple(executor.submit(function, *task_args) for task_args in zip(*input_lists))
            
            del input_lists

        if progress_bar:
            width = get_terminal_size().columns
            job_progress = Progress("{task.description}", SpinnerColumn(), BarColumn(bar_width=width), TextColumn("[progress.percentage][bright_green]{task.percentage:>3.0f}%"), "[bright_cyan]ETA", TimeRemainingColumn(), TimeElapsedColumn())
            overall_task = job_progress.add_task("[bright_green]Progress", total=int(len(futures)))
            progress_table = Table.grid()
            progress_table.add_row(Panel.fit(job_progress, title="[bright_white]Jobs", border_style="bright_red", padding=(1, 2)))

            with Live(progress_table, refresh_per_second=10):
                while not job_progress.finished:
                    time.sleep(0.1)
                    for future in as_completed(futures):
                        if future.done():
                            try: future.result()
                            except: pass
                            job_progress.advance(overall_task)

        else:
            for future in as_completed(futures):
                if future.done():
                    try: future.result()
                    except: pass
                
    except: 
        try: executor.shutdown()
        except: pass
        sys.exit(clr(err(sys.exc_info()),2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def github_downloads(user_repo: str) -> tuple:

    """
    Extracts direct download urls from the latest release on github and returns it as a tuple

    - Example Input: USER_NAME/REPO_NAME ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    - Example Output: ['https://github.com/USER_NAME/REPO_NAME/releases/download/VERSION/EXAMPLE.TXT']
    
    _____________________________________________________________________________________________________________________________________
    
    [ EXAMPLE ]
    ```python
    from dankware import github_downloads
    for _ in github_downloads("SirDank/dank.tool"): print(_)
    ```
    """
    
    import requests

    while True:
        try: response = requests.get(f"https://api.github.com/repos/{user_repo}/releases/latest").json(); break
        except: input(clr("  > Make sure you are connected to the Internet! Press [ENTER] to try again... ",2))
    
    return tuple(data["browser_download_url"] for data in response["assets"])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def github_file_selector(user_repo: str, filter_mode: str, name_iterable: tuple) -> tuple:
    
    """
    
    This function is used to filter the output from github_downloads()
    
    - user_repo = 'USER_NAME/REPO_NAME' ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    - filter_mode = 'add' or 'remove'
    - name_iterable = tuple of names to be added or removed
    
    _______________________________________________________________________________________________________________________________________________________________________
    
    [ EXAMPLE ]
    ```python
    from dankware import github_file_selector
    for file_url in github_file_selector("EssentialsX/Essentials", "remove", ('AntiBuild', 'Discord', 'GeoIP', 'Protect', 'XMPP')):
        print(file_url)
    ```
    
    _______________________________________________________________________________________________________________________________________________________________________
    
    Example output from github_downloads("EX_USER/EX_REPO"): [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
    ]
    
    _______________________________________________________________________________________________________________________________________________________________________
    
    Example Input: "EX_USER/EX_REPO", "add", ("EXAMPLE")
        
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
    ]
        
    - Note: Only urls with filenames containing "EXAMPLE" were returned.

    _______________________________________________________________________________________________________________________________________________________________________

    Example Input: "EX_USER/EX_REPO", "remove", ("EXAMPLE")
    
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
    ]
    
    - Note: Only urls with filenames not containing "EXAMPLE" were returned.
    
    """

    urls = []

    for file_url in github_downloads(user_repo):

        if filter_mode == "add":
            valid = False
        elif filter_mode == "remove":
            valid = True
        for name in name_iterable:
            if name in file_url.split('/')[-1]:
                valid = not valid
        if valid:
            urls.append(file_url)

    return tuple(urls)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_ip() -> str:
    
    """
    Generates a random valid computer ip
    - Follows: https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf
    """

    excluded_prefixes_one = {'22', '10', '205', '30', '11', '55', '215', '29', '7', '6', '26', '214', '33', '21', '28', '127', '136'}
    excluded_prefixes_two = {'161.73', '141.163', '143.52', '149.155', '139.222', '137.253', '157.228', '140.97', '146.87', '198.18', '129.169', '50.117', '146.227', '144.32', '134.83', '139.153', '160.5', '194.66', '212.219', '146.191', '129.11', '149.170', '129.67', '138.253', '134.36', '205.164', '192.177', '134.225', '139.133', '152.71', '136.148', '158.223', '137.222', '130.209', '172.252', '143.210', '164.11', '128.41', '147.143', '158.94', '192.168', '138.250', '158.125', '81.87', '134.219', '143.234', '144.82', '152.78', '128.243', '100.64', '130.246', '137.195', '152.105', '150.204', '141.241', '143.167', '139.166', '144.39', '161.74', '147.197', '163.160', '161.112', '136.156', '137.44', '143.117', '129.12', '134.220', '166.88', '134.151', '131.231', '31.25', '129.215', '153.11', '128.40', '142.111', '23.27', '75.127', '144.173', '148.79', '74.115', '192.186', '163.1', '146.176', '193.60', '129.123', '212.121', '142.252', '165.160', '146.97', '148.197', '131.251', '137.108', '163.167', '129.31', '163.119', '194.80', '130.88', '137.73', '147.188', '137.50', '130.159', '131.111', '148.88', '129.234', '131.227', '155.245', '159.92', '146.179', '169.254', '138.40', '144.124', '155.198', '139.184', '128.232', '157.140', '128.240', '158.143', '161.76', '195.194', '138.38', '128.86', '160.9', '146.169', '128.16'}
    excluded_prefixes_three = {'8.17.250', '194.36.2', '199.187.168', '192.173.1', '216.151.190', '193.32.22', '72.52.76', '50.93.194', '178.18.29', '74.82.43', '192.84.75', '199.255.208', '208.80.4', '198.12.120', '192.153.213', '8.14.146', '64.158.146', '69.176.80', '192.160.194', '68.68.96', '23.231.128', '173.245.194', '192.84.212', '193.107.116', '198.12.121', '192.41.112', '8.12.162', '216.172.128', '108.171.52', '192.84.76', '173.252.192', '74.122.100', '50.93.197', '141.170.100', '192.173.128', '74.115.2', '209.107.212', '192.195.118', '178.18.28', '192.133.244', '192.68.153', '192.108.120', '194.35.186', '209.107.192', '192.173.4', '194.35.241', '204.113.91', '192.35.172', '193.37.225', '199.33.120', '108.171.32', '209.54.48', '203.12.6', '50.93.196', '50.93.195', '199.48.147', '50.115.128', '192.84.5', '192.171.128', '8.14.84', '192.88.99', '216.218.233', '194.35.192', '192.76.16', '64.145.82', '185.83.168', '74.114.88', '193.37.240', '66.79.160', '69.46.64', '193.39.172', '204.74.208', '192.92.114', '192.84.80', '132.206.125', '194.60.218', '198.144.240', '63.141.222', '192.149.111', '208.123.223', '192.156.162', '192.155.160', '193.39.80', '192.195.105', '50.118.128', '38.72.200', '146.82.55.93', '192.94.235', '132.206.9', '8.14.147', '8.17.251', '192.190.201', '132.206.123', '192.250.240', '50.93.192', '74.115.4', '141.170.96', '192.107.168', '178.18.27', '193.138.86', '198.51.100', '192.100.154', '206.108.52', '74.82.160', '192.76.8', '192.76.32', '37.72.112', '192.88.10', '194.36.121', '205.159.189', '192.18.195', '149.54.152', '103.251.91', '192.195.42', '194.110.214', '199.33.124', '204.16.192', '192.100.78', '178.18.26', '194.35.93', '37.72.172', '208.77.40', '64.92.96', '212.121.192', '192.76.6', '192.249.64', '192.124.46', '211.156.110', '159.86.128', '192.173.2', '192.171.192', '85.12.64', '89.207.208', '199.188.238', '108.171.62', '64.62.253', '31.25.4', '72.13.80', '118.193.78', '8.12.164', '65.162.192', '65.49.24', '130.93.16', '205.209.128', '141.170.64', '50.93.193', '192.150.180', '192.190.202', '5.152.179', '192.150.184', '173.245.64', '209.107.210', '206.165.4', '192.41.128', '65.49.93', '183.182.22', '193.133.28', '199.68.196', '198.12.122', '192.88.9', '209.51.185', '192.12.72', '193.38.143', '149.54.136', '216.151.183', '216.224.112', '192.188.157', '194.36.152', '192.188.158', '31.25.2', '8.17.252', '108.171.42', '192.41.104', '199.127.240', '64.145.79', '193.39.212', '216.185.36', '194.187.32', '8.12.163', '178.18.16', '204.19.238', '173.245.220', '8.14.145', '92.245.224', '192.82.153', '4.53.201', '194.32.32', '192.195.116', '46.254.200', '194.36.1', '66.160.191', '204.13.64', '193.130.15'}
    
    while True:
        
        first_octet = random.randint(1, 223)
        if f"{first_octet}" in excluded_prefixes_one: continue
        
        second_octet = random.randint(0, 255)
        if f"{first_octet}.{second_octet}" in excluded_prefixes_two: continue
        
        third_octet = random.randint(0, 255)
        if f"{first_octet}.{second_octet}.{third_octet}" in excluded_prefixes_three: continue
        
        fourth_octet = random.randint(0, 255)
        
        if first_octet == 172 and second_octet >= 16 and second_octet <= 31: continue
        elif first_octet == 192:
            if fourth_octet == 170 or fourth_octet == 171 or third_octet == 2: continue
        elif first_octet == 203 and third_octet == 113: continue
        elif first_octet == 216 and second_octet == 83 and third_octet >= 33 and third_octet <= 63: continue
        elif second_octet == 255 and third_octet == 255 and third_octet == 255: continue

        break
        
    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_admin() -> bool:
    
    """
    Checks if executed with admin privileges and returns True if found else False
    """
    
    if os.name == 'nt':
        import ctypes
        try: return ctypes.windll.shell32.IsUserAnAdmin()
        except: return False
    else: return os.getuid() == 0
    
'''
def run_as_admin() -> None:
    
    """
    Executes the script with admin privileges
    """
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #sys.exit(clr("\n  > Exiting original un-elevated script...",2))
'''

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def export_registry_keys(registry_root: str, registry_path: str, recursive: bool = True, export_path: str = "export.reg", verbose: bool = True) -> None:

    """
    Function to export registry keys with or without its subkeys and saves them to export_path
    - Examples for registry_root: 'HKEY_CLASSES_ROOT', 'HKEY_CURRENT_USER', 'HKEY_LOCAL_MACHINE', 'HKEY_USERS', 'HKEY_CURRENT_CONFIG'
    - Example for registry_path: r'Software\Google\Chrome\PreferenceMACs'
    - recursive: True (subkeys saved)
    - recursive: False (subkeys not saved)
    - export_path: "exported.reg" (default)
    
    _______________________________________________________________________________________________________________________________________________________________________
    
    [ EXAMPLE ]
    
    ```python
    from dankware import export_registry_keys
    export_registry_keys('HKEY_CURRENT_USER', r'Software\Google\Chrome\PreferenceMACs')
    ```
    """
    
    if os.name != 'nt':
        raise RuntimeError("This function can only be used on Windows!")

    import winreg
    
    try:
    
        key_data = []
        key_map = {
            'HKEY_CLASSES_ROOT': winreg.HKEY_CLASSES_ROOT,
            'HKEY_CURRENT_USER': winreg.HKEY_CURRENT_USER,
            'HKEY_LOCAL_MACHINE': winreg.HKEY_LOCAL_MACHINE,
            'HKEY_USERS': winreg.HKEY_USERS,
            'HKEY_CURRENT_CONFIG': winreg.HKEY_CURRENT_CONFIG,
        }
        
        if not export_path.endswith('.reg'):
            raise ValueError("Invalid Export Path! export_path must end with '.reg'")
        if registry_root not in key_map.keys():
            raise ValueError(f"Invalid Registry Root: {registry_root} | Valid Roots: {', '.join(key_map.keys())}")
        if not is_admin():
            raise RuntimeError("Current user is not an administrator! Exporting registry keys requires admin privileges!")
            # If the current user is not an admin, relaunch the script with admin privileges
            #run_as_admin()
            
        def exporter(key, registry_root, subkey_path, key_data, recursive) -> None:

            subkey = winreg.OpenKey(key, subkey_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            subkey_count = winreg.QueryInfoKey(subkey)[0]
            key_data.append(f'[{registry_root}\\{subkey_path}]')
    
            for i in range(winreg.QueryInfoKey(subkey)[1]):
                value_name, value_data, value_type = winreg.EnumValue(subkey, i)
                key_data.append(f'"{value_name}"="{value_data}"')

            key_data.append('')
            for i in range(subkey_count):
                subkey_name = winreg.EnumKey(subkey, i)
                subkey_full_path = subkey_path + '\\' + subkey_name if subkey_path else subkey_name
                if recursive: exporter(key, registry_root, subkey_full_path, key_data, recursive)

            winreg.CloseKey(subkey)

        key = key_map[registry_root]
        exporter(key, registry_root, registry_path, key_data, recursive)
        open(export_path, 'w', encoding='utf-16').write('Windows Registry Editor Version 5.00\n\n' + '\n'.join(key_data))
        
        if verbose:
            print(clr(f"\n  > Successfully exported registry keys to \"{os.path.join(os.getcwd(), 'export.reg') if export_path == 'export.reg' else export_path}\""))
    
    except: sys.exit(clr(err(sys.exc_info()),2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clr(text: str, preset: int = 1, colour_one: str = white, colour_two: str = red, colours: tuple = ()) -> str:
    
    """
    
    this function colours special characters inside the 'symbols' tuple
    
    ___________________________________________
    
    - preset: 1 | to display general text (default)
    - text = white (default) / specified colour
    - spl = red (default) / specified colour

    ___________________________________________

    - preset: 2 | to display error messages
    - text = red (fixed colour)
    - spl = white (fixed colour)

    ___________________________________________

    - preset: 3
    - text = random (fixed colour)
    - spl = white (fixed colour)

    ___________________________________________

    - preset: 4 | to display banners
    - text & spl = random (default) / colours inside input tuple
    
    """
    
    symbols = ('[', ']', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~')
    
    words_green = ('true', 'True', 'TRUE', 'online', 'Online', 'ONLINE', 'successfully', 'Successfully', 'SUCCESSFULLY', 'successful', 'Successful', 'SUCCESSFUL', 'success', 'Success', 'SUCCESS')
    words_red = ('falsely', 'Falsely', 'FALSELY', 'false', 'False', 'FALSE', 'offline', 'Offline', 'OFFLINE', 'failures', 'Failures', 'FAILURES', 'failure', 'Failure', 'FAILURE', 'failed', 'Failed', 'FAILED', 'fail', 'Fail', 'FAIL')
    
    colours_to_replace = (Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW, Style.BRIGHT, Style.RESET_ALL)
    colours_alt = ("BBLACKK", "BBLUEE", "CCYANN", "GGREENN", "MMAGENTAA", "RREDD", "WWHITEE", "YYELLOWW", "BBRIGHTT", "RRESETT")

    #styles = (Style.BRIGHT, Style.DIM, Style.NORMAL)
    
    try:
        if preset not in [3, 4]:
            for _ in range(len(colours_to_replace)):
                text = text.replace(colours_to_replace[_], colours_alt[_])
        else:
            for _ in range(len(colours_to_replace)):
                text = text.replace(colours_to_replace[_], '')

        # default

        if preset == 1:
            for symbol in symbols:
                text = text.replace(symbol, f"{colour_two}{symbol}{colour_one}")
            for word in words_green:
                replacement = green.join(list(word))
                text = text.replace(word, f"{green}{replacement}{colour_one}")
            for word in words_red:
                replacement = red.join(list(word))
                text = text.replace(word, f"{red}{replacement}{colour_one}")
        
        # for error messages
        
        elif preset == 2:
            for symbol in symbols:
                text = text.replace(symbol, f"{white}{symbol}{red}")
            for word in words_green:
                replacement = green.join(list(word))
                text = text.replace(word, f"{green}{replacement}{red}")
        
        # random | TRUE, FALSE will not be coloured!
        
        elif preset in (3, 4):

            text = list(text)
            
            if preset == 3: colour_spl = True
            elif preset == 4: colour_spl = False
            
            if colours == ():
                codes = vars(Fore)
                colours = tuple(codes[colour] for colour in codes if colour not in ('BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET'))
    
            for _ in range(len(text)):
                char = text[_]
                if char not in (' ', '\n', '\t', '\r', '\b'):
                    if colour_spl:
                        if char in symbols:
                            text[_] = white + char
                        else:
                            text[_] = random.choice(colours) + Style.BRIGHT + char
                    else:
                        text[_] = random.choice(colours) + Style.BRIGHT + char

            text = ''.join(text)

        else: raise ValueError(f"Invalid Preset: {preset} | Valid Presets: 1, 2, 3, 4")

        if preset not in (3, 4):
            for _ in range(len(colours_to_replace)):
                text = text.replace(colours_alt[_], colours_to_replace[_])

        if preset == 1: return colour_one + text + reset
        elif preset == 2: return red + text + reset
        elif preset == 3 or preset == 4: return text + reset
    
    except: sys.exit(clr(err(sys.exc_info()),2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def align(text: str) -> str: 
    
    """
    center align banner / line ( supports both coloured and non-coloured )
    - [NOTE] align supports: clr, does not support: fade
    """
    
    from shutil import get_terminal_size

    width = get_terminal_size().columns
    aligned = text
    
    for _ in tuple(vars(Fore).values()) + tuple(vars(Style).values()):
        aligned = aligned.replace(_,'')
    
    text = text.splitlines()
    aligned = aligned.splitlines()
    
    for _ in range(len(aligned)):
        aligned[_] = aligned[_].center(width).replace(aligned[_],text[_])

    return str('\n'.join(aligned) + reset)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fade(text: str, colour: str = "pink2red") -> str:
    
    """
    credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3
    - available_colours: [
        random,
        black2white,
        black2white-v,
        yellow2red,
        yellow2red-v,
        green2yellow,
        green2yellow-v,
        green2cyan,
        green2cyan-v,
        blue2cyan,
        blue2cyan-v,
        blue2pink,
        blue2pink-v,
        pink2red,
        pink2red-v,
    ]
    
    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware import fade
    # define banner
    print(fade(banner,"pink2red-v"))
    ```
    """
    
    available_colours = (
        "random",
        "black2white",
        "black2white-v",
        "yellow2red",
        "yellow2red-v",
        "green2yellow",
        "green2yellow-v",
        "green2cyan",
        "green2cyan-v",
        "blue2cyan",
        "blue2cyan-v",
        "blue2pink",
        "blue2pink-v",
        "pink2red",
        "pink2red-v",
    )

    try:
        colour = colour.lower()
        if not colour in available_colours: raise ValueError(f"Invalid Colour: {colour} | Available Colours: {', '.join(available_colours)}")
            
        faded = ""
        if len(text.splitlines()) > 1: multi_line = True
        else: multi_line = False
        
        if colour == "random":
            for line in text.splitlines():
                for char in line:
                    R, G, B = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                    faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
                if multi_line: faded += "\n"

        elif colour == "black2white":
            for line in text.splitlines():
                R = 0; G = 0; B = 0
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    if not R == 255 and not G == 255 and not B == 255:
                        R += shift; G += shift; B += shift
                        if R > 255 and G > 255 and B > 255:
                            R = 255; G = 255; B = 255
                    faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
                if multi_line: faded += "\n"
                
        elif colour == "black2white-v":
            R = 0; G = 0; B = 0
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += (f"\033[38;2;{R};{G};{B}m{line}\033[0m")
                if not R == 255 and not G == 255 and not B == 255:
                    R += shift; G += shift; B += shift
                    if R > 255 and G > 255 and B > 255:
                        R = 255; G = 255; B = 255
                if multi_line: faded += "\n"
     
        elif colour == "yellow2red":
            for line in text.splitlines():
                G = 255
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    if not G == 0:
                        G -= shift
                        if G < 0:
                            G = 0
                    faded += f"\033[38;2;255;{G};0m{char}\033[0m"
                if multi_line: faded += "\n"
        
        elif colour == "yellow2red-v":
            G = 255
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += f"\033[38;2;255;{G};0m{line}\033[0m"
                if not G == 0:
                    G -= shift
                    if G < 0:
                        G = 0
                if multi_line:faded += "\n"
                
        elif colour == "green2yellow":
            for line in text.splitlines():
                R = 0
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    if not R == 255:
                        R += shift
                        if R > 255:
                            R = 255
                    faded += f"\033[38;2;{R};255;0m{char}\033[0m"
                if multi_line: faded += "\n"
        
        elif colour == "green2yellow-v":
            R = 0
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += f"\033[38;2;{R};255;0m{line}\033[0m"
                if not R == 255:
                    R += shift
                    if R > 255:
                        R = 255
                if multi_line: faded += "\n"
                
        elif colour == "green2cyan":
            for line in text.splitlines():
                B = 100
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    if not B == 255:
                        B += shift
                        if B > 255:
                            B = 255
                    faded += f"\033[38;2;0;255;{B}m{char}\033[0m"
                if multi_line: faded += "\n"
        
        elif colour == "green2cyan-v":
            B = 100
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += f"\033[38;2;0;255;{B}m{line}\033[0m"
                if not B == 255:
                    B += shift
                    if B > 255:
                        B = 255
                if multi_line: faded += "\n"

        elif colour == "blue2cyan":
            for line in text.splitlines():
                G = 0
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    if not G == 255:
                        G += shift
                        if G > 255:
                            G = 255
                    faded += f"\033[38;2;0;{G};255m{char}\033[0m"
                if multi_line: faded += "\n"
                
        elif colour == "blue2cyan-v":
            G = 10
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += f"\033[38;2;0;{G};255m{line}\033[0m"
                if not G == 255:
                    G += shift
                    if G > 255:
                        G = 255
                if multi_line: faded += "\n"
            
        elif colour == "blue2pink":
            for line in text.splitlines():
                R = 35
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    if not R == 255:
                        R += shift
                        if R > 255:
                            R = 255
                    faded += f"\033[38;2;{R};0;220m{char}\033[0m"
                if multi_line: faded += "\n"
                
        elif colour == "blue2pink-v":
            R = 40
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += f"\033[38;2;{R};0;220m{line}\033[0m"
                if not R == 255:
                    R += shift
                    if R > 255:
                        R = 255
                if multi_line: faded += "\n"
 
        elif colour == "pink2red":
            for line in text.splitlines():
                B = 255
                shift = (int(255 / len(line)) if len(line) > 0 else 5)
                for char in line:
                    faded += f"\033[38;2;255;0;{B}m{char}\033[0m"
                    if not B == 0:
                        B -= shift
                        if B < 0:
                            B = 0
                if multi_line: faded += "\n"
            
        elif colour == "pink2red-v":
            B = 255
            shift = (int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25)
            for line in text.splitlines():
                faded += f"\033[38;2;255;0;{B}m{line}\033[0m"
                if not B == 0:
                    B -= shift
                    if B < 0: B = 0
                if multi_line: faded += "\n"

        else: raise ValueError(f"Invalid Colour: {colour} | Available Colours: {', '.join(available_colours)}")
        
        if multi_line: faded = faded[:-1]
        return faded

    except: sys.exit(clr(err(sys.exc_info()),2))
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_duration(then: datetime, now: datetime = None, interval = "default"):

    """
    Returns a duration as specified by the 'interval' variable
    
    __________________________________________________________
    
    valid intervals:
    - years -> int
    - days -> int
    - hours -> int
    - minutes -> int
    - seconds -> int
    - dynamic -> str
    - dynamic-mini -> str
    - default -> str
    """
    
    if now is None: now = datetime.now()

    duration = now - then

    if interval in ("year", "years"): return int(duration.days / 365)
    elif interval in ("day", "days"): return duration.days
    elif interval in ("hour", "hours"): return int(duration.total_seconds() / 3600)
    elif interval in ("minute", "minutes"): return int(duration.total_seconds() / 60)
    elif interval in ("second", "seconds"): return int(duration.total_seconds())
    elif interval in ("dynamic", "dynamic-mini"):
        
        mini = True if interval == "dynamic-mini" else False

        seconds = duration.total_seconds()

        if seconds < 60:
            if mini: return f"{int(seconds)}s"
            else: return f"{int(seconds)} second{'s' if seconds > 1 else ''}"
        
        elif seconds < 3600:
            minutes = int(seconds / 60)
            if mini: return f"{minutes}m"
            else:return f"{minutes} minute{'s' if minutes > 1 else ''}"
        
        elif seconds < 86400:
            hours = int(seconds / 3600)
            if mini: return f"{hours}h"
            else: return f"{hours} hour{'s' if hours > 1 else ''}"
       
        elif seconds < 31536000:
            days = int(seconds / 86400)
            if mini: return f"{days}d"
            else: return f"{days} day{'s' if days > 1 else ''}"
        
        else:
            years = int(seconds / 31536000)
            if mini: return f"{years}y"
            else: return f"{years} year{'s' if years > 1 else ''}"
    
    else:

        seconds = duration.total_seconds()

        years = int(seconds / 31536000)
        days = int((seconds % 31536000) / 86400)
        hours = int((seconds % 86400) / 3600)
        minutes = int((seconds % 3600) / 60)
        seconds = int(seconds % 60)

        parts = []
        if years: parts.append(f"{years} year{'s' if years > 1 else ''}")
        if days: parts.append(f"{days} day{'s' if days > 1 else ''}")
        if hours: parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
        if minutes: parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
        if seconds: parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")

        return ", ".join(parts)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def err(exc_info, mode = "default") -> str:
    
    """
    Returns a short traceback
    
    __________________________________________

    [ EXAMPLE ]

    ```python
    import sys
    from dankware import err, clr
    
    try:
        value = 1/0
    except:
        print(clr(err(sys.exc_info()),2))
        # OR
        print(clr(err(sys.exc_info(),'mini'),2))
    ```
    """

    from traceback import extract_tb

    ex_type, ex_value, ex_traceback = exc_info
    trace_back = extract_tb(ex_traceback)
    stack_trace = []
    
    if mode == "default":

        for trace in trace_back:
            filename = trace[0]
            if filename == "<string>": filename = str(__name__)
            elif filename.endswith(".pyc"): filename = filename[:-1]
            elif filename.endswith("$py.class"): filename = filename[:-9] + ".py"
            stack_trace.append("    - File: {} | Line: {} | Function: {}{}".format(filename, trace[1], trace[2] if trace[2] != '<module>' else 'top-level', ' | ' + trace[3] if trace[3] else ''))

        report = "  > Error Type: {}".format(ex_type.__name__)
        if ex_value: report += "\n  > Error Message: \n    - {}".format(ex_value)
        report += "\n  > Error Stack Trace: \n{}".format('\n'.join(stack_trace))

    elif mode == "mini":

        for trace in trace_back:
            filename = trace[0]
            if filename == "<string>": filename = str(__name__)
            elif filename.endswith(".pyc"): filename = filename[:-1]
            elif filename.endswith("$py.class"): filename = filename[:-9] + ".py"
            stack_trace.append("    - {} | {} | {}{}".format(filename, trace[1], trace[2] if trace[2] != '<module>' else 'top-level', ' | ' + trace[3] if trace[3] else ''))

        report = "  > {}".format(ex_type.__name__)
        if ex_value: report += " | {}".format(ex_value)
        report += "\n{}".format('\n'.join(stack_trace))
        
    else:
        
        raise ValueError(f"Invalid Mode: {mode} | Valid Modes: default, mini")

    return report

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def splash_screen(img_path: str, duration: int = 3) -> None:
    
    """
    Displays a splash screen for the given duration
    - Supports: GIFs / PNGs / JPGs / BMPs / ICOs
    
    __________________________________________
    
    [ EXAMPLE ]
    
    ```python
    from concurrent.futures import ThreadPoolExecutor
    ThreadPoolExecutor().submit(splash_screen, "splash.gif", duration=3)
    ```
    """
    
    import tkinter as tk
    try:
        from PIL import Image, ImageTk
    except:
        raise ImportError("Pillow is not installed! Run 'pip install pillow' to install it!")
    
    class SplashScreen(tk.Toplevel):

        def __init__(self, img_path):
            super().__init__()
            self.img_path = img_path
            self.setup_window()
            self.load_image()
            self.animate_image()

        def setup_window(self):
            self.overrideredirect(True)
            self.wm_attributes("-topmost", True)
            #self.wm_attributes("-transparentcolor", "white")

            self.image = Image.open(self.img_path)
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            width = self.image.width
            height = self.image.height
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2

            self.geometry(f"{width}x{height}+{x}+{y}")

            self.canvas = tk.Canvas(self, bg="black", highlightthickness=0)
            self.canvas.pack()

        def load_image(self):
            if self.img_path.lower().endswith('.gif'):
                self.frames = []
                for i in range(self.image.n_frames):
                    self.image.seek(i)
                    frame = ImageTk.PhotoImage(self.image)
                    self.frames.append(frame)
            else:
                self.frames = [ImageTk.PhotoImage(self.image)]

        def animate_image(self, current_frame=0):
            self.canvas.delete(tk.ALL)
            self.canvas.config(width=self.frames[current_frame].width(), height=self.frames[current_frame].height())
            self.canvas.create_image(self.frames[current_frame].width() // 2, self.frames[current_frame].height() // 2, image=self.frames[current_frame])
            current_frame = (current_frame + 1) % len(self.frames)
            if len(self.frames) > 1:
                self.after(int(1000 / self.image.info['duration']), self.animate_image, current_frame)
    
    root = tk.Tk()
    root.withdraw()
    SplashScreen(img_path)  
    root.after(int(duration * 1000), root.quit)
    root.mainloop()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hide_window() -> None:

    """
    Hides console window
    """
    
    if os.name == 'nt':
        from ctypes import windll
        hWnd = windll.kernel32.GetConsoleWindow()
        windll.user32.ShowWindow(hWnd, 0)
    else:
        import subprocess
        subprocess.call(["xdotool", "getactivewindow", "windowminimize"])

def show_window() -> None:

    """
    Shows console window
    """
    
    if os.name == 'nt':
        from ctypes import windll
        hWnd = windll.kernel32.GetConsoleWindow()
        windll.user32.ShowWindow(hWnd, 1)
    else:
        import subprocess
        subprocess.call(["xdotool", "getactivewindow", "windowactivate"])
    
def hide_window_for(duration: int = 3) -> None:
    
    """
    Hides console window for the given duration
    """

    from concurrent.futures import ThreadPoolExecutor
    
    def tmp():
        hide_window()
        time.sleep(duration)
        show_window()
    
    ThreadPoolExecutor(10).submit(tmp)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def file_selector(title: str = "Select File", icon_path: str = "") -> str:
    
    """
    Opens file selector and returns selected file path
    - Allows custom title and icon
    """
    
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    root = Tk()
    root.withdraw()
    if icon_path: root.iconbitmap(icon_path)
    file_path = askopenfilename(title=title)
    return file_path.replace("/", "\\")

def folder_selector(title: str = "Select Folder", icon_path: str = "") -> str:

    """
    Opens folder selector and returns selected folder path
    - Allows custom title and icon
    """

    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    root = Tk()
    root.withdraw()
    if icon_path: root.iconbitmap(icon_path)
    folder_path = askdirectory(title=title)
    return folder_path.replace("/", "\\")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_path(location: str) -> str:
    
    """
    Returns path from registry
    - Supports: Desktop / Documents / Favorites / Pictures / Videos / Music
    """
    
    if os.name == 'nt':

        try:

            import winreg
            
            valid_locations = ("AppData", "Desktop", "Documents", "Personal", "Favorites", "Local AppData", "Pictures", "My Pictures", "Videos", "My Video", "Music", "My Music")
            
            if location in valid_locations:
                
                if location == "Documents": location = "Personal"
                elif location == "Pictures": location = "My Pictures"
                elif location == "Videos": location = "My Video"
                elif location == "Music": location = "My Music"

                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders", access=winreg.KEY_READ)
                path = os.path.expandvars(winreg.QueryValueEx(key, location)[0])
                return path
            
            else: raise ValueError(f"Invalid location: {location} | Valid locations: {', '.join(valid_locations)}")

        except: sys.exit(clr(err(sys.exc_info()),2))

    else: raise RuntimeError("This function is only available on windows!")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cls() -> None: 
    
    """
    Clear screen for multi-os
    """
    
    print(reset)
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def title(title: str) -> None:
    
    """
    Changes console window title
    """

    if os.name == 'nt': os.system(f"title {title}")
    else:
        import subprocess
        subprocess.call(["xdotool", "getactivewindow", "set_window", "--name", title])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def rm_line() -> None:
    
    """
    Deletes previous line
    """
    
    from shutil import get_terminal_size

    print("\033[A" + " " * (get_terminal_size().columns - 6) + "\033[A")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sys_open(item: str) -> None:
    
    """
    Can do the following:
    - Open the url on the default browser on windows / linux
    - Open directory
    - Start file
    """
    
    if os.name == 'nt': os.system(f'start {item}')
    else: os.system(f'xdg-open {item}')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

