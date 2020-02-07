"""
   created at feb 06/20 by tir.farzad@gmail.com
   this package present the color class

"""
from colorama import (
    Fore, Back, init as colorama_init
)


class Color:
    colorama_init(autoreset=True)

    FORE_GREEN = Fore.GREEN
    FORE_RED = Fore.RED
    FORE_YELLOW = Fore.YELLOW
    FORE_CYAN = Fore.CYAN
    FORE_BLUE = Fore.BLUE
    FORE_WHITE = Fore.WHITE

    BACK_GREEN = Back.GREEN
    BACK_RED = Back.RED
    BACK_YELLOW = Back.YELLOW
    BACK_CYAN = Back.CYAN
    BACK_BLUE = Back.BLUE

