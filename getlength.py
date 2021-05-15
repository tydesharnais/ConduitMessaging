from colorama import Fore, Back, Style, init
import art
init(autoreset=True)



def _menu1(string):
    lenlist = []
    newstring = str(string)
    length = len(newstring) - newstring.count(' ')
    if length > 50:
        counted = length/4
        int_count = int(counted)
        split = '\n'
        for i in range(int_count):
            newstring[:50] + split + newstring[50:]


    print(Fore.RED + Style.BRIGHT + art.menu_top)
    print(Fore.WHITE + Style.BRIGHT + """
    ,------------------------------------------------------.
    | |O  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_| |
    | |----.),------.),------.),------.),------.),------.| |
    | |----' `------' `------' `------' `------' `------'| |
    """)
    print(Fore.WHITE + Style.BRIGHT + '    | |                                                  | |')
    print(Fore.WHITE + Style.BRIGHT + f'    | | {newstring}                                             | |')
    print(Fore.WHITE + Style.BRIGHT + """    | |                                                  | |
    | |                                                  | |
    | |                                                  | |
    | |  (`-.     (`-.     (`-.     (`-.     (`-.     (`-| |
    | | (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO  )_  (OO | |
    | |,------.),------.),------.),------.),------.),----| |
    `-'`------' `------' `------' `------' `------' `----`-'
    """)



total = _menu1('helloalffffffkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkvkdkdkdkdkdkdkdkdkdfdl')

print(total)
