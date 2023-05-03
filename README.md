<p align="center">
  <b>~ Visits ~</b><br><br>
  <img src="https://profile-counter.glitch.me/dankware/count.svg" />
</p>

<p align="center">
  <b>~ Stats ~</b><br><br>
  <img src="https://static.pepy.tech/personalized-badge/dankware?period=total&units=international_system&left_color=black&right_color=brightgreen&left_text=downloads" />
  <img src="https://static.pepy.tech/personalized-badge/dankware?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=downloads%20/%20month" />
  <img src="https://static.pepy.tech/personalized-badge/dankware?period=week&units=international_system&left_color=black&right_color=brightgreen&left_text=downloads%20/%20week" />
</p>

# 🚨 dankware 🚨
 Python module with various features! Install with the below command!
```
pip install dankware
```

Update to the latest version with the below command!
```
pip install --upgrade dankware
```
 
# 🚨 Multithreading 🚨
```py
from dankware import multithread
import time

a = 0
def example():
    global a
    a += 1
    print(a)
    time.sleep(5)
        
multithread(example, 10) # func: example | threads: 10 | single: 50 seconds | multi: 5 seconds
```
> <img width="500" alt="image" src="https://user-images.githubusercontent.com/52797753/224534374-4693f9fb-2c0c-426b-970d-face9926b9cd.png">

```py
from dankware import multithread
import time

new_list = [1, 2, 3, 4, 5]; sum = 0

def example(num):
    global sum
    sum += num
    time.sleep(5)

multithread(example, 10, new_list) # input_one: list
print(sum)
```
> <img width="500" alt="image" src="https://user-images.githubusercontent.com/52797753/224534424-f03f5884-e9c8-445f-8c0a-5bb227c35aed.png">

```py
from dankware import multithread
import time

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

def example(num1, num2):
    print(num1 + num2)
    time.sleep(5)

multithread(example, 10, list1, list2) # input_one: list1 | input_two: list2
```
> <img width="500" alt="image" src="https://user-images.githubusercontent.com/52797753/224534446-c956dfb0-81a2-4717-bd80-e04484e76507.png">

```py
from dankware import multithread
import time

new_list = [1, 2, 3, 4, 5]

def example(num1, num2):
    print(num1 * num2)
    time.sleep(5)

multithread(example, 10, new_list, 5, progress_bar=False) # input_two: 5 | disabled progress bar
```
> <img width="60" alt="image" src="https://user-images.githubusercontent.com/52797753/153749433-95512c4d-afcd-4ad7-9797-caded6e44239.png">

<p>&nbsp;</p>    

---  

# 🚨 Export Registry Keys 🚨

```py
import os
from dankware import export_registry_keys, is_admin

# [NOTE]: this function requires admin privileges!

export_path = "D:\\export.reg"
registry_root = r'HKEY_CURRENT_USER'
registry_path = r'Software\Google\Chrome\PreferenceMACs'
#export_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'export.reg')

export_registry_keys(registry_root, registry_path, recursive=True, export_path=export_path)
```
> <img width="500" alt="image" src="https://user-images.githubusercontent.com/52797753/221345714-f1cdea4a-0c08-4c47-8c95-c64d95d12dec.png">

> <img width="500" alt="image" src="https://user-images.githubusercontent.com/52797753/221345782-3a5a6ef0-d3b4-48a7-b8f8-c40f210b067d.png">

<p>&nbsp;</p>    

---  

# 🚨 Splash Screen 🚨

```py
from dankware import splash_screen
# Supports: GIFs / PNGs / JPGs / BMPs / ICOs
splash_screen("D:\\splash.gif", duration=5)
# runs on main thread
```

```py
from dankware import splash_screen
from concurrent.futures import ThreadPoolExecutor
ThreadPoolExecutor(1).submit(splash_screen, "splash.png", 5)
# runs on separate thread
```

> <img width="250" alt="image" src="https://user-images.githubusercontent.com/52797753/228445332-004f8f69-d8be-4d36-95e5-9065891e4d09.gif">

# 🚨 Error Traceback 🚨

```py
import sys
from dankware import err, clr
try: value = 1/0
except: print(clr(err(sys.exc_info()),2))
```
> <img width="700" alt="image" src="https://user-images.githubusercontent.com/52797753/221346044-db739b15-b365-47b3-b6f1-20d199c58ab2.png">

<p>&nbsp;</p>    

---  

# 🚨 Scraping 🚨

```py
from dankware import github_downloads
# full url > https://api.github.com/repos/EssentialsX/Essentials/releases/latest
for url in github_downloads("EssentialsX/Essentials"): print(url)
```
> <img width="700" alt="image" src="https://user-images.githubusercontent.com/52797753/216242124-ed911013-bae4-4622-8c0a-0d11638da750.png">

```py
from dankware import github_file_selector
# full url > https://api.github.com/repos/EssentialsX/Essentials/releases/latest
for url in github_file_selector("EssentialsX/Essentials", "remove", ['AntiBuild', 'Discord', 'GeoIP', 'Protect', 'XMPP']): print(url)
```
> <img width="700" alt="image" src="https://user-images.githubusercontent.com/52797753/216241961-5359d662-a117-4eb4-b74e-e82b41a895bc.png">

<p>&nbsp;</p>    

---  

# 🚨 Generate Random IPs 🚨

```py
from dankware import random_ip
print(random_ip())
```

> <img width="200" alt="image" src="https://user-images.githubusercontent.com/52797753/194127781-8f622448-4595-4c2a-a3e7-3e4356076840.png">

<p>&nbsp;</p>    

---  

# 🚨 Colour Special Characters 🚨

```py
from dankware import clr
# default mode = 1
# default colour_one = white
# default colour_two = magenta
print(clr("\n  > Hey! Long time no see :)"))
#print(clr("\n  > Hey! Long time no see :)", colour_one = white, colour_two = magenta))
```
> <img width="350" alt="image" src="https://user-images.githubusercontent.com/52797753/153749617-bb0483fe-0385-490b-8695-72f448300c39.png">

```py
from dankware import clr, white, magenta
# default mode = 1
# default colour_one = white
# default colour_two = magenta
print(clr("\n  > Hey! Long time no see :)", colour_one = magenta, colour_two = white))
```
> <img width="350" alt="image" src="https://user-images.githubusercontent.com/52797753/220981909-d6361e6a-d109-447a-8401-85e2813e7859.png">

```py
from dankware import clr
print(clr("\n  This is a string: True | This is an integer: False"))
```
> <img width="350" alt="image" src="https://user-images.githubusercontent.com/52797753/153749921-3332f3e6-eaa8-4bf1-ab4d-3fe35d245492.png">

```py
from dankware import clr, green, magenta
# dankware now supports adding custom colours on both the text and the function itself!
# colour_two = green
print(clr(f"\n  > {magenta}Purple{white} thinks he's better than everyone else :(", colour_two=green))
```
> <img width="350" alt="image" src="https://user-images.githubusercontent.com/52797753/190898116-750e256e-a1d9-4c8a-a3b2-d0ac209fa0f7.png">

```py
from dankware import clr
# mode = 2
print(clr("\n  > Error in sector [7] redirecting... | INTEGRITY_CHECK_SUCCESS: TRUE",2))
```
> <img width="500" alt="image" src="https://user-images.githubusercontent.com/52797753/153749821-ae3e4dfd-26dc-4e08-a06e-677ac26457a1.png">

```py
from dankware import clr
# mode = 3
print(clr("\n  > Is this a randomly coloured string: TRUE | As you can see it does not colour True/False",3))
```
> <img width="650" alt="image" src="https://user-images.githubusercontent.com/52797753/155293415-7b065b5a-44dd-4fe7-995d-a25582f904cb.png">

<p>&nbsp;</p>    

---  

# 🚨 Banners 🚨

```py
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
```

## ♦️ Colourize Banner (random) ♦️
```py
from dankware import clr
# mode = 4
print(clr(banner,4))
```
> <img width="550" alt="image" src="https://user-images.githubusercontent.com/52797753/153722086-2f372bfa-4872-46a0-81f8-cdf7c2344fd6.png">

## ♦️ Align Banner (console center) ♦️
```py
from dankware import align
print(align(banner)) # also works with single text line (even coloured)
```
> <img width="800" alt="image" src="https://user-images.githubusercontent.com/52797753/153722230-1f3b6103-6d8a-4537-9828-1718a6bd3367.png">

## ♦️ Align Coloured Banner ♦️
```py
from dankware import align, clr
print(clr(align(banner),4)) # OR print(align(clr(banner,4)))
```
> <img width="800" alt="image" src="https://user-images.githubusercontent.com/52797753/153722373-9925dd25-83bb-4d1c-83eb-bfaae1802088.png">

<p>&nbsp;</p>    

---  

# 🚨 Gradient Reworked [ Originally By @venaxyt ] 🚨

```py
from dankware import fade
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
```

## ♦️ Black ♦️
```py
print(fade(banner, "black"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153722811-b257611e-9111-4a0e-92fb-7dbe503ce6db.png">
```py
print(fade(banner, "black-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723205-a91eb1c6-07bc-4bc6-9fa6-52231e50a25c.png">

## ♦️ Red ♦️
```py
print(fade(banner, "red"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153722946-3221bfd8-ff9d-4c9d-8b70-0c2736ec4e30.png">
```py
print(fade(banner, "red-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723473-bdb75ea7-2df2-4f70-adb5-cf5caa57200a.png">

## ♦️ Green ♦️
```py
print(fade(banner, "green"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723050-c30bd3f1-989a-4141-b40a-2869a2dadef6.png">
```py
print(fade(banner, "green-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723481-2e5c21b2-0f12-4d99-ab8d-a3e5c40e4c16.png">

## ♦️ Cyan ♦️
```py
print(fade(banner, "cyan"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723059-b4808365-6006-4726-b427-b6848e0fc0e5.png">
```py
print(fade(banner, "cyan-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723496-8d03c5d3-601e-499d-80cd-51c3648957bf.png">

## ♦️ Blue ♦️
```py
print(fade(banner, "blue"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723092-0a32d8e6-680e-4df3-bdf1-089663f25f45.png">
```py
print(fade(banner, "blue-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723509-41732010-b7d5-4867-95f9-690d47322536.png">

## ♦️ Purple ♦️
```py
print(fade(banner, "purple"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723148-2c94c459-1441-4752-a11f-a547754da7bc.png">
```py
print(fade(banner, "purple-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723519-00aa980e-4a04-4d8d-a319-5691c1f8e517.png">

## ♦️ Pink ♦️
```py
print(fade(banner, "pink-v"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723540-b324dfe1-5ae2-4b66-ad3a-546a589558c8.png">

## ♦️ Random ♦️
```py
print(fade(banner, "random"))
```
> <img width="475" alt="image" src="https://user-images.githubusercontent.com/52797753/153723545-0ea34ea7-1844-4ace-8948-3e71e28c0a30.png">

<p>&nbsp;</p>    

---  

# 🚨 Also check out 🚨
<p align="center">
  <a href="https://github.com/SirDank/dank.tool">
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/52797753/192086704-35f5a0db-3c5d-4782-95a9-6e2756cc8528.png">
  </a>
</p>

<p>&nbsp;</p>    

---  

# 🚨 Stats 🚨

<br><p align="center"><img width="800" alt="image" src="https://repobeats.axiom.co/api/embed/ed44a86c2d46a8719705f5f57efde209b8cb5492.svg"></p><br>

# 🚨 Star History 🚨

<br><p align="center">[![Star History Chart](https://api.star-history.com/svg?repos=SirDank/dankware&type=Date)](https://star-history.com/#SirDank/dankware&Date)</p><br>
