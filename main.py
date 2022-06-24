import requests, os

from colorama import Fore, Back, Style, init
init(autoreset=True)

from time import sleep
    
def requests_send():
    while True:
        r = requests.get(url)
        print(Fore.LIGHTBLUE_EX + "> " + Fore.GREEN + "Requests Send !")
        sleep(30)

url = input("Enter relpit url -> ")
print("\n")
requests_send()