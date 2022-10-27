"""
Imports
"""
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
            word = random.choice(word_list)

    return word.upper()


def game(word):
    """
    Play game.
    """
    word_hint = "_" * len(word)
    guessed_correct = False
    letters_guessed = []
    words_guessed = []
    lives = 6
    print("Time to start guessing!")
    print(word_hint)
    while not guessed_correct and lives > 0:
        print(f"You have {lives} guesses remaining")
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print("You've already guessed that, try again")
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print("You've already guessed that, try again")
        else:
            print("Invalid input. Enter a letter or word.")
