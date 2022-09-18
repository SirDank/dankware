# Please read the documentation on github before using this module > https://github.com/SirDank/dankware

import os
import sys
import time
import json
import random
import requests
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

def multithread(function, threads: int = 1, input_one = None, input_two = None, progress_bar: bool = True) -> None: # input one/two can be any of these: None, List, Variable 

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
            if len(input_one) != len(input_two): print(clr(f"\n  > MULTITHREAD ERROR! - input_one[{len(input_one)}] and input_two[{len(input_two)}] do not have the same length!",2)); return
            for index in range(len(input_one)): futures.append(executor.submit(function, input_one[index], input_two[index]))
        elif one_isList:
            for index in range(len(input_one)): futures.append(executor.submit(function, input_one[index], input_two)) 
        elif two_isList:
            for index in range(len(input_two)): futures.append(executor.submit(function, input_one, input_two[index]))
        elif not one_isList and not two_isList:
            for _ in range(threads): futures.append(executor.submit(function, input_one, input_two))

    if progress_bar:
        with alive_bar(int(len(futures))) as bar:
            for future in as_completed(futures):
                try: future.result(); bar()
                except: bar()
    else:
        for future in as_completed(futures):
            try: future.result()
            except: pass

def cls() -> None: # clear screen for multi-os
    
    print(Style.RESET_ALL)
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

def clr(text: str, mode: int = 1) -> str: # colour special chars: mode = 1 > spl = magenta & text = white | mode=2 > spl = white & text = red | mode=3 > spl = white & text = random
    
    chars = ['>','.',',','=','-','_','!','|','(',')','{','}','/',':','"',"'"]
    chars_2 = ['true', 'True', 'TRUE']
    chars_3 = ['false', 'False', 'FALSE']
    colours = [black, blue, cyan, green, magenta, red, white, yellow]
    colours_alt = ["BBLACKK", "BBLUEE", "CCYANN", "GGREENN", "MMAGENTAA", "RREDD", "WWHITEE", "YYELLOWW"]

    for _ in range(len(colours)):
        text = text.replace(colours[_], colours_alt[_])

    if mode == 1: # default
        text = str(text).replace("[",f"{magenta}[{white}").replace("]",f"{magenta}]{white}")
        for char in chars: text = text.replace(char, f"{magenta}{char}{white}")
        for bool in chars_2: text = text.replace(bool, f"{green}{bool}{white}")
        for bool in chars_3: text = text.replace(bool, f"{red}{bool}{white}")
    
    elif mode == 2: # for error messages
        text = str(text).replace("[",f"{white}[{red}").replace("]",f"{white}]{red}")
        for char in chars: text = text.replace(char, f"{white}{char}{red}")
        for bool in chars_2: text = text.replace(bool, f"{green}{bool}{red}")
        return str(f"{red}{text}" + Style.RESET_ALL)
    
    elif mode == 3: # random | TRUE, FALSE will not be coloured!
        text = [char for char in text]; bad_colours = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
        codes = vars(Fore); colours = [codes[colour] for colour in codes if colour not in bad_colours]
        for _ in range(len(text)):
            char = text[_]
            if char != ' ':
                if char in ( ['[',']'] + chars ): text[_] = white + char
                else: text[_] = random.choice(colours) + Style.BRIGHT + char

    else: return str(f"\n  {white}> {red}CLR ERROR{white}! - {red}Wrong mode {white}[{red}{mode}{white}]" + Style.RESET_ALL)
    
    for _ in range(len(colours)):
        text = text.replace(colours_alt[_], colours[_])

    if mode == 1: return str(f"{white}{text}" + Style.RESET_ALL)
    elif mode == 2: return str(f"{red}{text}" + Style.RESET_ALL)
    elif mode == 3: return str(''.join(text) + Style.RESET_ALL)

# [NOTE] align supports: clr, clr_banner (colorama), does not support: fade

def align(text: str) -> str: # center align banner / line ( supports both coloured and non-coloured )
    
    width = os.get_terminal_size().columns; aligned = text
    for colour in vars(Fore).values(): aligned = aligned.replace(colour,'')
    for style in vars(Style).values(): aligned = aligned.replace(style,'')
    text = text.split('\n'); aligned = aligned.split('\n')
    for _ in range(len(aligned)): aligned[_] = aligned[_].center(width).replace(aligned[_],text[_])
    return str('\n'.join(aligned) + Style.RESET_ALL)

def clr_banner(banner: str) -> str: # randomized banner color

    bad_colours = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
    codes = vars(Fore); colours = [codes[colour] for colour in codes if colour not in bad_colours]
    colored_chars = [random.choice(colours) + Style.BRIGHT + char if char != ' ' else char for char in banner]
    return str(''.join(colored_chars) + Style.RESET_ALL)

def fade(text: str, colour: str = "purple") -> str: # credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3

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

# functions for windows executables [ dankware ]

def title(title: str) -> None: # changes title

    os.system(f"title {title}")
    
def rm_line() -> None: # deletes previous line

    print("\033[A                             \033[A")

def chdir(mode: str) -> str: # changes directory to filepath

    if mode == "script": return "os.chdir(os.path.dirname(__file__))" # as .py
    elif mode == "exe": return "os.chdir(os.path.dirname(sys.argv[0]))" # as .exe
 
def error(exception: Exception) -> None: # exception / error handler
    
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print(clr(f"\n  > Error: {str(exception)} | {exc_type} | Line: {exc_tb.tb_lineno}",2))
    
def github_downloads(url: str) -> list: # extracts download urls from latest release on github and returns as list | example input > https://api.github.com/repos/EXAMPLE/EXAMPLE/releases/latest | example output > ['https://github.com/EXAMPLE/EXAMPLE/releases/download/VERSION/EXAMPLE.TXT']

    if "https://api.github.com/repos/" not in url or "/releases/latest" not in url: print(clr('  > Invalid url! Must follow: "https://api.github.com/repos/NAME/NAME/releases/latest"',2)); time.sleep(5); sys.exit(1)    
    while True:
        try: response = str(json.dumps(requests.get(url).json(), indent=4)).splitlines(); urls = []; break
        except: wait = input(clr("  > Make sure you are connected to the Internet! Press [ENTER] to try again... ",2))
    for line in response:
        if "browser_download_url" in line: urls.append(line.replace('"','').split(' ')[-1])
    return urls

def dankware_banner() -> None: # dankware banner printer with github url

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

