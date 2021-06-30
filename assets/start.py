import pyttsx3
import pyfiglet
from colorama import * 
import os
import sys

def start():
    os.system('cls')
    print(Fore.CYAN + """
      ___           ___           ___           ___                   ___
     /\  \         /\__\         /\  \         /\__\      ___        /\  \  
    /::\  \       /::|  |       /::\  \       /:/  /     /\  \      /::\  \ 
   /:/\:\  \     /:|:|  |      /:/\:\  \     /:/  /      \:\  \    /:/\:\  \ 
  /::\~\:\  \   /:/|:|__|__   /::\~\:\  \   /:/  /       /::\__\  /::\~\:\  \ 
 /:/\:\ \:\__\ /:/ |::::\__\ /:/\:\ \:\__\ /:/__/     __/:/\/__/ /:/\:\ \:\__\ 
 \/__\:\/:/  / \/__/~~/:/  / \:\~\:\ \/__/ \:\  \    /\/:/  /    \/__\:\/:/  /
      \::/  /        /:/  /   \:\ \:\__\    \:\  \   \::/__/          \::/  /
      /:/  /        /:/  /     \:\ \/__/     \:\  \   \:\__\          /:/  /
     /:/  /        /:/  /       \:\__\        \:\__\   \/__/         /:/  /
     \/__/         \/__/         \/__/         \/__/                 \/__/

""")
    print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Amelia v 1.0.0 ')
    print(Fore.RED + '\n\t [=]' +  Fore.GREEN + ' Early Access Version ')
    print(Fore.RED + '\n\n\n\t [+]' +  Fore.RED + ' Write Exit to exit ')
    print(Fore.RED + '\n\n\n\t [+]' +  Fore.RED + ' Write Chat to use the chatbot ')

    ust = input(">>")
    if "exit" in ust:
        os.system('cls')
        sys.exit()
    else:
        input('Press enter again')
    