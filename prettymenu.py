import art
from colorama import Fore, Back, Style, init
init(autoreset=True)

string = "fdhfhdhfhfhdhfhdhfhdh"

def get_length(string):
    newstring = str(string)
    length = len(newstring) - newstring.count(' ')
    lenlist = []
    count = length/4
    if length > 50:
        newstring = newstring + '\n'
        return newstring, count

    else:
        return newstring, count

def _menu1():
    print(Fore.RED + Style.BRIGHT + art.menu_top)
    print(Fore.WHITE + Style.BRIGHT + """
    ,------------------------------------------------------.
    | |O  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_| |
    | |----.),------.),------.),------.),------.),------.| |
    | |----' `------' `------' `------' `------' `------'| |
    """)
    print(Fore.WHITE + Style.BRIGHT + '    | |                                                  | |')
    print(Fore.WHITE + Style.BRIGHT + f'    | | {string}                                             | |')
    print(Fore.WHITE + Style.BRIGHT + """    | |                                                  | |
    | |                                                  | |
    | |                                                  | |
    | |  (`-.     (`-.     (`-.     (`-.     (`-.     (`-| |
    | | (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO | |
    | |,------.),------.),------.),------.),------.),----| |
    `-'`------' `------' `------' `------' `------' `----`-'
    """)
    print(count)

def main():
    total = get_length('helldude')
    print(total)



if __name__ == "__main___":
    main()
