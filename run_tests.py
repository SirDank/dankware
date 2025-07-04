import os
import sys
import time
import random
from colorama import Style, Fore
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from dankware import (
    err,
    fade,
    get_duration,
    get_path,
    github_downloads,
    github_file_selector,
    multithread,
    random_ip,
    clr,
    align,
    cls,
)
from dankware import (
    white_bright,
    white_normal,
    white_dim,
    red_bright,
    red_normal,
    red_dim,
    green,
    white,
    magenta,
    reset,
)

cls()
a = 0
sum = 0


def main():
    COUNTER = 0

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    def example():
        global a
        a += 1
        print(a)
        time.sleep(1)

    multithread(example, 10)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    new_list = [1, 2, 3, 4, 5]

    def example1(num):
        global sum
        sum += num
        time.sleep(1)

    multithread(example1, 10, new_list)  # input_one: list
    print(sum)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]

    def example2(num1, num2):
        print(num1 + num2)
        time.sleep(1)

    multithread(example2, 10, list1, list2)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    new_list = [1, 2, 3, 4, 5]

    def example(num1, num2):
        print(f"{num1} + {num2} = {num1 + num2}")
        time.sleep(1)

    multithread(example, 10, new_list, 5, progress_bar=False)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(random_ip())

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    def random_ip_old() -> str:
        excluded_prefixes_one = [
            "6.",
            "7.",
            "10.",
            "11.",
            "21.",
            "22.",
            "26.",
            "28.",
            "29.",
            "30.",
            "33.",
            "55.",
            "127.",
            "136.",
            "205.",
            "214.",
            "215.",
        ]
        excluded_prefixes_two = [
            "23.27.",
            "31.25.",
            "50.117.",
            "74.115.",
            "75.127.",
            "81.87.",
            "100.64.",
            "128.16.",
            "128.40.",
            "128.41.",
            "128.86.",
            "128.232.",
            "128.240.",
            "128.243.",
            "129.11.",
            "129.12.",
            "129.31.",
            "129.67.",
            "129.123.",
            "129.169.",
            "129.215.",
            "129.234.",
            "130.88.",
            "130.159.",
            "130.209.",
            "130.246.",
            "131.111.",
            "131.227.",
            "131.231.",
            "131.251.",
            "134.36.",
            "134.83.",
            "134.151.",
            "134.219.",
            "134.220.",
            "134.225.",
            "136.148.",
            "136.156.",
            "137.44.",
            "137.50.",
            "137.73.",
            "137.108.",
            "137.195.",
            "137.222.",
            "137.253.",
            "138.38.",
            "138.40.",
            "138.250.",
            "138.253.",
            "139.133.",
            "139.153.",
            "139.166.",
            "139.184.",
            "139.222.",
            "140.97.",
            "141.163.",
            "141.241.",
            "142.111.",
            "142.252.",
            "143.52.",
            "143.117.",
            "143.167.",
            "143.210.",
            "143.234.",
            "144.32.",
            "144.39.",
            "144.82.",
            "144.124.",
            "144.173.",
            "146.87.",
            "146.97.",
            "146.169.",
            "146.176.",
            "146.179.",
            "146.191.",
            "146.227.",
            "147.143.",
            "147.188.",
            "147.197.",
            "148.79.",
            "148.88.",
            "148.197.",
            "149.155.",
            "149.170.",
            "150.204.",
            "152.71.",
            "152.78.",
            "152.105.",
            "153.11.",
            "155.198.",
            "155.245.",
            "157.140.",
            "157.228.",
            "158.94.",
            "158.125.",
            "158.143.",
            "158.223.",
            "159.92.",
            "160.5.",
            "160.9.",
            "161.73.",
            "161.74.",
            "161.76.",
            "161.112.",
            "163.1.",
            "163.119.",
            "163.160.",
            "163.167.",
            "164.11.",
            "165.160.",
            "166.88.",
            "169.254.",
            "172.252.",
            "192.168.",
            "192.177.",
            "192.186.",
            "193.60.",
            "194.66.",
            "194.80.",
            "195.194.",
            "198.18.",
            "205.164.",
            "212.121.",
            "212.219.",
        ]
        excluded_prefixes_three = [
            "4.53.201.",
            "5.152.179.",
            "8.12.162.",
            "8.12.163.",
            "8.12.164.",
            "8.14.84.",
            "8.14.145.",
            "8.14.146.",
            "8.14.147.",
            "8.17.250.",
            "8.17.251.",
            "8.17.252.",
            "23.231.128.",
            "31.25.2.",
            "31.25.4.",
            "37.72.112.",
            "37.72.172.",
            "38.72.200.",
            "46.254.200.",
            "50.93.192.",
            "50.93.193.",
            "50.93.194.",
            "50.93.195.",
            "50.93.196.",
            "50.93.197.",
            "50.115.128.",
            "50.118.128.",
            "63.141.222.",
            "64.62.253.",
            "64.92.96.",
            "64.145.79.",
            "64.145.82.",
            "64.158.146.",
            "65.49.24.",
            "65.49.93.",
            "65.162.192.",
            "66.79.160.",
            "66.160.191.",
            "68.68.96.",
            "69.46.64.",
            "69.176.80.",
            "72.13.80.",
            "72.52.76.",
            "74.82.43.",
            "74.82.160.",
            "74.114.88.",
            "74.115.2.",
            "74.115.4.",
            "74.122.100.",
            "85.12.64.",
            "89.207.208.",
            "92.245.224.",
            "103.251.91.",
            "108.171.32.",
            "108.171.42.",
            "108.171.52.",
            "108.171.62.",
            "118.193.78.",
            "130.93.16.",
            "132.206.9.",
            "132.206.123.",
            "132.206.125.",
            "141.170.64.",
            "141.170.96.",
            "141.170.100.",
            "146.82.55.93",
            "149.54.136.",
            "149.54.152.",
            "159.86.128.",
            "173.245.64.",
            "173.245.194.",
            "173.245.220.",
            "173.252.192.",
            "178.18.16.",
            "178.18.26.",
            "178.18.27.",
            "178.18.28.",
            "178.18.29.",
            "183.182.22.",
            "185.83.168.",
            "192.12.72.",
            "192.18.195.",
            "192.35.172.",
            "192.41.104.",
            "192.41.112.",
            "192.41.128.",
            "192.68.153.",
            "192.76.6.",
            "192.76.8.",
            "192.76.16.",
            "192.76.32.",
            "192.82.153.",
            "192.84.5.",
            "192.84.75.",
            "192.84.76.",
            "192.84.80.",
            "192.84.212.",
            "192.88.9.",
            "192.88.10.",
            "192.88.99.",
            "192.92.114.",
            "192.94.235.",
            "192.100.78.",
            "192.100.154.",
            "192.107.168.",
            "192.108.120.",
            "192.124.46.",
            "192.133.244.",
            "192.149.111.",
            "192.150.180.",
            "192.150.184.",
            "192.153.213.",
            "192.155.160.",
            "192.156.162.",
            "192.160.194.",
            "192.171.128.",
            "192.171.192.",
            "192.173.1.",
            "192.173.2.",
            "192.173.4.",
            "192.173.128.",
            "192.188.157.",
            "192.188.158.",
            "192.190.201.",
            "192.190.202.",
            "192.195.42.",
            "192.195.105.",
            "192.195.116.",
            "192.195.118.",
            "192.249.64.",
            "192.250.240.",
            "193.32.22.",
            "193.37.225.",
            "193.37.240.",
            "193.38.143.",
            "193.39.80.",
            "193.39.172.",
            "193.39.212.",
            "193.107.116.",
            "193.130.15.",
            "193.133.28.",
            "193.138.86.",
            "194.32.32.",
            "194.35.93.",
            "194.35.186.",
            "194.35.192.",
            "194.35.241.",
            "194.36.1.",
            "194.36.2.",
            "194.36.121.",
            "194.36.152.",
            "194.60.218.",
            "194.110.214.",
            "194.187.32.",
            "198.12.120.",
            "198.12.121.",
            "198.12.122.",
            "198.51.100.",
            "198.144.240.",
            "199.33.120.",
            "199.33.124.",
            "199.48.147.",
            "199.68.196.",
            "199.127.240.",
            "199.187.168.",
            "199.188.238.",
            "199.255.208.",
            "203.12.6.",
            "204.13.64.",
            "204.16.192.",
            "204.19.238.",
            "204.74.208.",
            "204.113.91.",
            "205.159.189.",
            "205.209.128.",
            "206.108.52.",
            "206.165.4.",
            "208.77.40.",
            "208.80.4.",
            "208.123.223.",
            "209.51.185.",
            "209.54.48.",
            "209.107.192.",
            "209.107.210.",
            "209.107.212.",
            "211.156.110.",
            "212.121.192.",
            "216.151.183.",
            "216.151.190.",
            "216.172.128.",
            "216.185.36.",
            "216.218.233.",
            "216.224.112.",
        ]

        """
        Generates a random valid computer ip
        - Follows: https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf
        """

        while True:
            ip = f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

            if any(ip.startswith(prefix) for prefix in excluded_prefixes_one):
                continue
            elif any(ip.startswith(prefix) for prefix in excluded_prefixes_two):
                continue
            elif any(ip.startswith(prefix) for prefix in excluded_prefixes_three):
                continue

            if (
                ip.startswith("172.")
                and int(ip.split(".")[1]) >= 16
                and int(ip.split(".")[1]) <= 31
            ):
                continue
            elif ip.startswith("192."):
                if (
                    ip.endswith(".170")
                    or ip.endswith(".171")
                    or ip.split(".")[2] == "2"
                ):
                    continue
            elif ip.startswith("203.") and ip.split(".")[2] == "113":
                continue
            elif (
                ip.startswith("216.83.")
                and int(ip.split(".")[2]) >= 33
                and int(ip.split(".")[2]) <= 63
            ):
                continue
            elif ip.endswith(".255.255.255"):
                continue

            break

        return ip

    def gen_old():
        while True:
            ip = random_ip_old()
            if ip in ips:
                continue
            ips[ip] = ""
            break

    def gen_new():
        while True:
            ip = random_ip()
            if ip in ips:
                continue
            ips[ip] = ""
            break

    gen_rate = 10000
    repeat_amt = 10

    print(clr(f"\n  Generating {gen_rate * repeat_amt} unique ips [ old ]"))

    ips = {}
    start_time = datetime.now()
    for _ in range(repeat_amt):
        multithread(gen_old, gen_rate, progress_bar=False)

    print(clr(f"\n  > Time Taken: {get_duration(start_time)}"))

    print(clr(f"\n  Generating {gen_rate * repeat_amt} unique ips [ new ]"))

    ips = {}
    start_time = datetime.now()
    for _ in range(repeat_amt):
        multithread(gen_new, gen_rate, progress_bar=False)

    print(clr(f"\n  > Time Taken: {get_duration(start_time)}"))

    print("")

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    try:
        value = 1 / 0
    except Exception as exc:
        print(clr(err((type(exc), exc, exc.__traceback__)), 2))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    try:
        value = 1 / 0
    except Exception as exc:
        print(clr(err((type(exc), exc, exc.__traceback__), "mini"), 2))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    for url in github_downloads("EssentialsX/Essentials"):
        print(url)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    for url in github_file_selector(
        "EssentialsX/Essentials",
        "remove",
        ("AntiBuild", "Discord", "GeoIP", "Protect", "XMPP"),
    ):
        print(url)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    if os.name == "nt":
        locations = (
            "AppData",
            "Desktop",
            "Documents",
            "Favorites",
            "Local AppData",
            "Music",
            "Pictures",
            "Videos",
        )
    elif os.name == "posix":
        locations = ("Desktop", "Documents", "Downloads", "Pictures", "Videos", "Music")
    for location in locations:
        path = get_path(location)
        print(path)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(clr("\n  > Hey! Long time no see :)"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(clr("\n  > Hey! Long time no see :)", colour_one=magenta, colour_two=white))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(clr("\n  This is a string: True | This is an integer: False"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(clr("\n  EXEC STATUS: [SUCCESS]! | PROGRESS: 100%"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(
        clr(
            f"\n  > {magenta}Purple{white} thinks he's better than everyone else :(",
            colour_two=green,
        )
    )

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(clr("\n  > Error in sector [7] redirecting... | INTEGRITY_CHECK: SUCCESS", 2))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(
        clr(
            "\n  > Is this a randomly coloured string: TRUE | As you can see it does not colour True/False",
            3,
        )
    )

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(
        clr(
            "\n  > This is a randomly coloured string based on the input colours!",
            3,
            colours=(
                white_bright,
                white_normal,
                white_dim,
                red_bright,
                red_normal,
                red_dim,
            ),
        )
    )

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    codes = vars(Fore)
    colours = [codes[colour] for colour in codes]
    for colour in colours:
        print(colour + Style.BRIGHT + "BRIGHT" + reset)
        print(colour + Style.NORMAL + "NORMAL" + reset)
        print(colour + Style.DIM + "DIM" + reset)

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    banner = """

     888                   888                                             
     888                   888           s i r . d a n k ' s               
     888                   888                                             
 .d88888  8888b.  88888b.  888  888 888  888  888  8888b.  888d888 .d88b.  
d88" 888     "88b 888 "88b 888 .88P 888  888  888     "88b 888P"  d8P  Y8b 
888  888 .d888888 888  888 888888K  888  888  888 .d888888 888    88888888 
Y88b 888 888  888 888  888 888 "88b Y88b 888 d88P 888  888 888    Y8b.     
 "Y88888 "Y888888 888  888 888  888  "Y8888888P"  "Y888888 888     "Y8888  

"""
    print(clr(banner, 4))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(align(banner))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(clr(align(banner), 4))
    print(align(clr(banner, 4)))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    banner = """

                              888 d8b                   888    
       v e n a x y t ' s      888 Y8P                   888    
                              888                       888    
 .d88b.  888d888 8888b.   .d88888 888  .d88b.  88888b.  888888 
d88P"88b 888P"      "88b d88" 888 888 d8P  Y8b 888 "88b 888    
888  888 888    .d888888 888  888 888 88888888 888  888 888    
Y88b 888 888    888  888 Y88b 888 888 Y8b.     888  888 Y88b.  
 "Y88888 888    "Y888888  "Y88888 888  "Y8888  888  888  "Y888 
     888                                                       
Y8b d88P                                                       
 "Y88P"                                                        


"""

    print(fade(banner, "random"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "black2white"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "black2white-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "yellow2red"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "yellow2red-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "green2yellow"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "green2yellow-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "green2cyan"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "green2cyan-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "blue2cyan"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "blue2cyan-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "blue2pink"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "blue2pink-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "pink2red"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade(banner, "pink2red-v"))

    COUNTER += 1
    print(
        clr(
            f"\n___[{COUNTER}]__________________________________________________________________________________\n"
        )
    )

    print(fade("\n  > This is a test string!", "pink2red"))

    # COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________\n"))

    # print('\n'.join(sorted(tuple(sys.modules))))


if __name__ == "__main__":
    main()
