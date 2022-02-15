# dankware
 Python module with various features! Install with the below command!
```
pip install dankware
```
 
## Multithreading
```py
from dankware.threading import multithread
import time

a = 0
def example():
    global a
    a += 1
    print(a)
    time.sleep(5)
        
multithread(example, 10)
```
> <img width="404" alt="image" src="https://user-images.githubusercontent.com/52797753/153721721-0541e26b-f0b2-4c87-8c61-778a817cf80e.png">

```py
from dankware.threading import multithread
import time

list = [1, 2, 3, 4, 5];sum = 0

def example(num):
    global sum;sum += num;time.sleep(5)

multithread(example, 10, list)
print(sum)
```
> <img width="397" alt="image" src="https://user-images.githubusercontent.com/52797753/153748543-07260a2e-5e25-4926-b11f-9d3670d2f3ef.png">

```py
from dankware.threading import multithread
import time

list1 = [1, 2, 3, 4, 5];list2 = [5, 4, 3, 2, 1]

def example(num1, num2):
    print(num1 + num2);time.sleep(5)

multithread(example, 10, list1, list2)
```
> <img width="392" alt="image" src="https://user-images.githubusercontent.com/52797753/153749164-d8224ad4-3116-4376-90cd-bc1d093e0942.png">

```py
from dankware.threading import multithread
import time

list = [1, 2, 3, 4, 5]

def example(num1, num2):
    print(num1 * num2);time.sleep(5)

multithread(example, 10, list, 5, progress_bar=False)
```
> <img width="25" alt="image" src="https://user-images.githubusercontent.com/52797753/153749433-95512c4d-afcd-4ad7-9797-caded6e44239.png">

<p>&nbsp;</p>    

---  

# Colour Specific Chars

```py
from dankware.colours import clr
print(clr("\n  > Hey! Long time no see :)"))
```
> <img width="159" alt="image" src="https://user-images.githubusercontent.com/52797753/153749617-bb0483fe-0385-490b-8695-72f448300c39.png">

```py
from dankware.colours import clr
print(clr("\n  This is a string: True | This is an integer: False"))
```
> <img width="286" alt="image" src="https://user-images.githubusercontent.com/52797753/153749921-3332f3e6-eaa8-4bf1-ab4d-3fe35d245492.png">

```py
from dankware.colours import clr
print(clr("\n  > Error in sector [7] redirecting... | INTEGRITY_CHECK_SUCCESS: TRUE",2))
```
> <img width="389" alt="image" src="https://user-images.githubusercontent.com/52797753/153749821-ae3e4dfd-26dc-4e08-a06e-677ac26457a1.png">

<p>&nbsp;</p>    

---  

# Banners

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

## Colourize Banner (random)
```py
from dankware.colours import clr_banner
print(clr_banner(banner))
```
> <img width="429" alt="image" src="https://user-images.githubusercontent.com/52797753/153722086-2f372bfa-4872-46a0-81f8-cdf7c2344fd6.png">

## Align Banner (console center)
```py
from dankware.colours import align_banner
print(align_banner(banner))
```
> <img width="617" alt="image" src="https://user-images.githubusercontent.com/52797753/153722230-1f3b6103-6d8a-4537-9828-1718a6bd3367.png">

## Align Coloured Banner
```py
from dankware.colours import align_banner, clr_banner
print(align_banner(banner, clr_banner(banner)))
```
> <img width="638" alt="image" src="https://user-images.githubusercontent.com/52797753/153722373-9925dd25-83bb-4d1c-83eb-bfaae1802088.png">

<p>&nbsp;</p>    

---  

# Gradient Reworked [ Originally By @venaxyt ]

```py
from dankware.colours import fade
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

## Black
```py
print(fade(banner, "black"))
```
> <img width="370" alt="image" src="https://user-images.githubusercontent.com/52797753/153722811-b257611e-9111-4a0e-92fb-7dbe503ce6db.png">
```py
print(fade(banner, "black-v"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723205-a91eb1c6-07bc-4bc6-9fa6-52231e50a25c.png">

## Red
```py
print(fade(banner, "red"))
```
> <img width="372" alt="image" src="https://user-images.githubusercontent.com/52797753/153722946-3221bfd8-ff9d-4c9d-8b70-0c2736ec4e30.png">
```py
print(fade(banner, "red-v"))
```
> <img width="367" alt="image" src="https://user-images.githubusercontent.com/52797753/153723473-bdb75ea7-2df2-4f70-adb5-cf5caa57200a.png">

## Green
```py
print(fade(banner, "green"))
```
> <img width="369" alt="image" src="https://user-images.githubusercontent.com/52797753/153723050-c30bd3f1-989a-4141-b40a-2869a2dadef6.png">
```py
print(fade(banner, "green-v"))
```
> <img width="367" alt="image" src="https://user-images.githubusercontent.com/52797753/153723481-2e5c21b2-0f12-4d99-ab8d-a3e5c40e4c16.png">

## Cyan
```py
from dankware.colours import fade
print(fade(banner, "cyan"))
```
> <img width="369" alt="image" src="https://user-images.githubusercontent.com/52797753/153723059-b4808365-6006-4726-b427-b6848e0fc0e5.png">
```py
print(fade(banner, "cyan-v"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723496-8d03c5d3-601e-499d-80cd-51c3648957bf.png">

## Blue
```py
print(fade(banner, "blue"))
```
> <img width="360" alt="image" src="https://user-images.githubusercontent.com/52797753/153723092-0a32d8e6-680e-4df3-bdf1-089663f25f45.png">
```py
print(fade(banner, "blue-v"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723509-41732010-b7d5-4867-95f9-690d47322536.png">

## Purple
```py
print(fade(banner, "purple"))
```
> <img width="367" alt="image" src="https://user-images.githubusercontent.com/52797753/153723148-2c94c459-1441-4752-a11f-a547754da7bc.png">
```py
print(fade(banner, "purple-v"))
```
> <img width="357" alt="image" src="https://user-images.githubusercontent.com/52797753/153723519-00aa980e-4a04-4d8d-a319-5691c1f8e517.png">

## Pink
```py
print(fade(banner, "pink-v"))
```
> <img width="363" alt="image" src="https://user-images.githubusercontent.com/52797753/153723540-b324dfe1-5ae2-4b66-ad3a-546a589558c8.png">

## Random
```py
print(fade(banner, "random"))
```
> <img width="362" alt="image" src="https://user-images.githubusercontent.com/52797753/153723545-0ea34ea7-1844-4ace-8948-3e71e28c0a30.png">

<p>&nbsp;</p>    

---  
