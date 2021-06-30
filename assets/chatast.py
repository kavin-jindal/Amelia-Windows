import os
from rsap import AsyncRSAP
from rsap import RSAP
import requests
from colorama import *
from start import start
init()


def bot_reply():
    
    bot = RSAP("BTPF7gRedtMu", bot_name = 'Amelia', dev_name = 'Kavin Jindal', language = 'en')
    user_text = input('[.] Type your message >> ')
    if 'exit' in user_text:
        start()
    else:
        astro_text = bot.ai_response(user_text)
        print(Fore.GREEN + f'\n[.] {astro_text}')
        bot_reply()
def chatbot():
    
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
    print(Fore.YELLOW + '\n\n\t [=]' +  Fore.CYAN + ' ChatBot Powered by Random-Stuff-API ')
    print('   ')


