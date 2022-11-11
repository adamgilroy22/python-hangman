import pyfiglet
import colorama
from colorama import Fore, Style


def title():
    game_title = pyfiglet.figlet_format("Welcome To\n Hangman",
                                        font="standard", justify="center")
    credits = pyfiglet.figlet_format("By Adam Gilroy",
                                     font="digital", justify="center")
    print(Fore.CYAN + Style.BRIGHT + game_title)
    print(credits)


def hangman(lives):
    """
    Print hangman stages indexing
    list of stages with lives remaining.
    """
    hangman_lives = [f'''{Fore.GREEN}






  =========
9 LIVES REMAIN''', f'''{Fore.GREEN}

        |
        |
        |
        |
        |
  =========
8 LIVES REMAIN''', f'''{Fore.GREEN}
    +---+
        |
        |
        |
        |
        |
  =========
7 LIVES REMAIN''', f'''{Fore.GREEN}
    +---+
    |   |
        |
        |
        |
        |
  =========
6 LIVES REMAIN''', f'''{Fore.GREEN}
    +---+
    |   |
    O   |
        |
        |
        |
  =========
5 LIVES REMAIN''', f'''{Fore.YELLOW}
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
4 LIVES REMAIN''', f'''{Fore.YELLOW}
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
3 LIVES REMAIN''', f'''{Fore.RED}
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =========
2 LIVES REMAIN''', f'''{Fore.RED}
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =========
1 LIFE REMAINS''', f'''{Fore.RED}
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =========
  YOU LOSE''']
    return hangman_lives[-lives-1]
