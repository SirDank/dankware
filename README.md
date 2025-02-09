
<p align="center">
  <b>~ Visits ~</b><br><br>
  <img src="https://profile-counter.glitch.me/dankware/count.svg" />
</p>

<p align="center">
  <b>~ Stats ~</b><br><br>
  <img src="https://static.pepy.tech/badge/dankware" />
  <img src="https://static.pepy.tech/badge/dankware/month" />
  <img src="https://static.pepy.tech/badge/dankware/week" />
</p>

# 🚨 dankware 🚨

 Python module with various features! Install with the below command!

```bash
pip install dankware
```

```bash
pip install dankware[extras]
```

Update to the latest version with the below command!

```bash
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

<img width="500" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/25fd06a6-ac4d-4f40-8b8a-24a7f0700623"><br>

```py
from dankware import multithread
import time

new_list = [1, 2, 3, 4, 5]
sum = 0

def example(num):
    global sum
    sum += num
    time.sleep(5)

multithread(example, 10, new_list) # input_one: list
print(sum)
```

<img width="500" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/dbc2bd0a-192e-4311-8058-06ab68d01607"><br>

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

<img width="500" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/0b3e2d17-c1eb-4982-a6a8-be5bf643946b"><br>

```py
from dankware import multithread
import time

new_list = [1, 2, 3, 4, 5]

def example(num1, num2):
    print(num1 * num2)
    time.sleep(5)

multithread(example, 10, new_list, 5, progress_bar=False) # input_two: 5 | disabled progress bar
```

<img width="60" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/153749433-95512c4d-afcd-4ad7-9797-caded6e44239.png"><br>

<p>&nbsp;</p>

---  

# 🚨 Export Registry Keys 🚨

```py
import os
from dankware import export_registry_keys

# [NOTE]: this function requires admin privileges!

export_path = "D:\\export.reg"
registry_root = r'HKEY_CURRENT_USER'
registry_path = r'Software\Google\Chrome\PreferenceMACs'
#export_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'export.reg')

export_registry_keys(registry_root, registry_path, recursive=True, export_path=export_path)
```

<img width="500" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/221345714-f1cdea4a-0c08-4c47-8c95-c64d95d12dec.png">
<img width="500" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/221345782-3a5a6ef0-d3b4-48a7-b8f8-c40f210b067d.png"><br>

<p>&nbsp;</p>

---  

# 🚨 Splash Screen 🚨

```py
from dankware.pillow import splash_screen
#from dankware import hide_window, show_window

# Supports: GIFs / PNGs / JPGs / BMPs / ICOs

# hide_window()
splash_screen("D:\\splash.gif", duration=5) # runs on main thread
# show_window()
```

```py
from dankware.pillow import splash_screen
from concurrent.futures import ThreadPoolExecutor
ThreadPoolExecutor(1).submit(splash_screen, "splash.png", 5)
# runs on separate thread
```

<img width="250" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/228445332-004f8f69-d8be-4d36-95e5-9065891e4d09.gif"><br>

# 🚨 Error Traceback 🚨

```py
import sys
from dankware import err, clr
try: value = 1/0
except Exception as exc:
  print(clr(err((type(exc), exc, exc.__traceback__)),2))
  # OR
  print(clr(err(sys.exc_info()),2))
# OR
try: value = 1/0
except Exception as exc:
  print(clr(err((type(exc), exc, exc.__traceback__),'mini'),2))
  # OR
  print(clr(err(sys.exc_info(),"mini"),2))
```

<img width="700" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/e2a22bab-05c7-4d10-abbe-9fcd6d3ecf4e"><br>
<img width="700" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/15a930c9-2633-42a9-a3eb-bbe0956624b0"><br>

<p>&nbsp;</p>

---  

# 🚨 Scraping 🚨

```py
from dankware import github_downloads
# full url > https://api.github.com/repos/EssentialsX/Essentials/releases/latest
for url in github_downloads("EssentialsX/Essentials"): print(url)
```

<img width="700" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/216242124-ed911013-bae4-4622-8c0a-0d11638da750.png"><br>

```py
from dankware import github_file_selector
# full url > https://api.github.com/repos/EssentialsX/Essentials/releases/latest
for url in github_file_selector("EssentialsX/Essentials", "remove", ('AntiBuild', 'Discord', 'GeoIP', 'Protect', 'XMPP')): print(url)
```

<img width="700" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/216241961-5359d662-a117-4eb4-b74e-e82b41a895bc.png"><br>

<p>&nbsp;</p>

---  

# 🚨 Generate Random IPs 🚨

```py
from dankware import random_ip
print(random_ip())
```

<img width="200" alt="image" style="border-radius:5%" src="https://user-images.githubusercontent.com/52797753/194127781-8f622448-4595-4c2a-a3e7-3e4356076840.png"><br>

<p>&nbsp;</p>

---  

# 🚨 GUI File / Path Selector 🚨

```py
from dankware.tkinter import file_selector
path = file_selector() # opens file explorer to select a file
print(path)
```

```py
from dankware.tkinter import folder_selector
path = folder_selector() # opens file explorer to select a folder
print(path)
```

# 🚨 Path Extractor 🚨

```py
import os
from dankware import get_path

if os.name == 'nt': # extracts path from registry
    locations = ("AppData", "Desktop", "Documents", "Favorites", "Local AppData", "Pictures", "Videos", "Music", "Downloads", "Temp")
elif os.name == 'posix':
    locations = ("Desktop", "Documents", "Downloads", "Music", "Pictures", "Videos", "Temp")
for location in locations:
    path = get_path(location)
    print(path)
```

<img width="200" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/ee06bdd9-fbd3-4765-9450-6e2435dd6880"><br>

<p>&nbsp;</p>

---  

# 🚨 Colour Special Characters 🚨

```py
from dankware import clr
# default preset = 1
# default colour_one = white_bright
# default colour_two = red_bright
print(clr("\n  > Hey! Long time no see :)"))
#print(clr("\n  > Hey! Long time no see :)", colour_one = white_bright, colour_two = red_bright))
```

<img width="350" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/f8cd517e-c3df-4038-a1b1-df16f9d6ab8c"><br>

```py
from dankware import clr, white, magenta
# default preset = 1
# colour_one = magenta
# colour_two = white
print(clr("\n  > Hey! Long time no see :)", colour_one = magenta, colour_two = white))
```

<img width="350" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/40dec334-39b7-4fcb-90c8-b6b824c372cb"><br>

```py
from dankware import clr
print(clr("\n  This is a string: True | This is an integer: False"))
```

<img width="350" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/5bab7947-ffd1-49a9-b10b-dce31acf65fb"><br>

```py
from dankware import clr, green, magenta, white
# default colour_one = white_bright
# colour_two = green
print(clr(f"\n  > {magenta}Purple{white} thinks he's better than everyone else :(", colour_two=green))
```

<img width="350" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/e43774dd-b76e-43af-832b-0305e282e565"><br>

```py
from dankware import clr
# preset = 2
print(clr("\n  > Error in sector [7] redirecting... | INTEGRITY_CHECK: SUCCESS",2))
```

<img width="500" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/c69d3eeb-b4a0-45df-ab86-def37ac0f179"><br>

```py
from dankware import clr
# preset = 3
print(clr("\n  > Is this a randomly coloured string: TRUE | As you can see it does not colour True/False",3))
```

<img width="650" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/f89c5126-c7a0-4060-ab01-8783f95224f4"><br>

```py
from dankware import clr, white, white_normal, white_dim, red, red_normal, red_dim
# preset = 3
print(clr("\n  > This is a randomly coloured string based on the input colours!",3,colours=(white_bright, white_normal, white_dim, red_bright, red_normal, red_dim)))
```

<img width="650" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/bf27ee3e-a72b-4e52-85e5-85fa4df8fba6"><br>

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
# preset = 4
print(clr(banner,4))
```

<img width="550" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/c34c6f9d-de2a-4a91-bb46-b262248caab4"><br>

## ♦️ Align Banner (console center) ♦️

```py
from dankware import align
print(align(banner)) # also works with single text line (even coloured)
```

<img width="800" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/678296e6-3668-4d54-bbb1-273547f7f654"><br>

## ♦️ Align Coloured Banner ♦️

```py
from dankware import align, clr
print(clr(align(banner),4)) # OR (preferably not) print(align(clr(banner,4)))
```

<img width="800" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/a90e4bc3-1c08-48e4-801a-2403c6b08d16"><br>

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

## ♦️ Black To White ♦️

```py
print(fade(banner, "black2white"))
print(fade(banner, "black2white-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/9cd7e49c-fb2a-4973-87a9-6bfae1967db3" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/ed997994-8cce-47dd-bd8e-9db8293606ea" />
</p>

## ♦️ Yellow To Red ♦️

```py
print(fade(banner, "yellow2red"))
print(fade(banner, "yellow2red-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/c92aed4e-a883-44c8-a9cc-c7916fae9b18" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/c9f07d49-3d7b-4213-addd-51d5af46fa87" />
</p>

## ♦️ Green To Yellow ♦️

```py
print(fade(banner, "green2yellow"))
print(fade(banner, "green2yellow-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/4d6e9eed-7f51-46fe-9188-48adcb20d7c9" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/8c6c1c6a-fbcc-4170-a527-1b8856d1d1c1" />
</p>

## ♦️ Green To Cyan ♦️

```py
print(fade(banner, "green2cyan"))
print(fade(banner, "green2cyan-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/5565e166-767a-4cb6-ba5a-a090b0348bc7" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/92252aaa-ad8f-42d9-93da-7e2926f69408" />
</p>

## ♦️ Blue To Cyan ♦️

```py
print(fade(banner, "blue2cyan"))
print(fade(banner, "blue2cyan-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/49a6b5ee-1d23-44bb-908f-9515ff2877ca" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/6011a3ae-0922-4b4c-9ca8-33384293188c" />
</p>

## ♦️ Blue To Pink ♦️

```py
print(fade(banner, "blue2pink"))
print(fade(banner, "blue2pink-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/ce5e798a-f6b9-408f-800c-980b8079caba" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/2f4fa5d0-121b-46a0-992f-457c7e404ecc" />
</p>

## ♦️ Pink To Red ♦️

```py
print(fade(banner, "pink2red"))
print(fade(banner, "pink2red-v"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/7063ec77-16a9-42f0-9f46-3bc9284e4397" />
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/46ff4976-8c2a-491b-b4a5-979aab2f7a6a" />
</p>

## ♦️ Random ♦️

```py
print(fade(banner, "random"))
```

<p align="left">
  <img width="400" alt="image" style="border-radius:5%" src="https://github.com/SirDank/dankware/assets/52797753/58a13389-7620-4c63-b967-c057b022af90" />
</p>

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

# 🚨 Wallpapers 🚨

## ♦️ Style 1 ♦️

<br><p align="center"><img width="700" alt="image" src="__wallpapers__/1.png"></p><br>

## ♦️ Style 2 ♦️

<br><p align="center"><img width="700" alt="image" src="__wallpapers__/2.png"></p><br>

## ♦️ Style 3 ♦️

<br><p align="center"><img width="700" alt="image" src="__wallpapers__/3.png"></p><br>

## ♦️ Style 4 ♦️

<br><p align="center"><img width="700" alt="image" src="__wallpapers__/4.png"></p><br>

<p>&nbsp;</p>

---  

# 🚨 Stats 🚨

<br><p align="center"><img width="800" alt="image" src="https://repobeats.axiom.co/api/embed/ed44a86c2d46a8719705f5f57efde209b8cb5492.svg"></p><br>

# 🚨 Star History 🚨

<p align="center">
<a href="https://star-history.com/#SirDank/dankware&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SirDank/dankware&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SirDank/dankware&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SirDank/dankware&type=Date" />
  </picture>
</a>
</p>
