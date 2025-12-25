import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored_tree():
    GREEN = "\033[32m"
    BROWN = "\033[33m"  
    RESET = "\033[0m"

    foliage = [
        "      +       ",
        "    +   +     ",
        "  +       +   ",
        " +         +  ",
        "+           + ",
        "+++++   +++++"
    ]
    
    trunk = [
        "    +   +     ",
        "    +   +     ",
        "    +   +     "
    ]
    for line in foliage:
        print(GREEN + line + RESET)
    
    for line in trunk:
        print(BROWN + line + RESET)

clear_console()
print_colored_tree()