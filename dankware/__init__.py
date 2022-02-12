from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore, Style
from alive_progress import alive_bar
import random
import time
import os

def multithread(function, threads = 1, input_one = None, input_two = None, progress_bar = True) -> None:

    futures = []
    executor = ThreadPoolExecutor(max_workers=threads)
    one_isList = type(input_one) is list
    two_isList = type(input_two) is list
    one_isNone = type(input_one) is None
    two_isNone = type(input_two) is None
    
    if one_isNone:
        for i in range(threads):futures.append(executor.submit(function))
    
    elif two_isNone:

        if one_isList:
            for item in input_one:futures.append(executor.submit(function, item))
        else:
            for i in range(threads):futures.append(executor.submit(function, input_one))

    elif not one_isNone and not two_isNone:

        if one_isList and two_isList:
            if len(input_one) != len(input_two):print(f"\n  > MULTITHREAD ERROR! - input_one[{len(input_one)}] and input_two[{len(input_two)}] do not have the same length!");return
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

def clr_banner(banner: str) -> str: # randomized banner color
    
    init(autoreset=True)
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
    codes = vars(Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    return ''.join(colored_chars)

def align_banner(banner: str, coloured_banner = "") -> str: # center align banner with terminal size ( supports coloured and non-coloured )
    
    width = os.get_terminal_size().columns
    banner = banner.splitlines()
    if coloured_banner == "":coloured = False
    else:coloured_banner = coloured_banner.splitlines();coloured = True
    for i in range(len(banner)):
        if coloured:banner[i] = banner[i].center(width).replace(banner[i],coloured_banner[i])
        else:banner[i] = banner[i].center(width)
    return '\n'.join(banner)
        
def dankware_banner() -> None:
    
    init(autoreset=True)
    banner="\n 8 888888888o.     \n 8 8888    `^888.  \n 8 8888        `88.\n 8 8888         `88\n 8 8888          88\n 8 8888          88\n 8 8888         ,88\n 8 8888        ,88'\n 8 8888    ,o88P'  \n 8 888888888P'     \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n b.             8\n 888o.          8\n Y88888o.       8\n .`Y888888o.    8\n 8o. `Y888888o. 8\n 8`Y8o. `Y88888o8\n 8   `Y8o. `Y8888\n 8      `Y8o. `Y8\n 8         `Y8o.`\n 8            `Yo\n\n\n 8 8888     ,88'\n 8 8888    ,88' \n 8 8888   ,88'  \n 8 8888  ,88'   \n 8 8888 ,88'    \n 8 8888 88'     \n 8 888888<      \n 8 8888 `Y8.    \n 8 8888   `Y8.  \n 8 8888     `Y8.\n\n\n `8.`888b                 ,8'\n  `8.`888b               ,8' \n   `8.`888b             ,8'  \n    `8.`888b     .b    ,8'   \n     `8.`888b    88b  ,8'    \n      `8.`888b .`888b,8'     \n       `8.`888b8.`8888'      \n        `8.`888`8.`88'       \n         `8.`8' `8,`'        \n          `8.`   `8'         \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n 8 888888888o.  \n 8 8888    `88. \n 8 8888     `88 \n 8 8888     ,88 \n 8 8888.   ,88' \n 8 888888888P'  \n 8 8888`8b      \n 8 8888 `8b.    \n 8 8888   `8b.  \n 8 8888     `88.\n\n\n 8 8888888888   \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n 8 8888         \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n "
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in align_banner(banner, clr_banner(banner)).splitlines():
        time.sleep(0.05);print(line)
    for i in range(18):
        time.sleep(0.1);print("\n")
    os.system('cls')
    
def fade(text: str, colour = "purple", direction = "H") -> str: # credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3
    
    colour = colour.lower()
    direction = str(direction).upper()
    available_colours = ['black', 'red', 'green', 'cyan', 'blue', 'purple', 'pink', 'random']
    valid_colour = False
    for available in available_colours:
        if colour == available:valid_colour = True
    if not valid_colour:
        print(f"\n  > FADE ERROR! - Invalid colour: {colour} | Available colours: {', '.join(available_colours)}");return
        
    faded = ""
    if direction == "H":
        
        if colour == "black":
            for line in text.splitlines():
                red = 0; green = 0; blue = 0
                for character in line:
                    red += 3; green += 3; blue += 3
                    if red > 255 and green > 255 and blue > 255:red = 255; green = 255; blue = 255
                    faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
                faded += "\n"
                
        elif colour == "red":
            for line in text.splitlines():
                green = 250
                for character in line:
                    green -= 5
                    if green < 0:green = 0
                    faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
                faded += "\n"
                
        elif colour == "green":
            for line in text.splitlines():
                red = 0
                for character in line:
                    if not red > 200:red += 3
                    faded += (f"\033[38;2;{red};255;0m{character}\033[0m")
                faded += "\n"
                
        elif colour == "cyan":
            for line in text.splitlines():
                blue = 100
                for character in line:
                    blue += 2
                    if blue > 255:blue = 255
                    faded += (f"\033[38;2;0;255;{blue}m{character}\033[0m")
                faded += "\n"

        elif colour == "blue":
            for line in text.splitlines():
                green = 0
                for character in line:
                    green += 3
                    if green > 255:green = 255
                    faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
                faded += "\n"
            
        elif colour == "purple":
            for line in text.splitlines():
                red = 35
                for character in line:
                    red += 3
                    if red > 255:red = 255
                    faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
                faded += "\n"
                
        #elif colour == "random":

        else:print(f"\n  > FADE ERROR! - [{colour}] is not supported yet for the [H] direction, try [V]!")
        return faded
        
    elif direction == "V":
        
        if colour == "black":
            red = 0; green = 0; blue = 0
            for line in text.splitlines():
                faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
                if not red == 255 and not green == 255 and not blue == 255:
                    red += 20; green += 20; blue += 20
                    if red > 255 and green > 255 and blue > 255:red = 255; green = 255; blue = 255
                        
        elif colour == "red":
            green = 250
            for line in text.splitlines():
                faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
                if not green == 0:
                    green -= 25
                    if green < 0:
                        green = 0

        elif colour == "green":
            red = 0
            for line in text.splitlines():
                faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
                if not red > 200:red += 30
            
        elif colour == "cyan":
            blue = 100
            for line in text.splitlines():
                faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
                if not blue == 255:
                    blue += 15
                    if blue > 255:blue = 255
            
        elif colour == "blue":
            green = 10
            for line in text.splitlines():
                faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
                if not green == 255:
                    green += 15
                    if green > 255:green = 255
            
        elif colour == "purple":
            red = 40
            for line in text.splitlines():
                faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
                if not red == 255:
                    red += 15
                    if red > 255:red = 255
            
        elif colour == "pink":
            blue = 255
            for line in text.splitlines():
                faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
                if not blue == 0:
                    blue -= 20
                    if blue < 0:blue = 0
 
        elif colour == "random":
            for line in text.splitlines():
                for character in line:
                    faded += (f"\033[38;2;{random.randint(0,255)};{random.randint(0,255)};{random.randint(0,255)}m{character}\033[0m")
                faded += "\n"
            
        else:print(f"\n  > FADE ERROR! - [{colour}] is not supported yet for the [V] direction, try [H]!")
        return faded
        
    else:print(f"\n  > FADE ERROR! - invalid direction: {direction} | Either \"H\" or \"V\"")