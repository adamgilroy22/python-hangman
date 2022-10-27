# imports
import random


def game_menu():
    """
    Menu to begin game, change difficulty and view rules
    """
    print("Press 1 To Start Game")
    print("Press 2 To Select Difficulty")
    print("Press 3 To View Rules")

    menu_selection = False
    while not menu_selection:
        selection = input("What would you like to do?\n")
        if selection == 1:
            menu_selection = True

        elif selection == 2:
            menu_selection = True

        elif selection == 3:
            menu_selection = True

        else:
            print("Select 1, 2 or 3")


def random_word():
    """
    Select random word from words.txt to be used
    in game. Word must be at least 3 characters.
    """
    word = ""
    while len(word) < 3:
        with open("words.txt", "r") as file:
            all_words = file.read()
            word_list = list(map(str, all_words.split('\n')))
            word = random.choice(word_list).upper

    return word


random_word()
