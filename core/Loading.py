import art
import os
import time
from progress.bar import Bar
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Loading script (To import)
def bunnyloader(n):
	loop = 0
	while (loop != int(n)):
		os.system('clear')
		print('Loading.')
		print(art.ani1)
		time.sleep(0.25)
		os.system('clear')
		print('Loading..')
		print(art.ani2)
		time.sleep(0.25)
		os.system('clear')
		print('Loading...')
		print(art.ani3)
		time.sleep(0.25)
		os.system('clear')
		print('Loading....')
		print(art.ani4)
		time.sleep(0.25)
		os.system('clear')
		loop = loop + 1

def backslash_symbol(n):
	loop = 0
	while (loop != int(n)):
		print(Fore.RED + Style.BRIGHT + art.ani5)
		time.sleep(0.5)
		os.system('clear')
		print(Fore.BLUE + Style.BRIGHT + art.ani5)
		time.sleep(0.5)
		os.system('clear')
		print(Fore.WHITE + Style.BRIGHT + art.ani5)
		time.sleep(0.5)
		os.system('clear')
		loop = loop + 1
	return Fore.WHITE + Style.BRIGHT + art.ani5
