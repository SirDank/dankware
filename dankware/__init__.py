from concurrent.futures import ThreadPoolExecutor, as_completed
from alive_progress import alive_bar
from colorama import Fore, Style
import random
import time
import os

white = Fore.WHITE + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT

def multithread(function, threads: int = 1, input_one = None, input_two = None, progress_bar: bool = True) -> None:

    futures = []
    executor = ThreadPoolExecutor(max_workers=threads)
    one_isList = type(input_one) is list
    two_isList = type(input_two) is list
    if input_one is None:one_isNone = True
    else:one_isNone = False
    if input_two is None:two_isNone = True
    else:two_isNone = False

    if one_isNone:
        for i in range(threads):futures.append(executor.submit(function))
    
    elif two_isNone:

        if one_isList:
            for item in input_one:futures.append(executor.submit(function, item))
        else:
            for i in range(threads):futures.append(executor.submit(function, input_one))

    elif not one_isNone and not two_isNone:

        if one_isList and two_isList:
            if len(input_one) != len(input_two):print(clr(f"\n  > MULTITHREAD ERROR! - input_one[{len(input_one)}] and input_two[{len(input_two)}] do not have the same length!",2) + Style.RESET_ALL);return
            for index in range(len(input_one)):futures.append(executor.submit(function, input_one[index], input_two[index]))
            
        elif one_isList:
            for index in range(len(input_one)):futures.append(executor.submit(function, input_one[index], input_two))
            
        elif two_isList:
            for index in range(len(input_two)):futures.append(executor.submit(function, input_one, input_two[index]))
            
        elif not one_isList and not two_isList:
            for i in range(threads):futures.append(executor.submit(function, input_one, input_two))

    if progress_bar:
        with alive_bar(int(len(futures))) as bar:
            for future in as_completed(futures):
                try:future.result();bar()
                except:bar()
    else:
        for future in as_completed(futures):
            try:future.result()
            except:pass

def cls() -> None:
    if os.name == 'nt':_ = os.system('cls')
    else:_ = os.system('clear')

def clr(text: str, mode: int = 1) -> str: # colour chars with magenta and white / red and white

    if mode == 1:
        text = str(text).replace("[",f"{magenta}[{white}").replace("]",f"{magenta}]{white}")
        for char in ['>','.',',','=','-','!','|','(',')','/',':']:text = text.replace(char, f"{magenta}{char}{white}")
        for bool in ['true', 'True', 'TRUE']:text = text.replace(bool, f"{green}{bool}{white}")
        for bool in ['false', 'False', 'FALSE']:text = text.replace(bool, f"{red}{bool}{white}")
        return f"{white}{text}" + Style.RESET_ALL
    
    elif mode == 2:
        text = str(text).replace("[",f"{white}[{red}").replace("]",f"{white}]{red}")
        for char in ['>','.',',','=','-','!','|','(',')','/',':']:text = text.replace(char, f"{white}{char}{red}")
        for bool in ['true', 'True', 'TRUE']:text = text.replace(bool, f"{green}{bool}{red}")
        return f"{red}{text}" + Style.RESET_ALL
    
    else:return f"\n  {white}> {red}CLR ERROR{white}! - {red}Wrong mode {white}[{red}{mode}{white}]" + Style.RESET_ALL

def clr_banner(banner: str) -> str: # randomized banner color

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
    codes = vars(Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    return ''.join(colored_chars) + Style.RESET_ALL

def align_banner(banner: str, coloured_banner: str = "") -> str: # center align banner with terminal size ( supports coloured and non-coloured )

    width = os.get_terminal_size().columns
    banner = banner.splitlines()
    if coloured_banner == "":coloured = False
    else:coloured_banner = coloured_banner.splitlines();coloured = True
    for i in range(len(banner)):
        if coloured:banner[i] = banner[i].center(width).replace(banner[i],coloured_banner[i])
        else:banner[i] = banner[i].center(width)
    return '\n'.join(banner) + Style.RESET_ALL
        
def dankware_banner() -> None:

    banner="\n 8 888888888o.     \n 8 8888    `^888.  \n 8 8888        `88.\n 8 8888         `88\n 8 8888          88\n 8 8888          88\n 8 8888         ,88\n 8 8888        ,88'\n 8 8888    ,o88P'  \n 8 888888888P'     \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n b.             8\n 888o.          8\n Y88888o.       8\n .`Y888888o.    8\n 8o. `Y888888o. 8\n 8`Y8o. `Y88888o8\n 8   `Y8o. `Y8888\n 8      `Y8o. `Y8\n 8         `Y8o.`\n 8            `Yo\n\n\n 8 8888     ,88'\n 8 8888    ,88' \n 8 8888   ,88'  \n 8 8888  ,88'   \n 8 8888 ,88'    \n 8 8888 88'     \n 8 888888<      \n 8 8888 `Y8.    \n 8 8888   `Y8.  \n 8 8888     `Y8.\n\n\n `8.`888b                 ,8'\n  `8.`888b               ,8' \n   `8.`888b             ,8'  \n    `8.`888b     .b    ,8'   \n     `8.`888b    88b  ,8'    \n      `8.`888b .`888b,8'     \n       `8.`888b8.`8888'      \n        `8.`888`8.`88'       \n         `8.`8' `8,`'        \n          `8.`   `8'         \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n 8 888888888o.  \n 8 8888    `88. \n 8 8888     `88 \n 8 8888     ,88 \n 8 8888.   ,88' \n 8 888888888P'  \n 8 8888`8b      \n 8 8888 `8b.    \n 8 8888   `8b.  \n 8 8888     `88.\n\n\n 8 8888888888   \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n 8 8888         \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n "
    cls()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in align_banner(banner, clr_banner(banner)).splitlines():time.sleep(0.05);print(line)
    for i in range(18):time.sleep(0.1);print("\n")
    cls()
    
def fade(text: str, colour: str = "purple") -> str: # credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3

    colour = colour.lower()
    available_colours = ['black','red','green','cyan','blue','purple','random','black-v','red-v','green-v','cyan-v','blue-v','purple-v','pink-v']
    valid_colour = False
    for available in available_colours:
        if colour == available:valid_colour = True
    if not valid_colour:return clr(f"\n  > FADE ERROR! - Invalid colour: {colour} | Available colours: {', '.join(available_colours)}") + Style.RESET_ALL
        
    faded = ""
    if len(text.splitlines()) > 1:multi_line = True
    else:multi_line = False

    if colour == "black":
        for line in text.splitlines():
            R = 0; G = 0; B = 0
            for character in line:
                R += 3; G += 3; B += 3
                if R > 255 and G > 255 and B > 255:R = 255; G = 255; B = 255
                faded += f"\033[38;2;{R};{G};{B}m{character}\033[0m"
            if multi_line:faded += "\n"
            
    elif colour == "red":
        for line in text.splitlines():
            G = 250
            for character in line:
                G -= 5
                if G < 0:G = 0
                faded += f"\033[38;2;255;{G};0m{character}\033[0m"
            if multi_line:faded += "\n"
            
    elif colour == "green":
        for line in text.splitlines():
            R = 0
            for character in line:
                if not R > 200:R += 3
                faded += f"\033[38;2;{R};255;0m{character}\033[0m"
            if multi_line:faded += "\n"
            
    elif colour == "cyan":
        for line in text.splitlines():
            B = 100
            for character in line:
                B += 2
                if B > 255:B = 255
                faded += f"\033[38;2;0;255;{B}m{character}\033[0m"
            if multi_line:faded += "\n"

    elif colour == "blue":
        for line in text.splitlines():
            G = 0
            for character in line:
                G += 3
                if G > 255:G = 255
                faded += f"\033[38;2;0;{G};255m{character}\033[0m"
            if multi_line:faded += "\n"
        
    elif colour == "purple":
        for line in text.splitlines():
            R = 35
            for character in line:
                R += 3
                if R > 255:R = 255
                faded += f"\033[38;2;{R};0;220m{character}\033[0m"
            if multi_line:faded += "\n"

    elif colour == "black-v":
        R = 0; G = 0; B = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{R};{G};{B}m{line}\033[0m")
            if not R == 255 and not G == 255 and not B == 255:
                R += 20; G += 20; B += 20
                if R > 255 and G > 255 and B > 255:R = 255; G = 255; B = 255
            if multi_line:faded += "\n"
                    
    elif colour == "red-v":
        G = 250
        for line in text.splitlines():
            faded += f"\033[38;2;255;{G};0m{line}\033[0m"
            if not G == 0:
                G -= 25
                if G < 0:
                    G = 0
            if multi_line:faded += "\n"

    elif colour == "green-v":
        R = 0
        for line in text.splitlines():
            faded += f"\033[38;2;{R};255;0m{line}\033[0m"
            if not R > 200:R += 30
            if multi_line:faded += "\n"
        
    elif colour == "cyan-v":
        B = 100
        for line in text.splitlines():
            faded += f"\033[38;2;0;255;{B}m{line}\033[0m"
            if not B == 255:
                B += 15
                if B > 255:B = 255
            if multi_line:faded += "\n"
        
    elif colour == "blue-v":
        G = 10
        for line in text.splitlines():
            faded += f"\033[38;2;0;{G};255m{line}\033[0m"
            if not G == 255:
                G += 15
                if G > 255:G = 255
            if multi_line:faded += "\n"
        
    elif colour == "purple-v":
        R = 40
        for line in text.splitlines():
            faded += f"\033[38;2;{R};0;220m{line}\033[0m"
            if not R == 255:
                R += 15
                if R > 255:R = 255
            if multi_line:faded += "\n"
        
    elif colour == "pink-v":
        B = 255
        for line in text.splitlines():
            faded += f"\033[38;2;255;0;{B}m{line}\033[0m"
            if not B == 0:
                B -= 20
                if B < 0:B = 0
            if multi_line:faded += "\n"

    elif colour == "random":
        for line in text.splitlines():
            for character in line:
                R, G, B = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                faded += f"\033[38;2;{R};{G};{B}m{character}\033[0m"
            if multi_line:faded += "\n"
    
    else:return clr(f"\n  > FADE ERROR! - [{colour}] is not supported yet!",2) + Style.RESET_ALL
    
    if multi_line:faded = faded[:-1]
    return faded