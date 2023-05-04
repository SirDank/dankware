###################################################################################

#                            https://github.com/SirDank                            

###################################################################################

# > Please read the documentation on github before using this module!

import os
import sys
import time
import random
from datetime import datetime
from colorama import Fore, Style

# colorama colours

black = Fore.BLACK + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
reset = Style.RESET_ALL
white = Fore.WHITE + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def multithread(function: callable, threads: int = 1, *args, progress_bar: bool = True) -> None:
    
    """
    > Please read the documentation on github before using this function!
    
    ________________________________________________________________________________

    Run the given function in multiple threads with the specified inputs.

    - function: The function to run in multiple threads.
    - threads: The number of threads to use.
    - *args: Input(s) for the function. Can be a list, a single value.
    - progress_bar: Whether to display a progress bar.
    """
    
    from rich.live import Live
    from rich.panel import Panel
    from rich.table import Table
    from shutil import get_terminal_size
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn, TimeElapsedColumn

    try:
        
        def submit_task(executor, *args):
            return executor.submit(function, *args)
        
        if threads < 1:
            raise ValueError("The number of threads must be a positive integer.")

        futures = []
        executor = ThreadPoolExecutor(max_workers=threads)

        if not args:
            for _ in range(threads): futures.append(executor.submit(function))
        else:
            input_lists = []
            for arg in args:
                if isinstance(arg, list):
                    input_lists.append(arg)
                else:
                    input_lists.append([arg] * threads)

            for task_args in zip(*input_lists):
                futures.append(submit_task(executor, *task_args))

        if progress_bar:
            width = get_terminal_size().columns
            job_progress = Progress("{task.description}", SpinnerColumn(), BarColumn(bar_width=width), TextColumn("[deep_pink1][progress.percentage][bright_cyan]{task.percentage:>3.0f}%"), "[bright_cyan]ETA", TimeRemainingColumn(), TimeElapsedColumn())
            overall_task = job_progress.add_task("[bright_green]Progress", total=int(len(futures)))
            progress_table = Table.grid()
            progress_table.add_row(Panel.fit(job_progress, title="[bright_red]Jobs", border_style="magenta1", padding=(1, 2)))

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

def github_downloads(user_repo: str) -> list:

    """
    Extracts direct download urls from the latest release on github and returns it as a list

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
    
    urls = []

    #if "https://api.github.com/repos/" not in url or "/releases/latest" not in url:
    #    raise ValueError(clr('  > Invalid url! Must follow: "https://api.github.com/repos/NAME/NAME/releases/latest"',2)) 
    while True:
        try: response = requests.get(f"https://api.github.com/repos/{user_repo}/releases/latest").json(); break
        except: input(clr("  > Make sure you are connected to the Internet! Press [ENTER] to try again... ",2))
    
    for data in response["assets"]:
        urls.append(data["browser_download_url"])

    return urls

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def github_file_selector(user_repo: str, filter_mode: str, name_list: list) -> list:
    
    """
    
    This function is used to filter the output from github_downloads()
    
    - user_repo = 'USER_NAME/REPO_NAME' ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    - filter_mode = 'add' or 'remove'
    - name_list = list of names to be added or removed
    
    _______________________________________________________________________________________________________________________________________________________________________
    
    [ EXAMPLE ]
    ```python
    from dankware import github_file_selector
    for file_url in github_file_selector("EssentialsX/Essentials", "remove", ['AntiBuild', 'Discord', 'GeoIP', 'Protect', 'XMPP']):
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
    
    Example Input: "EX_USER/EX_REPO", "add", ["EXAMPLE"]
        
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
    ]
        
    - Note: Only urls with filenames containing "EXAMPLE" were returned.

    _______________________________________________________________________________________________________________________________________________________________________

    Example Input: "EX_USER/EX_REPO", "remove", ["EXAMPLE"]
    
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
    ]
    
    - Note: Only urls with filenames not containing "EXAMPLE" were returned.
    
    """

    urls = []
    for file_url in github_downloads(user_repo):
        if filter_mode == "add": valid = False
        elif filter_mode == "remove": valid = True
        for name in name_list:
            if name in file_url.split('/')[-1]:
                if filter_mode == "add": valid = True
                elif filter_mode == "remove": valid = False
        if valid: urls.append(file_url)
    return urls

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_ip() -> str:
    
    """
    Generates a random valid computer ip
    - Follows: https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf
    """

    excluded_prefixes_one = {'6':'','7':'','10':'','11':'','21':'','22':'','26':'','28':'','29':'','30':'','33':'','55':'','127':'','136':'','205':'','214':'','215':''}
    excluded_prefixes_two = {'23.27':'','31.25':'','50.117':'','74.115':'','75.127':'','81.87':'','100.64':'','128.16':'','128.40':'','128.41':'','128.86':'','128.232':'','128.240':'','128.243':'','129.11':'','129.12':'','129.31':'','129.67':'','129.123':'','129.169':'','129.215':'','129.234':'','130.88':'','130.159':'','130.209':'','130.246':'','131.111':'','131.227':'','131.231':'','131.251':'','134.36':'','134.83':'','134.151':'','134.219':'','134.220':'','134.225':'','136.148':'','136.156':'','137.44':'','137.50':'','137.73':'','137.108':'','137.195':'','137.222':'','137.253':'','138.38':'','138.40':'','138.250':'','138.253':'','139.133':'','139.153':'','139.166':'','139.184':'','139.222':'','140.97':'','141.163':'','141.241':'','142.111':'','142.252':'','143.52':'','143.117':'','143.167':'','143.210':'','143.234':'','144.32':'','144.39':'','144.82':'','144.124':'','144.173':'','146.87':'','146.97':'','146.169':'','146.176':'','146.179':'','146.191':'','146.227':'','147.143':'','147.188':'','147.197':'','148.79':'','148.88':'','148.197':'','149.155':'','149.170':'','150.204':'','152.71':'','152.78':'','152.105':'','153.11':'','155.198':'','155.245':'','157.140':'','157.228':'','158.94':'','158.125':'','158.143':'','158.223':'','159.92':'','160.5':'','160.9':'','161.73':'','161.74':'','161.76':'','161.112':'','163.1':'','163.119':'','163.160':'','163.167':'','164.11':'','165.160':'','166.88':'','169.254':'','172.252':'','192.168':'','192.177':'','192.186':'','193.60':'','194.66':'','194.80':'','195.194':'','198.18':'','205.164':'','212.121':'','212.219':''}
    excluded_prefixes_three = {'4.53.201':'','5.152.179':'','8.12.162':'','8.12.163':'','8.12.164':'','8.14.84':'','8.14.145':'','8.14.146':'','8.14.147':'','8.17.250':'','8.17.251':'','8.17.252':'','23.231.128':'','31.25.2':'','31.25.4':'','37.72.112':'','37.72.172':'','38.72.200':'','46.254.200':'','50.93.192':'','50.93.193':'','50.93.194':'','50.93.195':'','50.93.196':'','50.93.197':'','50.115.128':'','50.118.128':'','63.141.222':'','64.62.253':'','64.92.96':'','64.145.79':'','64.145.82':'','64.158.146':'','65.49.24':'','65.49.93':'','65.162.192':'','66.79.160':'','66.160.191':'','68.68.96':'','69.46.64':'','69.176.80':'','72.13.80':'','72.52.76':'','74.82.43':'','74.82.160':'','74.114.88':'','74.115.2':'','74.115.4':'','74.122.100':'','85.12.64':'','89.207.208':'','92.245.224':'','103.251.91':'','108.171.32':'','108.171.42':'','108.171.52':'','108.171.62':'','118.193.78':'','130.93.16':'','132.206.9':'','132.206.123':'','132.206.125':'','141.170.64':'','141.170.96':'','141.170.100':'','146.82.55.93':'','149.54.136':'','149.54.152':'','159.86.128':'','173.245.64':'','173.245.194':'','173.245.220':'','173.252.192':'','178.18.16':'','178.18.26':'','178.18.27':'','178.18.28':'','178.18.29':'','183.182.22':'','185.83.168':'','192.12.72':'','192.18.195':'','192.35.172':'','192.41.104':'','192.41.112':'','192.41.128':'','192.68.153':'','192.76.6':'','192.76.8':'','192.76.16':'','192.76.32':'','192.82.153':'','192.84.5':'','192.84.75':'','192.84.76':'','192.84.80':'','192.84.212':'','192.88.9':'','192.88.10':'','192.88.99':'','192.92.114':'','192.94.235':'','192.100.78':'','192.100.154':'','192.107.168':'','192.108.120':'','192.124.46':'','192.133.244':'','192.149.111':'','192.150.180':'','192.150.184':'','192.153.213':'','192.155.160':'','192.156.162':'','192.160.194':'','192.171.128':'','192.171.192':'','192.173.1':'','192.173.2':'','192.173.4':'','192.173.128':'','192.188.157':'','192.188.158':'','192.190.201':'','192.190.202':'','192.195.42':'','192.195.105':'','192.195.116':'','192.195.118':'','192.249.64':'','192.250.240':'','193.32.22':'','193.37.225':'','193.37.240':'','193.38.143':'','193.39.80':'','193.39.172':'','193.39.212':'','193.107.116':'','193.130.15':'','193.133.28':'','193.138.86':'','194.32.32':'','194.35.93':'','194.35.186':'','194.35.192':'','194.35.241':'','194.36.1':'','194.36.2':'','194.36.121':'','194.36.152':'','194.60.218':'','194.110.214':'','194.187.32':'','198.12.120':'','198.12.121':'','198.12.122':'','198.51.100':'','198.144.240':'','199.33.120':'','199.33.124':'','199.48.147':'','199.68.196':'','199.127.240':'','199.187.168':'','199.188.238':'','199.255.208':'','203.12.6':'','204.13.64':'','204.16.192':'','204.19.238':'','204.74.208':'','204.113.91':'','205.159.189':'','205.209.128':'','206.108.52':'','206.165.4':'','208.77.40':'','208.80.4':'','208.123.223':'','209.51.185':'','209.54.48':'','209.107.192':'','209.107.210':'','209.107.212':'','211.156.110':'','212.121.192':'','216.151.183':'','216.151.190':'','216.172.128':'','216.185.36':'','216.218.233':'','216.224.112':''}
    
    while True:
        
        first_octet = random.randint(1, 223)
        if f"{first_octet}" in excluded_prefixes_one.keys(): continue
        
        second_octet = random.randint(0, 255)
        if f"{first_octet}.{second_octet}" in excluded_prefixes_two.keys(): continue
        
        third_octet = random.randint(0, 255)
        if f"{first_octet}.{second_octet}.{third_octet}" in excluded_prefixes_three.keys(): continue
        
        fourth_octet = random.randint(0, 255)
        
        if first_octet == 172 and second_octet >= 16 and second_octet <= 31: continue
        elif first_octet == 192:
            if fourth_octet == 170 or fourth_octet == 171 or third_octet == 2: continue
        elif first_octet == 203 and third_octet == 113: continue
        elif first_octet == 216 and second_octet == 83 and third_octet >= 33 and third_octet <= 63: continue
        elif second_octet == 255 and third_octet == 255 and third_octet == 255: continue

        break
    
    ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
        
    return ip

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def is_admin() -> bool:
    
    import ctypes
    
    """
    Checks if the current user has admin privileges and returns True if found else False
    """
    
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False
    
'''
def run_as_admin() -> None:
    
    """
    Executes the script with admin privileges
    """
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #sys.exit(clr("\n  > Exiting original un-elevated script...",2))
'''

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def export_registry_keys(registry_root: str, registry_path: str, recursive: bool = True, export_path: str = "export.reg") -> None:

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
            raise ValueError(f"Invalid Registry Root! Use one of the following: {', '.join(key_map.keys())}")
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
        print(clr(f"\n  > Successfully exported registry keys to \"{os.path.join(os.getcwd(), 'export.reg') if export_path == 'export.reg' else export_path}\""))
    
    except: sys.exit(clr(err(sys.exc_info()),2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clr(text: str, mode: int = 1, colour_one: str = white, colour_two: str = magenta) -> str:
    
    """
    
    this function colours special characters inside the 'chars' list
    
    ___________________________________________
    
    - mode: 1 | to display general text (default)
    - text = white (default) / specified colour
    - spl = magenta (default) / specified colour

    ___________________________________________

    - mode: 2 | to display error messages
    - text = red (fixed colour)
    - spl = white (fixed colour)

    ___________________________________________

    - mode: 3
    - text = random (fixed colour)
    - spl = white (fixed colour)

    ___________________________________________

    - mode: 4 | to display banners
    - text & spl = random (fixed colour)
    
    """
    
    chars = ['[',']','>','<','.',',','=','-','_','?','!','|','(',')','{','}','/','\\',':','"',"'","%"]
    
    words_green = ['true', 'True', 'TRUE', 'online', 'Online', 'ONLINE', 'successfully', 'Successfully', 'SUCCESSFULLY', 'successful', 'Successful', 'SUCCESSFUL', 'success', 'Success', 'SUCCESS']
    words_red = ['falsely', 'Falsely', 'FALSELY', 'false', 'False', 'FALSE', 'offline', 'Offline', 'OFFLINE', 'failures', 'Failures', 'FAILURES', 'failure', 'Failure', 'FAILURE', 'failed', 'Failed', 'FAILED', 'fail', 'Fail', 'FAIL']
    
    colours_to_replace = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW, Style.BRIGHT, Style.RESET_ALL]
    colours_alt = ["BBLACKK", "BBLUEE", "CCYANN", "GGREENN", "MMAGENTAA", "RREDD", "WWHITEE", "YYELLOWW", "BBRIGHTT", "RRESETT"]
    
    bad_colours = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
    codes = vars(Fore); colours = [codes[colour] for colour in codes if colour not in bad_colours]
    styles = [Style.BRIGHT, Style.DIM, Style.NORMAL]
    
    try:
        if mode not in [3, 4]:
            for _ in range(len(colours_to_replace)):
                text = text.replace(colours_to_replace[_], colours_alt[_])
        else:
            for _ in range(len(colours_to_replace)):
                text = text.replace(colours_to_replace[_], '')

        # default

        if mode == 1:
            #text = text.replace("[",f"{colour_two}[{colour_one}").replace("]",f"{colour_two}]{colour_one}")
            for char in chars: text = text.replace(char, f"{colour_two}{char}{colour_one}")
            for word in words_green:
                replacement = green.join(list(word))
                text = text.replace(word, f"{green}{replacement}{colour_one}")
            for word in words_red:
                replacement = red.join(list(word))
                text = text.replace(word, f"{red}{replacement}{colour_one}")
        
        # for error messages
        
        elif mode == 2:
            #text = text.replace("[",f"{white}[{red}").replace("]",f"{white}]{red}")
            for char in chars: text = text.replace(char, f"{white}{char}{red}")
            for word in words_green:
                replacement = green.join(list(word))
                text = text.replace(word, f"{green}{replacement}{red}")
        
        # random | TRUE, FALSE will not be coloured!
        
        elif mode in [3, 4]:

            text = [char for char in text]
            
            if mode == 3: colour_spl = True
            else: colour_spl = False
    
            for _ in range(len(text)):
                char = text[_]
                if char != ' ' and char != '\n':
                    if colour_spl:
                        if char in chars:
                            text[_] = white + char
                        else:
                            text[_] = random.choice(colours) + Style.BRIGHT + char
                    else:
                        text[_] = random.choice(colours) + Style.BRIGHT + char

            text = ''.join(text)

        else: raise ValueError(f"\n  {white}> {red}Invalid Mode {white}[{red}{mode}{white}] | Valid Modes{white}: {red}1{white},{red}2{white},{red}3{white},{red}4" + reset)

        if mode not in [3, 4]:
            for _ in range(len(colours_to_replace)):
                text = text.replace(colours_alt[_], colours_to_replace[_])

        if mode == 1: return white + text + reset
        elif mode == 2: return red + text + reset
        elif mode == 3 or mode == 4: return text + reset
    
    except: sys.exit(clr(err(sys.exc_info()),2))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def align(text: str) -> str: 
    
    """
    center align banner / line ( supports both coloured and non-coloured )
    - [NOTE] align supports: clr, does not support: fade
    """
    
    from shutil import get_terminal_size

    width = get_terminal_size().columns; aligned = text
    for colour in vars(Fore).values(): aligned = aligned.replace(colour,'')
    for style in vars(Style).values(): aligned = aligned.replace(style,'')
    text = text.split('\n'); aligned = aligned.split('\n')
    for _ in range(len(aligned)): aligned[_] = aligned[_].center(width).replace(aligned[_],text[_])
    return str('\n'.join(aligned) + reset)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fade(text: str, colour: str = "purple") -> str:
    
    """
    credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3
    - available_colours = black, red, green, cyan, blue, purple, random, black-v, red-v, green-v, cyan-v, blue-v, purple-v, pink-v
    """
    
    available_colours = ['black','red','green','cyan','blue','purple','random','black-v','red-v','green-v','cyan-v','blue-v','purple-v','pink-v']

    try:
        colour = colour.lower()
        if not colour in available_colours: raise ValueError(clr(f"\n  > Invalid Colour: {colour} | Available Colours: {', '.join(available_colours)}",2))
            
        faded = ""
        if len(text.splitlines()) > 1: multi_line = True
        else: multi_line = False

        if colour == "black":
            for line in text.splitlines():
                R = 0; G = 0; B = 0
                for char in line:
                    R += 3; G += 3; B += 3
                    if R > 255 and G > 255 and B > 255: R = 255; G = 255; B = 255
                    faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
                if multi_line: faded += "\n"
                
        elif colour == "red":
            for line in text.splitlines():
                G = 250
                for char in line:
                    G -= 5
                    if G < 0: G = 0
                    faded += f"\033[38;2;255;{G};0m{char}\033[0m"
                if multi_line: faded += "\n"
                
        elif colour == "green":
            for line in text.splitlines():
                R = 0
                for char in line:
                    if not R > 200: R += 3
                    faded += f"\033[38;2;{R};255;0m{char}\033[0m"
                if multi_line: faded += "\n"
                
        elif colour == "cyan":
            for line in text.splitlines():
                B = 100
                for char in line:
                    B += 2
                    if B > 255: B = 255
                    faded += f"\033[38;2;0;255;{B}m{char}\033[0m"
                if multi_line: faded += "\n"

        elif colour == "blue":
            for line in text.splitlines():
                G = 0
                for char in line:
                    G += 3
                    if G > 255: G = 255
                    faded += f"\033[38;2;0;{G};255m{char}\033[0m"
                if multi_line: faded += "\n"
            
        elif colour == "purple":
            for line in text.splitlines():
                R = 35
                for char in line:
                    R += 3
                    if R > 255: R = 255
                    faded += f"\033[38;2;{R};0;220m{char}\033[0m"
                if multi_line: faded += "\n"

        elif colour == "black-v":
            R = 0; G = 0; B = 0
            for line in text.splitlines():
                faded += (f"\033[38;2;{R};{G};{B}m{line}\033[0m")
                if not R == 255 and not G == 255 and not B == 255:
                    R += 20; G += 20; B += 20
                    if R > 255 and G > 255 and B > 255: R = 255; G = 255; B = 255
                if multi_line: faded += "\n"
                        
        elif colour == "red-v":
            G = 250
            for line in text.splitlines():
                faded += f"\033[38;2;255;{G};0m{line}\033[0m"
                if not G == 0:
                    G -= 25
                    if G < 0: G = 0
                if multi_line:faded += "\n"

        elif colour == "green-v":
            R = 0
            for line in text.splitlines():
                faded += f"\033[38;2;{R};255;0m{line}\033[0m"
                if not R > 200: R += 30
                if multi_line: faded += "\n"
            
        elif colour == "cyan-v":
            B = 100
            for line in text.splitlines():
                faded += f"\033[38;2;0;255;{B}m{line}\033[0m"
                if not B == 255:
                    B += 15
                    if B > 255: B = 255
                if multi_line: faded += "\n"
            
        elif colour == "blue-v":
            G = 10
            for line in text.splitlines():
                faded += f"\033[38;2;0;{G};255m{line}\033[0m"
                if not G == 255:
                    G += 15
                    if G > 255: G = 255
                if multi_line: faded += "\n"
            
        elif colour == "purple-v":
            R = 40
            for line in text.splitlines():
                faded += f"\033[38;2;{R};0;220m{line}\033[0m"
                if not R == 255:
                    R += 15
                    if R > 255: R = 255
                if multi_line: faded += "\n"
            
        elif colour == "pink-v":
            B = 255
            for line in text.splitlines():
                faded += f"\033[38;2;255;0;{B}m{line}\033[0m"
                if not B == 0:
                    B -= 20
                    if B < 0: B = 0
                if multi_line: faded += "\n"

        elif colour == "random":
            for line in text.splitlines():
                for char in line:
                    R, G, B = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                    faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
                if multi_line: faded += "\n"
        
        else: raise ValueError(clr(f"\n  > FADE ERROR! - [{colour}] is not supported yet!",2))
        
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
    - default -> str
    """
    
    if now is None: now = datetime.now()

    duration = now - then

    if interval in ("year", "years"): return int(duration.days / 365)
    elif interval in ("day", "days"): return duration.days
    elif interval in ("hour", "hours"): return int(duration.total_seconds() / 3600)
    elif interval in ("minute", "minutes"): return int(duration.total_seconds() / 60)
    elif interval in ("second", "seconds"): return int(duration.total_seconds())
    elif interval == "dynamic":

        seconds = duration.total_seconds()

        if seconds < 60:
            return f"{int(seconds)} second{'s' if seconds > 1 else ''}"
        
        elif seconds < 3600:
            minutes = int(seconds / 60)
            return f"{minutes} minute{'s' if minutes > 1 else ''}"
        
        elif seconds < 86400:
            hours = int(seconds / 3600)
            return f"{hours} hour{'s' if hours > 1 else ''}"
       
        elif seconds < 31536000:
            days = int(seconds / 86400)
            return f"{days} day{'s' if days > 1 else ''}"
        
        else:
            years = int(seconds / 31536000)
            return f"{years} year{'s' if years > 1 else ''}"
    
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

def err(exc_info) -> str:
    
    """
    Returns a short traceback
    
    __________________________________________

    [ EXAMPLE ]

    ```python
    import sys
    from dankware import err, clr
    try: value = 1/0
    except: print(clr(err(sys.exc_info()),2))
    ```
    """
    
    from traceback import extract_tb

    ex_type, ex_value, ex_traceback = exc_info
    trace_back = extract_tb(ex_traceback)
    stack_trace = []

    for trace in trace_back:
        filename = trace[0]
        if filename == "<string>": filename = str(__name__)
        #elif filename.endswith(".pyc"): filename = filename[:-1]
        #elif filename.endswith("$py.class"): filename = filename[:-9] + ".py"
        stack_trace.append("    - File: {} | Line: {} | Function: {}{}".format(filename, trace[1], trace[2] if trace[2] != '<module>' else 'top-level', ' | ' + trace[3] if trace[3] else ''))

    report = "  > Error Type: {}".format(ex_type.__name__)
    if ex_value: report += "\n  > Error Message: \n    - {}".format(ex_value)
    report += "\n  > Error Stack Trace: \n{}".format('\n'.join(stack_trace))

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
    from PIL import Image, ImageTk
    
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

            self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
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
    
    from ctypes import windll

    hWnd = windll.kernel32.GetConsoleWindow()
    windll.user32.ShowWindow(hWnd, 0)

def show_window() -> None:

    """
    Shows console window
    """
    
    from ctypes import windll

    hWnd = windll.kernel32.GetConsoleWindow()
    windll.user32.ShowWindow(hWnd, 1)
    
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

def file_selector(title: str = "Open", icon_path: str = "") -> str:
    
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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_path(name: str) -> str:
    
    """
    Returns path from registry
    - Supports: Desktop / Documents / Favorites / Pictures / Videos / Music
    """
    
    if name in ["Desktop", "Documents", "Favorites", "Pictures", "My Pictures", "Videos", "My Video", "Music", "My Music"]:
        
        if name == "Documents": name = "Personal"
        elif name == "Pictures": name = "My Pictures"
        elif name == "Videos": name = "My Video"
        elif name == "Music": name = "My Music"
        
        import winreg
        import os

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders", access=winreg.KEY_READ)
        path = os.path.expandvars(winreg.QueryValueEx(key, name)[0])
        return path
    
    else: raise ValueError("Invalid name")

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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def rm_line() -> None:
    
    """
    Deletes previous line
    """
    
    from shutil import get_terminal_size

    print("\033[A" + " " * (get_terminal_size().columns - 6) + "\033[A")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def chdir(mode: str) -> str:
    
    """
    - running "os.chdir(os.path.dirname(__file__))" inside example.py will change its directory to the example.py file's location
    - running "os.chdir(os.path.dirname(sys.argv[0]))" inside example.exe will change its directory to the example.exe file's location (nuitka)
    - for changing directory to exe's path as exe: exec(chdir("exe"))
    - for changing directory to script's path as script: exec(chdir("script"))
    - [NOTE] When I build executables, the [ exec_mode = "script" ] is automatically replaced with [ exec_mode = "exe" ] inside the script
    - [NOTE] If you run "os.chdir(os.path.dirname(__file__))" as an executable, it will change its directory to its temp folder [ C:\\Users\\user\\AppData\\Local\\Temp\\dankware_PPID ]
    """

    if mode == "script": return "os.chdir(os.path.dirname(__file__))" # as .py
    elif mode == "exe": return "os.chdir(os.path.dirname(sys.argv[0]))" # as .exe

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

def dankware_banner() -> None:
    
    """
    Dankware banner printer with github url
    """
    
    from shutil import get_terminal_size
    
    num_lines = get_terminal_size().lines
    banner="\n 8 888888888o.     \n 8 8888    `^888.  \n 8 8888        `88.\n 8 8888         `88\n 8 8888          88\n 8 8888          88\n 8 8888         ,88\n 8 8888        ,88'\n 8 8888    ,o88P'  \n 8 888888888P'     \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n b.             8\n 888o.          8\n Y88888o.       8\n .`Y888888o.    8\n 8o. `Y888888o. 8\n 8`Y8o. `Y88888o8\n 8   `Y8o. `Y8888\n 8      `Y8o. `Y8\n 8         `Y8o.`\n 8            `Yo\n\n\n 8 8888     ,88'\n 8 8888    ,88' \n 8 8888   ,88'  \n 8 8888  ,88'   \n 8 8888 ,88'    \n 8 8888 88'     \n 8 888888<      \n 8 8888 `Y8.    \n 8 8888   `Y8.  \n 8 8888     `Y8.\n\n\n `8.`888b                 ,8'\n  `8.`888b               ,8' \n   `8.`888b             ,8'  \n    `8.`888b     .b    ,8'   \n     `8.`888b    88b  ,8'    \n      `8.`888b .`888b,8'     \n       `8.`888b8.`8888'      \n        `8.`888`8.`88'       \n         `8.`8' `8,`'        \n          `8.`   `8'         \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n 8 888888888o.  \n 8 8888    `88. \n 8 8888     `88 \n 8 8888     ,88 \n 8 8888.   ,88' \n 8 888888888P'  \n 8 8888`8b      \n 8 8888 `8b.    \n 8 8888   `8b.  \n 8 8888     `88.\n\n\n 8 8888888888   \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n 8 8888         \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n "
    
    tmp = ""
    to_print = []
    sleep_time = []
    sleep_time_1 = 0.05
    sleep_time_2 = 0.01
    sleep_time_3 = 0.333
    sleep_time_variation = 0.01
    
    # sleep_time_1
        
    for line in align(clr(banner,4)).splitlines():
        to_print.append(line)
        sleep_time.append(sleep_time_1)
        
    for _ in range(num_lines):
        tmp += "     \n"
        to_print.append("     ")
        sleep_time.append(sleep_time_1)
        
    # sleep_time_2
    
    tmp += (align(clr("github.com / SirDank")) + '\n')
    to_print.append(align(clr("github.com / SirDank")))
    sleep_time.append(sleep_time_2)
    
    for _ in range(int(num_lines/2)):
        tmp += "     \n"
        to_print.append("     ")
        sleep_time.append(sleep_time_2)
        sleep_time_2 = float(f'{(sleep_time_2 + sleep_time_variation):.3f}')
        
    # sleep_time_3

    for _ in range(3):
        to_print.append(tmp.replace(align(clr("github.com / SirDank")), align(clr("< github.com / SirDank >"))))
        sleep_time.append(sleep_time_3)
        to_print.append(tmp.replace(align(clr("github.com / SirDank")), align(clr("<   github.com / SirDank   >"))))
        sleep_time.append(sleep_time_3)
        to_print.append(tmp.replace(align(clr("github.com / SirDank")), align(clr("<     github.com / SirDank     >"))))
        sleep_time.append(sleep_time_3)
    to_print.append(tmp)
    sleep_time.append(sleep_time_3)
    
    sleep_time[-1] = 4
    
    for _ in range(int(num_lines/2)):
        to_print.append("     ")
        sleep_time.append(0.01)
        #sleep_time.append(sleep_time_2)
        #sleep_time_2 = float(f'{(sleep_time_2 - sleep_time_variation):.3f}')
        
    # start
        
    cls(); print('\n' * 60)
    for _, amt in zip(to_print, sleep_time):
        print(_); time.sleep(amt)
    
    # finish
        
    cls()
