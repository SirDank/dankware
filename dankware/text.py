import random
from colorama import Style, Fore
from shutil import get_terminal_size
from . import white_bright, red, reset, green_bright, red_bright, red_normal

SYMBOLS = (
    "[",
    "]",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "+",
    "-",
    "=",
    "{",
    "}",
    "|",
    "\\",
    ";",
    ":",
    "'",
    '"',
    ",",
    ".",
    "<",
    ">",
    "/",
    "?",
    "`",
    "~",
)
WORDS_GREEN = (
    "true",
    "True",
    "TRUE",
    "online",
    "Online",
    "ONLINE",
    "successfully",
    "Successfully",
    "SUCCESSFULLY",
    "successful",
    "Successful",
    "SUCCESSFUL",
    "success",
    "Success",
    "SUCCESS",
)
WORDS_RED = (
    "falsely",
    "Falsely",
    "FALSELY",
    "false",
    "False",
    "FALSE",
    "offline",
    "Offline",
    "OFFLINE",
    "failures",
    "Failures",
    "FAILURES",
    "failure",
    "Failure",
    "FAILURE",
    "failed",
    "Failed",
    "FAILED",
    "fail",
    "Fail",
    "FAIL",
)
COLOURS_TO_REPLACE = (
    Fore.BLACK,
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW,
    Style.BRIGHT,
    Style.RESET_ALL,
)
COLOURS_ALT = (
    "BBLACKK",
    "BBLUEE",
    "CCYANN",
    "GGREENN",
    "MMAGENTAA",
    "RREDD",
    "WWHITEE",
    "YYELLOWW",
    "BBRIGHTT",
    "RRESETT",
)


def align(text: str) -> str:
    """
    center align banner / line ( supports both coloured and non-coloured )
    - [NOTE] align supports: clr, does not support: fade
    """

    width = get_terminal_size().columns
    aligned = text

    for _ in tuple(vars(Fore).values()) + tuple(vars(Style).values()):
        aligned = aligned.replace(_, "")

    text = text.splitlines()
    aligned = aligned.splitlines()

    for _, __ in enumerate(aligned):
        aligned[_] = __.center(width).replace(__, text[_])

    return str("\n".join(aligned))


def random_ip() -> str:
    """
    Generates a random valid computer ip
    - Follows: https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf
    """

    while True:
        first_octet = random.randint(1, 223)
        if f"{first_octet}" in {
            "22",
            "10",
            "205",
            "30",
            "11",
            "55",
            "215",
            "29",
            "7",
            "6",
            "26",
            "214",
            "33",
            "21",
            "28",
            "127",
            "136",
        }:
            continue

        second_octet = random.randint(0, 255)
        if f"{first_octet}.{second_octet}" in {
            "161.73",
            "141.163",
            "143.52",
            "149.155",
            "139.222",
            "137.253",
            "157.228",
            "140.97",
            "146.87",
            "198.18",
            "129.169",
            "50.117",
            "146.227",
            "144.32",
            "134.83",
            "139.153",
            "160.5",
            "194.66",
            "212.219",
            "146.191",
            "129.11",
            "149.170",
            "129.67",
            "138.253",
            "134.36",
            "205.164",
            "192.177",
            "134.225",
            "139.133",
            "152.71",
            "136.148",
            "158.223",
            "137.222",
            "130.209",
            "172.252",
            "143.210",
            "164.11",
            "128.41",
            "147.143",
            "158.94",
            "192.168",
            "138.250",
            "158.125",
            "81.87",
            "134.219",
            "143.234",
            "144.82",
            "152.78",
            "128.243",
            "100.64",
            "130.246",
            "137.195",
            "152.105",
            "150.204",
            "141.241",
            "143.167",
            "139.166",
            "144.39",
            "161.74",
            "147.197",
            "163.160",
            "161.112",
            "136.156",
            "137.44",
            "143.117",
            "129.12",
            "134.220",
            "166.88",
            "134.151",
            "131.231",
            "31.25",
            "129.215",
            "153.11",
            "128.40",
            "142.111",
            "23.27",
            "75.127",
            "144.173",
            "148.79",
            "74.115",
            "192.186",
            "163.1",
            "146.176",
            "193.60",
            "129.123",
            "212.121",
            "142.252",
            "165.160",
            "146.97",
            "148.197",
            "131.251",
            "137.108",
            "163.167",
            "129.31",
            "163.119",
            "194.80",
            "130.88",
            "137.73",
            "147.188",
            "137.50",
            "130.159",
            "131.111",
            "148.88",
            "129.234",
            "131.227",
            "155.245",
            "159.92",
            "146.179",
            "169.254",
            "138.40",
            "144.124",
            "155.198",
            "139.184",
            "128.232",
            "157.140",
            "128.240",
            "158.143",
            "161.76",
            "195.194",
            "138.38",
            "128.86",
            "160.9",
            "146.169",
            "128.16",
        }:
            continue
        if first_octet == 172 and 16 <= second_octet <= 31:
            continue

        third_octet = random.randint(0, 255)
        if f"{first_octet}.{second_octet}.{third_octet}" in {
            "8.17.250",
            "194.36.2",
            "199.187.168",
            "192.173.1",
            "216.151.190",
            "193.32.22",
            "72.52.76",
            "50.93.194",
            "178.18.29",
            "74.82.43",
            "192.84.75",
            "199.255.208",
            "208.80.4",
            "198.12.120",
            "192.153.213",
            "8.14.146",
            "64.158.146",
            "69.176.80",
            "192.160.194",
            "68.68.96",
            "23.231.128",
            "173.245.194",
            "192.84.212",
            "193.107.116",
            "198.12.121",
            "192.41.112",
            "8.12.162",
            "216.172.128",
            "108.171.52",
            "192.84.76",
            "173.252.192",
            "74.122.100",
            "50.93.197",
            "141.170.100",
            "192.173.128",
            "74.115.2",
            "209.107.212",
            "192.195.118",
            "178.18.28",
            "192.133.244",
            "192.68.153",
            "192.108.120",
            "194.35.186",
            "209.107.192",
            "192.173.4",
            "194.35.241",
            "204.113.91",
            "192.35.172",
            "193.37.225",
            "199.33.120",
            "108.171.32",
            "209.54.48",
            "203.12.6",
            "50.93.196",
            "50.93.195",
            "199.48.147",
            "50.115.128",
            "192.84.5",
            "192.171.128",
            "8.14.84",
            "192.88.99",
            "216.218.233",
            "194.35.192",
            "192.76.16",
            "64.145.82",
            "185.83.168",
            "74.114.88",
            "193.37.240",
            "66.79.160",
            "69.46.64",
            "193.39.172",
            "204.74.208",
            "192.92.114",
            "192.84.80",
            "132.206.125",
            "194.60.218",
            "198.144.240",
            "63.141.222",
            "192.149.111",
            "208.123.223",
            "192.156.162",
            "192.155.160",
            "193.39.80",
            "192.195.105",
            "50.118.128",
            "38.72.200",
            "146.82.55.93",
            "192.94.235",
            "132.206.9",
            "8.14.147",
            "8.17.251",
            "192.190.201",
            "132.206.123",
            "192.250.240",
            "50.93.192",
            "74.115.4",
            "141.170.96",
            "192.107.168",
            "178.18.27",
            "193.138.86",
            "198.51.100",
            "192.100.154",
            "206.108.52",
            "74.82.160",
            "192.76.8",
            "192.76.32",
            "37.72.112",
            "192.88.10",
            "194.36.121",
            "205.159.189",
            "192.18.195",
            "149.54.152",
            "103.251.91",
            "192.195.42",
            "194.110.214",
            "199.33.124",
            "204.16.192",
            "192.100.78",
            "178.18.26",
            "194.35.93",
            "37.72.172",
            "208.77.40",
            "64.92.96",
            "212.121.192",
            "192.76.6",
            "192.249.64",
            "192.124.46",
            "211.156.110",
            "159.86.128",
            "192.173.2",
            "192.171.192",
            "85.12.64",
            "89.207.208",
            "199.188.238",
            "108.171.62",
            "64.62.253",
            "31.25.4",
            "72.13.80",
            "118.193.78",
            "8.12.164",
            "65.162.192",
            "65.49.24",
            "130.93.16",
            "205.209.128",
            "141.170.64",
            "50.93.193",
            "192.150.180",
            "192.190.202",
            "5.152.179",
            "192.150.184",
            "173.245.64",
            "209.107.210",
            "206.165.4",
            "192.41.128",
            "65.49.93",
            "183.182.22",
            "193.133.28",
            "199.68.196",
            "198.12.122",
            "192.88.9",
            "209.51.185",
            "192.12.72",
            "193.38.143",
            "149.54.136",
            "216.151.183",
            "216.224.112",
            "192.188.157",
            "194.36.152",
            "192.188.158",
            "31.25.2",
            "8.17.252",
            "108.171.42",
            "192.41.104",
            "199.127.240",
            "64.145.79",
            "193.39.212",
            "216.185.36",
            "194.187.32",
            "8.12.163",
            "178.18.16",
            "204.19.238",
            "173.245.220",
            "8.14.145",
            "92.245.224",
            "192.82.153",
            "4.53.201",
            "194.32.32",
            "192.195.116",
            "46.254.200",
            "194.36.1",
            "66.160.191",
            "204.13.64",
            "193.130.15",
        }:
            continue
        if first_octet == 203 and third_octet == 113:
            continue
        if first_octet == 216 and second_octet == 83 and 33 <= third_octet <= 63:
            continue

        fourth_octet = random.randint(0, 255)
        if first_octet == 192:
            if third_octet == 2 or fourth_octet in (170, 171):
                continue

        break

    return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"


def clr(
    text: str,
    preset: int = 1,
    colour_one: str = white_bright,
    colour_two: str = red,
    colours: tuple[str] = None,
) -> str:
    """

    this function colours special characters inside the 'symbols' tuple

    ___________________________________________

    - preset: 1 | to display general text (default)
    - text = bright white (default) / specified colour
    - symbols = bright red (default) / specified colour
    - special = bright green / bright red

    ___________________________________________

    - preset: 2 | to display error messages
    - text = red (fixed colour)
    - symbols = bright white (fixed colour)
    - special = bright green / bright red

    ___________________________________________

    - preset: 3
    - text = random (default) / colours inside input tuple
    - symbols = bright white (fixed colour)

    ___________________________________________

    - preset: 4 | to display banners
    - text & symbols = random (default) / colours inside input tuple

    """

    # default

    if preset == 1:
        for _, __ in zip(COLOURS_TO_REPLACE, COLOURS_ALT):
            text = text.replace(_, __)
        for symbol in SYMBOLS:
            text = text.replace(
                symbol, reset + colour_two + symbol + reset + colour_one
            )
        for word in WORDS_GREEN:
            text = text.replace(
                word,
                reset
                + green_bright
                + str(green_bright).join(list(word))
                + reset
                + colour_one,
            )
        for word in WORDS_RED:
            text = text.replace(
                word,
                reset
                + red_bright
                + str(red_bright).join(list(word))
                + reset
                + colour_one,
            )
        for _, __ in zip(COLOURS_ALT, COLOURS_TO_REPLACE):
            text = text.replace(_, __)
        return reset + colour_one + text + reset

    # for error messages

    if preset == 2:
        for _, __ in zip(COLOURS_TO_REPLACE, COLOURS_ALT):
            text = text.replace(_, __)
        for symbol in SYMBOLS:
            text = text.replace(symbol, reset + white_bright + symbol + reset + red)
        for word in WORDS_GREEN:
            text = text.replace(
                word,
                reset + green_bright + str(green_bright).join(list(word)) + reset + red,
            )
        for word in WORDS_RED:
            text = text.replace(
                word,
                reset + red_bright + str(red_bright).join(list(word)) + reset + red,
            )
        for _, __ in zip(COLOURS_ALT, COLOURS_TO_REPLACE):
            text = text.replace(_, __)
        return reset + red_normal + text + reset

    # random | words_green, words_red will not be coloured!

    if preset in (3, 4):
        for _ in COLOURS_TO_REPLACE:
            text = text.replace(_, "")

        text = list(text)
        colour_spl = bool(preset == 3)

        if not colours:
            text.insert(0, str(Style.BRIGHT))
            codes = vars(Fore)
            colours = tuple(
                codes[colour]
                for colour in codes
                if colour
                not in ("BLACK", "WHITE", "LIGHTBLACK_EX", "LIGHTWHITE_EX", "RESET")
            )

        for _, char in enumerate(text):
            if char not in (" ", "\n", "\t", "\r", "\b"):
                if colour_spl:
                    if char in SYMBOLS:
                        text[_] = reset + white_bright + char  # type: ignore
                    else:
                        text[_] = reset + random.choice(colours) + char  # type: ignore
                else:
                    text[_] = reset + random.choice(colours) + char  # type: ignore

        return reset + "".join(text) + reset

    raise ValueError(f"Invalid Preset: {preset} | Valid Presets: 1, 2, 3, 4")


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

    colour = colour.lower()
    if colour not in available_colours:
        raise ValueError(
            f"Invalid Colour: {colour} | Available Colours: {', '.join(available_colours)}"
        )

    faded = ""
    multi_line = bool(len(text.splitlines()) > 1)

    if colour == "random":
        for line in text.splitlines():
            for char in line:
                R, G, B = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
                faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "black2white":
        for line in text.splitlines():
            R = 0
            G = 0
            B = 0
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                R += shift
                G += shift
                B += shift
                R = min(R, 255)
                G = min(G, 255)
                B = min(B, 255)
                faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "black2white-v":
        R = 0
        G = 0
        B = 0
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;{R};{G};{B}m{line}\033[0m"
            R += shift
            G += shift
            B += shift
            R = min(R, 255)
            G = min(G, 255)
            B = min(B, 255)
            if multi_line:
                faded += "\n"

    elif colour == "yellow2red":
        for line in text.splitlines():
            G = 255
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                G -= shift
                G = max(G, 0)
                faded += f"\033[38;2;255;{G};0m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "yellow2red-v":
        G = 255
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;255;{G};0m{line}\033[0m"
            G -= shift
            G = max(G, 0)
            if multi_line:
                faded += "\n"

    elif colour == "green2yellow":
        for line in text.splitlines():
            R = 0
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                R += shift
                R = min(R, 255)
                faded += f"\033[38;2;{R};255;0m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "green2yellow-v":
        R = 0
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;{R};255;0m{line}\033[0m"
            R += shift
            R = min(R, 255)
            if multi_line:
                faded += "\n"

    elif colour == "green2cyan":
        for line in text.splitlines():
            B = 100
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                B += shift
                B = min(B, 255)
                faded += f"\033[38;2;0;255;{B}m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "green2cyan-v":
        B = 100
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;0;255;{B}m{line}\033[0m"
            B += shift
            B = min(B, 255)
            if multi_line:
                faded += "\n"

    elif colour == "blue2cyan":
        for line in text.splitlines():
            G = 0
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                G += shift
                G = min(G, 255)
                faded += f"\033[38;2;0;{G};255m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "blue2cyan-v":
        G = 10
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;0;{G};255m{line}\033[0m"
            if G != 255:
                G += shift
                G = min(G, 255)
            if multi_line:
                faded += "\n"

    elif colour == "blue2pink":
        for line in text.splitlines():
            R = 35
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                R += shift
                R = min(R, 255)
                faded += f"\033[38;2;{R};0;220m{char}\033[0m"
            if multi_line:
                faded += "\n"

    elif colour == "blue2pink-v":
        R = 40
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;{R};0;220m{line}\033[0m"
            R += shift
            R = min(R, 255)
            if multi_line:
                faded += "\n"

    elif colour == "pink2red":
        for line in text.splitlines():
            B = 255
            shift = int(255 / len(line)) if len(line) > 0 else 5
            for char in line:
                faded += f"\033[38;2;255;0;{B}m{char}\033[0m"
                B -= shift
                B = max(B, 0)
            if multi_line:
                faded += "\n"

    elif colour == "pink2red-v":
        B = 255
        shift = int(255 / len(text.splitlines())) if len(text.splitlines()) > 0 else 25
        for line in text.splitlines():
            faded += f"\033[38;2;255;0;{B}m{line}\033[0m"
            B -= shift
            B = max(B, 0)
            if multi_line:
                faded += "\n"

    else:
        raise ValueError(
            f"Invalid Colour: {colour} | Available Colours: {', '.join(available_colours)}"
        )

    if multi_line:
        faded = faded[:-1]
    return faded
