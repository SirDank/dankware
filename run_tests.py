import os
import sys
import time
import ctypes
import winreg
import random
import requests
from datetime import datetime
from colorama import Fore, Style
from traceback import extract_tb
from alive_progress import alive_bar
from concurrent.futures import ThreadPoolExecutor, as_completed
from dankware import multithread, github_downloads, github_file_selector, random_ip, is_admin, export_registry_keys, clr, align, fade, get_duration, err, cls, title, rm_line, chdir, sys_open, dankware_banner, white, magenta, green

cls()
a = 0
sum = 0

def main():
    
    COUNTER = 0
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))

    def example():
        global a
        a += 1
        print(a)
        time.sleep(1)
            
    multithread(example, 10)
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    new_list = [1, 2, 3, 4, 5]

    def example(num):
        global sum
        sum += num
        time.sleep(1)

    multithread(example, 10, new_list) # input_one: list
    print(sum)
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]

    def example(num1, num2):
        print(num1 + num2)
        time.sleep(1)

    multithread(example, 10, list1, list2)
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    new_list = [1, 2, 3, 4, 5]

    def example(num1, num2):
        print(num1 * num2)
        time.sleep(1)

    multithread(example, 10, new_list, 5, progress_bar=False)
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(random_ip())
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    try: value = 1/0
    except: print(clr(err(sys.exc_info()), 2))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))

    for url in github_downloads("EssentialsX/Essentials"): print(url)
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))

    for url in github_file_selector("EssentialsX/Essentials", "remove", ['AntiBuild', 'Discord', 'GeoIP', 'Protect', 'XMPP']): print(url)
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(clr("\n  > Hey! Long time no see :)"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(clr("\n  > Hey! Long time no see :)", colour_one = magenta, colour_two = white))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(clr("\n  This is a string: True | This is an integer: False"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(clr(f"\n  > {magenta}Purple{white} thinks he's better than everyone else :(", colour_two=green))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(clr("\n  > Error in sector [7] redirecting... | INTEGRITY_CHECK_SUCCESS: TRUE",2))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(clr("\n  > Is this a randomly coloured string: TRUE | As you can see it does not colour True/False",3))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    banner = '''

     888                   888                                             
     888                   888           s i r . d a n k ' s               
     888                   888                                             
 .d88888  8888b.  88888b.  888  888 888  888  888  8888b.  888d888 .d88b.  
d88" 888     "88b 888 "88b 888 .88P 888  888  888     "88b 888P"  d8P  Y8b 
888  888 .d888888 888  888 888888K  888  888  888 .d888888 888    88888888 
Y88b 888 888  888 888  888 888 "88b Y88b 888 d88P 888  888 888    Y8b.     
 "Y88888 "Y888888 888  888 888  888  "Y8888888P"  "Y888888 888     "Y8888  

'''
    print(clr(banner,4))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(align(banner))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(align(clr(banner,4)))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    banner = '''

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


'''
    print(fade(banner, "black"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "black-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "red"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "red-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "green"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "green-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "cyan"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "cyan-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "blue"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "blue-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "purple"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "purple-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "pink-v"))
    
    COUNTER += 1; print(clr(f"\n___[{COUNTER}]__________________________________________________________________________________"))
    
    print(fade(banner, "random"))

if __name__ == "__main__": main()
