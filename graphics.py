import pyfiglet
import colorama
from colorama import Fore, Style


def title():
    game_title = pyfiglet.figlet_format("Hangman", font="standard")
    print(Fore.CYAN + Style.BRIGHT + game_title)


def hangman(lives):
    """
    Print hangman stages indexing
    list of stages with lives remaining.
    """
    hangman_lives = ['''






  =========
9 LIVES REMAIN''', '''

        |
        |
        |
        |
        |
  =========
8 LIVES REMAIN''', '''
    +---+
        |
        |
        |
        |
        |
  =========
7 LIVES REMAIN''', '''
    +---+
    |   |
        |
        |
        |
        |
  =========
6 LIVES REMAIN''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
5 LIVES REMAIN''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
4 LIVES REMAIN''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
3 LIVES REMAIN''', '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =========
2 LIVES REMAIN''', '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =========
1 LIFE REMAINS''', '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =========
  YOU LOSE''']
    return hangman_lives[-lives-1]
