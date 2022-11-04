import pyfiglet
import colorama
from colorama import Fore, Style


def title():
    game_title = pyfiglet.figlet_format("Hangman", font="big")
    print(Fore.CYAN + Style.BRIGHT + game_title)


def hangman(lives):
    """
    Print hangman stages indexing
    list of stages with lives remaining.
    """
    hangman_lives = ['''






=========''', '''

      |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return hangman_lives[-lives-1]
