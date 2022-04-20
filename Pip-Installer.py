# py to exe converter
# ====================================================== #

# Libraries
import os
import time
from colorama import Fore , init
import sys
import platform

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


Fore.BLUE

def cls(string:str=""):

    if platform.system() == 'Linux':
        print("")
        print(string)
        time.sleep(3)
        os.system('cls')

    elif platform.system() == 'Windows':
        print("")
        print(string)
        time.sleep(3)
        os.system('cls')

# Logo

os.system('cls')

def logo():
    print(f'''{b}
                 .__            .__                 __         .__  .__   
          ______ |__|_____      |__| ____   _______/  |______  |  | |  |  
          \____ \|  \____ \     |  |/    \ /  ___/\   __\__  \ |  | |  |  
          |  |_> >  |  |_> >    |  |   |  \\___ \   |  |  / __ \|  |_|  |__
          |   __/|__|   __/     |__|___|  /____  > |__| (____  /____/____/
          |__|      |__|                \/     \/            \/           
                            {r}|- Programmed by : TheGreatVex -|
     ''')

def home():

    print(f'''{b}
                 .__            .__                 __         .__  .__   
          ______ |__|_____      |__| ____   _______/  |______  |  | |  |  
          \____ \|  \____ \     |  |/    \ /  ___/\   __\__  \ |  | |  |  
          |  |_> >  |  |_> >    |  |   |  \\___ \   |  |  / __ \|  |_|  |__
          |   __/|__|   __/     |__|___|  /____  > |__| (____  /____/____/
          |__|      |__|                \/     \/            \/           
                            {r}|- Programmed by : TheGreatVex -|    
    
     {r}[{w}1{r}]{b} Library list        {r}[{w}2{r}]{b} Custom Library   
          
            {r}[{w}99{r}]{b} About     {r}[{w}0{r}]{b} exit   
     ''')

    HomeChoices = {
        '0':['exit',sys.exit],
        '1':['library list',libList],
        '2':['custom library',customLib],
        '99':['about',about],
    }

    choice = input(f"{r}[{w}?{r}]{b} Enter choice : ")

    if choice in HomeChoices:
        HomeChoices[choice][1]()

def libList():

    LibraryChoices = {
        '0':['home',home],
        '1':'TensorFlow',
        '2':'Requests',
        '3':'pandas',
        '4':'pygame',
        '5':'numpy',
        '6':'pytorch',
        '7':'keras',
        '8':'pillow',
        '9':'theano',
        '10':'matplotlib',
        '11':'scipy',
        '12':'tkinter',
        '99':['about',about],
    }
    print(f'''
     {r}[{w}1{r}]{b} TensorFlow {r}[{w}5{r}]{b} Numpy   {r}[{w}9{r}]{b}  Theano
     {r}[{w}2{r}]{b} Requests   {r}[{w}6{r}]{b} PyTorch {r}[{w}10{r}]{b} Matplotlib
     {r}[{w}3{r}]{b} Pandas     {r}[{w}7{r}]{b} Keras   {r}[{w}11{r}]{b} SciPy
     {r}[{w}4{r}]{b} Pygame     {r}[{w}8{r}]{b} Pillow  {r}[{w}12{r}]{b} Tkinter
            
     {r}[{w}0{r}]{b} Main Menu  {r}[{w}99{r}]{b} About   {r}[{w}X{r}]{b} Exit 
     ''')


    choice = input(f"{r}[{w}?{r}]{b} Enter choice : ")

    if choice == '0' or choice ==  '99':
        os.system('cls')
        LibraryChoices[choice][1]()

    if choice == 'x':
        os.system('cls')
        sys.exit()

    elif int(choice) in range(1,12):
        print()
        print(f'{r}[{w}+{r}]{b} Started downloading {LibraryChoices[choice]}')
        print()
        os.system(f'pip install {LibraryChoices[choice]}')
        cls(f"{r}[{w}+{r}]{b} Done downloading {LibraryChoices[choice]}")
        home()
    else:
        print()
        print(f'{r}[{w}!{r}]{b} Not a valid choice')
        time.sleep(3)
        os.system('cls')
        logo()
        libList()

def customLib():
    print()
    lib = input(f"{r}[{w}?{r}]{b} what library you want to download : ")
    os.system(f'pip install {lib}')
    cls(f"{r}[{w}+{r}]{b} Done downloading the library")
    home()

def about():

    os.system('cls')
    print(f'''{b}
                 _         _           _        _ _ 
           _ __ (_)_ __   (_)_ __  ___| |_ __ _| | |
          | '_ \| | '_ \  | | '_ \/ __| __/ _` | | |
          | |_) | | |_) | | | | | \__ \ || (_| | | |
          | .__/|_| .__/  |_|_| |_|___/\__\__,_|_|_|
          |_|     |_|     {r}Version : 1.0                             

 {r}[{w}+{r}]{b} Tool Created by V E X (Hussain)                                                         
                                                                                                    
 {r}Author      :  {b}Hussain [V E X]
 {r}Github      :  {b}https://github.com/0VEX
 {r}instagram   :  {b}https://instagram.com/thegreatvex
 {r}Version     :  {b}1.0
     
 {r}[{w}0{r}]{b} Main Menu    {r}[{w}99{r}]{b} Exit
    ''')    
    info = input(f" {r}[{w}?{r}]{b} Enter choice : ")
    if info == '0':
        cls(f" {r}[{w}!{r}]{b} Returning to main menu ...")
        home()

    if info == '99':
        cls(f" {r}[{w}!{r}]{b} Exiting the tool ...")
        time.sleep(3)
        exit()

home()

#=====================================================
