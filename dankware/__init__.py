# Please read the documentation on github before using this module > https://github.com/SirDank/dankware

import os
import sys
import time
import random
from json import dumps
from requests import get
from datetime import datetime
from colorama import Fore, Style
from alive_progress import alive_bar
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def multithread(function, threads: int = 1, input_one = None, input_two = None, progress_bar: bool = True) -> None:
    
    """
    input one/two can be any of these: None, List, Variable
    """

    futures = []
    executor = ThreadPoolExecutor(max_workers=threads)
    one_isList = type(input_one) is list
    two_isList = type(input_two) is list
    if input_one is None: one_isNone = True
    else: one_isNone = False
    if input_two is None: two_isNone = True
    else: two_isNone = False

    if one_isNone:
        for _ in range(threads): futures.append(executor.submit(function))
    
    elif two_isNone:
        if one_isList:
            for item in input_one: futures.append(executor.submit(function, item))
        else:
            for _ in range(threads): futures.append(executor.submit(function, input_one))

    elif not one_isNone and not two_isNone:
        if one_isList and two_isList:
            if len(input_one) != len(input_two): print(clr(f"\n  > MULTITHREAD ERROR! - input_one({len(input_one)}) and input_two({len(input_two)}) do not have the same length!",2)); return
            for index in range(len(input_one)): futures.append(executor.submit(function, input_one[index], input_two[index]))
        elif one_isList:
            for index in range(len(input_one)): futures.append(executor.submit(function, input_one[index], input_two)) 
        elif two_isList:
            for index in range(len(input_two)): futures.append(executor.submit(function, input_one, input_two[index]))
        elif not one_isList and not two_isList:
            for _ in range(threads): futures.append(executor.submit(function, input_one, input_two))

    if progress_bar:
        with alive_bar(int(len(futures)), title='') as bar:
            for future in as_completed(futures):
                try: future.result(); bar()
                except: bar()
    else:
        for future in as_completed(futures):
            try: future.result()
            except: pass

def github_downloads(url: str) -> list:

    """
    
    this function extracts download urls from latest release on github and returns as list
    
    Example Input: https://api.github.com/repos/EXAMPLE/EXAMPLE/releases/latest
    
    Example Output: ['https://github.com/EXAMPLE/EXAMPLE/releases/download/VERSION/EXAMPLE.TXT']
    
    """

    if "https://api.github.com/repos/" not in url or "/releases/latest" not in url: print(clr('  > Invalid url! Must follow: "https://api.github.com/repos/NAME/NAME/releases/latest"',2)); time.sleep(5); sys.exit(1)    
    while True:
        try: response = str(dumps(get(url).json(), indent=4)).splitlines(); urls = []; break
        except: wait = input(clr("  > Make sure you are connected to the Internet! Press [ENTER] to try again... ",2))
    for line in response:
        if "browser_download_url" in line: urls.append(line.replace('"','').split(' ')[-1])
    return urls

def github_file_selector(url: str, mode: str, name_list: list) -> list:
    
    """
    
    This function is used to filter the output from github_downloads()
    
    url = 'USER_NAME/REPO_NAME'
    mode = 'add' or 'remove'
    name_list = list of names to be added or removed
    
    Example output from github_downloads(): [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
        ]
        
    ==================================================================================
    
    Example Input: "EX_USER/EX_REPO", "add", ["EXAMPLE"]
        
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
        ]
        
    Note: Only urls with filenames containing "EXAMPLE" were returned.

    ==================================================================================

    Example Input: "EX_USER/EX_REPO", "remove", ["EXAMPLE"]
    
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
        ]
    
    Note: Only urls with filenames not containing "EXAMPLE" were returned.
    
    """

    urls = []
    for file_url in github_downloads(f"https://api.github.com/repos/{url}/releases/latest"):
        if mode == "add": valid = False
        elif mode == "remove": valid = True
        for name in name_list:
            if name in file_url.split('/')[-1]:
                if mode == "add": valid = True
                elif mode == "remove": valid = False
        if valid: urls.append(file_url)
    return urls

def random_ip() -> str:
    
    """
    generates a random valid computer ip
    [NOTE] https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf
    """
    
    while True:

        ip = f"{random.randint(1,223)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

        for _ in ["6.","7.","10.","11.","21.","22.","26.","28.","29.","30.","33.","55.","100.64.","127.","129.123.","132.206.9.","132.206.123.","132.206.125.","144.39.","153.11.","165.160.","169.254.","192.88.99.","192.168.","198.18.","198.51.100.","204.113.91.","205.","214.","215."]:
            if ip.startswith(_): continue

        if ip.startswith("172."):
            temp_num = 16;
            while temp_num < 32:
                if ip.startswith(f"172.{temp_num}."): break
                temp_num += 1
            if not temp_num == 32: continue
        elif ip.startswith("192."):
            if ip.endswith(".170"): continue
            elif ip.endswith(".171"): continue
            elif ip.split('.')[2] == "2": continue
        elif ip.startswith("203.") and ip.split('.')[2] == "113": continue
        elif ip.endswith(".255.255.255"): continue

        break
        
    return ip

def clr(text: str, mode: int = 1, colour: str = magenta) -> str:
    
    """
    
    this function colours special characters inside the 'chars' list
    
    mode: 1 | to display general text (default)
    spl = magenta (default) / specified colour
    text = white
    
    mode: 2 | to display error messages
    spl = white
    text = red
    
    mode: 3
    spl = white
    text = random
    
    """
    
    chars = ['>','<','.',',','=','-','_','?','!','|','(',')','{','}','/','\\',':','"',"'"]
    words_green = ['true', 'True', 'TRUE', 'online', 'Online', 'ONLINE', 'successfully', 'Successfully', 'SUCCESSFULLY', 'successful', 'Successful', 'SUCCESSFUL', 'success', 'Success', 'SUCCESS']
    words_red = ['falsely', 'Falsely', 'FALSELY', 'false', 'False', 'FALSE', 'offline', 'Offline', 'OFFLINE', 'failures', 'Failures', 'FAILURES', 'failure', 'Failure', 'FAILURE', 'failed', 'Failed', 'FAILED', 'fail', 'Fail', 'FAIL']
    colours_bright = [black, blue, cyan, green, magenta, red, white, yellow]
    colours_alt = ["BBLACKK", "BBLUEE", "CCYANN", "GGREENN", "MMAGENTAA", "RREDD", "WWHITEE", "YYELLOWW"]

    for _ in range(len(colours_bright)):
        text = str(text).replace(colours_bright[_], colours_alt[_])
        
    # default

    if mode == 1:
        text = str(text).replace("[",f"{colour}[{white}").replace("]",f"{colour}]{white}")
        for char in chars: text = text.replace(char, f"{colour}{char}{white}")
        for word in words_green:
            #if word in ['success', 'Success', 'SUCCESS'] and "successful" in text.lower(): continue
            text = text.replace(word, f"{green}{word}{white}")
        for word in words_red:
            #if word in ['false', 'False', 'FALSE'] and "falsely" in text.lower(): continue
            text = text.replace(word, f"{red}{word}{white}")
    
    # for error messages
    
    elif mode == 2:
        text = str(text).replace("[",f"{white}[{red}").replace("]",f"{white}]{red}")
        for char in chars: text = text.replace(char, f"{white}{char}{red}")
        for word in words_green: text = text.replace(word, f"{green}{word}{red}")
    
    # random | TRUE, FALSE will not be coloured!
    
    elif mode == 3:
        text = [char for char in text]; bad_colours = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
        codes = vars(Fore); colours = [codes[colour] for colour in codes if colour not in bad_colours]
        for _ in range(len(text)):
            char = text[_]
            if char != ' ':
                if char in ( ['[',']'] + chars ): text[_] = white + char
                else: text[_] = random.choice(colours) + Style.BRIGHT + char

    else: return str(f"\n  {white}> {red}CLR ERROR{white}! - {red}Wrong mode {white}[{red}{mode}{white}]" + Style.RESET_ALL)
    
    for _ in range(len(colours_bright)):
        text = str(text).replace(colours_alt[_], colours_bright[_])

    if mode == 1: return str(f"{white}{text}" + Style.RESET_ALL)
    elif mode == 2: return str(f"{red}{text}" + Style.RESET_ALL)
    elif mode == 3: return str(''.join(text) + Style.RESET_ALL)

def align(text: str) -> str: 
    
    """
    center align banner / line ( supports both coloured and non-coloured )
    [NOTE] align supports: clr, clr_banner (colorama), does not support: fade
    """
    
    width = os.get_terminal_size().columns; aligned = text
    for colour in vars(Fore).values(): aligned = aligned.replace(colour,'')
    for style in vars(Style).values(): aligned = aligned.replace(style,'')
    text = text.split('\n'); aligned = aligned.split('\n')
    for _ in range(len(aligned)): aligned[_] = aligned[_].center(width).replace(aligned[_],text[_])
    return str('\n'.join(aligned) + Style.RESET_ALL)

def clr_banner(banner: str) -> str:
    
    """
    randomized banner colour
    """

    bad_colours = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
    codes = vars(Fore); colours = [codes[colour] for colour in codes if colour not in bad_colours]
    coloured_chars = [random.choice(colours) + Style.BRIGHT + char if char != ' ' else char for char in banner]
    return str(''.join(coloured_chars) + Style.RESET_ALL)

def fade(text: str, colour: str = "purple") -> str:
    
    """
    credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3
    available_colours = [black,red,green,cyan,blue,purple,random,black-v,red-v,green-v,cyan-v,blue-v,purple-v,pink-v]
    """

    colour = colour.lower(); available_colours = ['black','red','green','cyan','blue','purple','random','black-v','red-v','green-v','cyan-v','blue-v','purple-v','pink-v'] 
    if colour in available_colours: valid_colour = True
    else: valid_colour = False
    if not valid_colour: return clr(f"\n  > FADE ERROR! - Invalid colour: {colour} | Available colours: {', '.join(available_colours)}")
        
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
    
    else: return clr(f"\n  > FADE ERROR! - [{colour}] is not supported yet!",2)
    
    if multi_line: faded = faded[:-1]
    return faded

def get_duration(then, now = datetime.now(), interval = "default"):

    """
    Returns a duration as specified by variable interval
    Functions, except totalDuration, returns [quotient, remainder]
    """

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds() 
    
    def years():
        return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
        return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
        return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
        return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
        if seconds != None:
            return divmod(seconds, 1)   
        return duration_in_s
  
    def dynamic():

        dynamic_duration = int(years()[0])
        if dynamic_duration == 0:
            dynamic_duration = int(days()[0])
            if dynamic_duration == 0:
                dynamic_duration = int(hours()[0])
                if dynamic_duration == 0:
                    dynamic_duration = int(minutes()[0])
                    if dynamic_duration == 0:
                        dynamic_duration = int(seconds()[0])
                        if dynamic_duration == 1: return f"{dynamic_duration} second"
                        else: return f"{dynamic_duration} seconds"
                    elif dynamic_duration == 1: return f"{dynamic_duration} minute"
                    else: return f"{dynamic_duration} minutes"
                elif dynamic_duration == 1: return f"{dynamic_duration} hour"
                else: return f"{dynamic_duration} hours"
            elif dynamic_duration == 1: return f"{dynamic_duration} day"
            else: return f"{dynamic_duration} days"
        elif dynamic_duration == 1: return f"{dynamic_duration} year"
        else: return f"{dynamic_duration} years"

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'dynamic': dynamic(),
        'default': totalDuration()
    }[interval]

# functions for windows executables [ dankware ]

def cls() -> None: 
    
    """
    clear screen for multi-os
    """
    
    print(Style.RESET_ALL)
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

def title(title: str) -> None:
    
    """
    changes title
    """

    if os.name == 'nt': os.system(f"title {title}")
    
def rm_line() -> None:
    
    """
    deletes previous line
    """

    print("\033[A                             \033[A")

def chdir(mode: str) -> str:
    
    """

    running "os.chdir(os.path.dirname(__file__))" inside example.py will change its directory to the example.py file's location
    running "os.chdir(os.path.dirname(sys.argv[0]))" inside example.exe will change its directory to the example.exe file's location (nuitka)
        
    for changing directory to exe's path as exe: exec(chdir("exe"))
    for changing directory to script's path as script: exec(chdir("script"))
    
    [NOTE] When I build executables, the [ exec_mode = "script" ] is automatically replaced with [ exec_mode = "exe" ] inside the script
    [NOTE] If you run "os.chdir(os.path.dirname(__file__))" as an executable, it will change its directory to its temp folder [ C:\\Users\\user\\AppData\\Local\\Temp\\dankware_PPID ]

    """

    if mode == "script": return "os.chdir(os.path.dirname(__file__))" # as .py
    elif mode == "exe": return "os.chdir(os.path.dirname(sys.argv[0]))" # as .exe

def sys_open(item: str) -> None:
    
    """
    - opens the url on the default browser on windows / linux
    - opens directory
    - starts file
    """
    
    if os.name == 'nt': os.system(f'start {item}')
    else: os.system(f'xdg-open {item}')

def dankware_banner() -> None:
    
    """
    dankware banner printer with github url
    """

    banner="\n 8 888888888o.     \n 8 8888    `^888.  \n 8 8888        `88.\n 8 8888         `88\n 8 8888          88\n 8 8888          88\n 8 8888         ,88\n 8 8888        ,88'\n 8 8888    ,o88P'  \n 8 888888888P'     \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n b.             8\n 888o.          8\n Y88888o.       8\n .`Y888888o.    8\n 8o. `Y888888o. 8\n 8`Y8o. `Y88888o8\n 8   `Y8o. `Y8888\n 8      `Y8o. `Y8\n 8         `Y8o.`\n 8            `Yo\n\n\n 8 8888     ,88'\n 8 8888    ,88' \n 8 8888   ,88'  \n 8 8888  ,88'   \n 8 8888 ,88'    \n 8 8888 88'     \n 8 888888<      \n 8 8888 `Y8.    \n 8 8888   `Y8.  \n 8 8888     `Y8.\n\n\n `8.`888b                 ,8'\n  `8.`888b               ,8' \n   `8.`888b             ,8'  \n    `8.`888b     .b    ,8'   \n     `8.`888b    88b  ,8'    \n      `8.`888b .`888b,8'     \n       `8.`888b8.`8888'      \n        `8.`888`8.`88'       \n         `8.`8' `8,`'        \n          `8.`   `8'         \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n 8 888888888o.  \n 8 8888    `88. \n 8 8888     `88 \n 8 8888     ,88 \n 8 8888.   ,88' \n 8 888888888P'  \n 8 8888`8b      \n 8 8888 `8b.    \n 8 8888   `8b.  \n 8 8888     `88.\n\n\n 8 8888888888   \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n 8 8888         \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n "
    cls(); print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in align(clr_banner(banner)).splitlines(): time.sleep(0.05); print(line)

    num_lines = os.get_terminal_size().lines
    for _ in range(num_lines): time.sleep(0.1); print("\n")
    print(align(clr("github.com / SirDank"))); sleep_time = 0.01
    for _ in range(int(num_lines/4)): time.sleep(sleep_time); sleep_time += 0.025; print("\n")
    time.sleep(4)
    for _ in range(int(num_lines/2)+5): time.sleep(0.01); print("\n")
    cls()
