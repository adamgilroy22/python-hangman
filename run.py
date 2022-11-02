"""
Imports
"""
import random
from graphics import title
from graphics import hangman


def game_menu():
    """
    Menu to begin game, select difficulty and view rules
    """
    print("Press 1 to play game")
    print("Press 2 to view rules")
    menu_selection = False
    while not menu_selection:
        selection = input("What would you like to do?\n")
        selection = int(selection)
        if selection == 1:
            menu_selection = True
        elif selection == 2:
            menu_selection = True
            game_rules()
        else:
            print("Please select 1 or 2")


def game_difficulty():
    """
    Let user select easy, normal or hard difficulty
    """
    print("Select difficulty")
    print("1. Easy - 9 lives")
    print("2. Normal - 7 lives")
    print("3. Hard - 5 lives")

    difficulty_selection = False
    while not difficulty_selection:
        difficulty = input("What would you like to do?\n")
        difficulty = int(difficulty)
        if difficulty == 1:
            difficulty_selection = True
            num_lives = 9
            return num_lives
        elif difficulty == 2:
            difficulty_selection = True
            num_lives = 7
            return num_lives
        elif difficulty == 3:
            difficulty_selection = True
            num_lives = 5
            return num_lives
        else:
            print("Please select 1, 2 or 3")


def game_rules():
    """
    Shows user game rules and how to play
    """
    print(
        """
        Try to save the hangman by guessing the word.
        Guess either single letters or full words.
        If you guess wrong, you will lose a life
        and the hangman will get closer to his demise.
        Get the word in 9 guesses (6 in hard mode)
        and the hangman will be spared.
        Can you save the hangman?
        """
    )
    input("Press enter to return to main menu")
    main()


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


def game(word, num_lives):
    """
    Play game.
    Check if user guess is a letter or word.
    Check if guess is in word or is the word.
    Lose life if not.
    Display win/lose message.
    """
    word_hint = "_" * len(word)
    guessed_correct = False
    letters_guessed = []
    words_guessed = []
    lives = num_lives
    print("Time to start guessing!")
    while not guessed_correct and lives > 0:
        print(hangman(lives))
        print(word_hint)
        print(f"You have {lives} guesses remaining.")
        print(f"The word has {len(word)} letters.")
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print(f"You've already guessed {guess}, try again.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                lives -= 1
                letters_guessed.append(guess)
            else:
                print(f"Great, {guess} is in the word!")
                letters_guessed.append(guess)
                word_split = list(word_hint)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_split[index] = guess
                word_hint = "".join(word_split)
                if "_" not in word_hint:
                    guessed_correct = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print(f"You've already guessed {guess}, try again.")
            elif guess != word:
                print(f"{guess} is not the word.")
                lives -= 1
                words_guessed.append(guess)
                print(f"Full words guessed: {words_guessed}")
            else:
                guessed_correct = True
        else:
            print("Invalid input. Enter a letter or word.")
    if guessed_correct:
        print(f"Congratulations! The word was {word}.")
    else:
        print(hangman(lives))
        print(f"Out of guesses, the word was {word}.")


def main():
    """
    Run game.
    """
    title()
    game_menu()
    lives = game_difficulty()
    word = random_word()
    game(word, lives)


main()
