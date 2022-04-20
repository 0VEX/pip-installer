from time import time

import colorama


import os
from colorama import Fore , init

# Colors
init(autoreset=True)
m = Fore.MAGENTA
b = Fore.BLUE 
r = Fore.RED
y = Fore.YELLOW
c = Fore.CYAN
g = Fore.GREEN
w = Fore.WHITE
bl = Fore.BLACK
#---------------------------
lm = Fore.LIGHTMAGENTA_EX
lb = Fore.LIGHTBLUE_EX
lr = Fore.LIGHTRED_EX
ly = Fore.LIGHTYELLOW_EX
lc = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
lw = Fore.LIGHTWHITE_EX
lbl = Fore.LIGHTBLACK_EX

# More

red = "\033[1;31;40m";yel = '\033[1;33;40m'
bloFT = "\033[1;36;40m"
grn = '\033[1;32;40m';wit = "\033[1;37;40m"

# ---------------------------------------------------------------------------------------------------------


os.system('pip install os')
os.system('pip install time')
os.system('pip install colorama')
os.system('pip install sys')
os.system('pip install platform')

os.system('cls')

print(f'''{b}
                 .__            .__                 __         .__  .__   
          ______ |__|_____      |__| ____   _______/  |______  |  | |  |  
          \____ \|  \____ \     |  |/    \ /  ___/\   __\__  \ |  | |  |  
          |  |_> >  |  |_> >    |  |   |  \\___ \   |  |  / __ \|  |_|  |__
          |   __/|__|   __/     |__|___|  /____  > |__| (____  /____/____/
          |__|      |__|                \/     \/            \/           
                            {r}|- Programmed by : TheGreatVex -|
     
     ''')

print(f'{r}[{w}+{r}]{b} Done setting up the tool')
print()
ready = input(f'{r}[{w}!{r}]{b} Press ENTER to exit : ')
