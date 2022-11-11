"""
Imports
"""
import random
import os
import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Style
from graphics import title, hangman

colorama.init(autoreset=True)  # Set so colours auto-reset after being printed

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

leaderboard = SHEET.worksheet('leaderboard')
leaderboard_scores = leaderboard.get_all_values()


def update_leaderboard(player):
    """
    Adds user data to leaderboard and notifies
    the player if they are in the top 10 scores
    Sorts leaderboard sheet by scores descending from
    highest to lowest.
    """
    for count, score in enumerate(leaderboard_scores[1:11], 2):
        if player.score > int(score[2]):
            print(f"{Fore.GREEN}Well done {player.name}, you made the top 10!")
            player_as_list = [player.name, player.place, player.score]
            leaderboard.append_row(player_as_list)
            leaderboard.sort((3, 'des'), range='A2:C999')
            leaderboard.delete_rows(12)
            break
    else:
        print(f"{Fore.RED}Unlucky {player.name}, You didn't make the top 10 "
              "this time!")


def display_leaderboard():
    """
    Print current leaderboard
    """
    clear_screen()
    print(f"{Fore.YELLOW}TOP 10 LEADERBOARD")
    col_len = {i: max(map(len, inner))
               for i, inner in enumerate(zip(*leaderboard_scores))}

    for inner in leaderboard_scores:
        for col, word in enumerate(inner):
            print(f"{word:{col_len[col]}}", end=" | ")
        print()
    print()
    input("Press enter to return to main menu\n")
    clear_screen()


class Player:
    """
    Player class used to create player object
    containing name, location, number of lives and current score
    """
    def __init__(self, name, place, lives, score):
        self.name = name
        self.place = place
        self.lives = 7
        self.score = 0


def clear_screen():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def player_details():
    """
    Prompt player to enter their name and location
    and sets starting score to 0.
    """
    title()
    while True:
        player_name = input("What is your name?\n").upper()
        if player_name.isalpha():
            location = False
            while not location:
                player_place = input("Where are you from?\n").upper()
                if player_place.isalpha():
                    player = Player(name=player_name, place=player_place,
                                    lives=7, score=0)
                    return player
                else:
                    clear_screen()
                    print(f"{Fore.RED}{player_place} is not valid")
        else:
            clear_screen()
            print(f"{Fore.RED}{player_name} is not valid")


def game_menu(player):
    """
    Menu to begin game, view rules or check leaderboard
    """
    while True:
        print(f"Hello, {Fore.CYAN}{Style.BRIGHT}{player.name}")
        print("What would you like to do?")
        print("Press 1 to play game")
        print("Press 2 to view rules")
        print("Press 3 to view leaderboard")
        print("Press 4 to quit game")
        selection = input()
        if selection == "1":
            break
        elif selection == "2":
            game_rules()
        elif selection == "3":
            display_leaderboard()
        elif selection == "4":
            print(f"Goodbye {player.name}!")
            quit()
        else:
            clear_screen()
            print(f"{Fore.RED}{selection} is not valid.")


def game_difficulty():
    """
    Let user select easy, normal or hard difficulty
    """
    while True:
        print("Select difficulty")
        print(f"{Fore.GREEN}1. Easy - 9 lives")
        print(f"{Fore.YELLOW}2. Normal - 7 lives")
        print(f"{Fore.RED}3. Hard - 5 lives")
        difficulty = input()
        if difficulty == "1":
            return difficulty
        elif difficulty == "2":
            return difficulty
        elif difficulty == "3":
            return difficulty
        else:
            clear_screen()
            print(f"{Fore.RED}{difficulty} is not valid.")


def game_rules():
    """
    Shows user game rules and how to play
    """
    clear_screen()
    print(
        f"""
   {Fore.YELLOW}+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    Try to save the hangman by guessing the word.
    Guess either single letters or full words.
    If you guess wrong, you will lose a life
    and the hangman will get closer to his demise.
    Get the word before your lives are up
    and the hangman will be spared.

    Score points every time you win and try to
    earn a spot on the leaderboard. Easy, normal,
    and hard modes earn you 1, 2 and 3 points
    respectively and an extra point is awarded for
    long words. If you lose a game, you will also
    lose a point.

    Can you save the hangman and make the top 10?
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        """
    )
    input("Press enter to return to main menu\n")
    clear_screen()


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


def game(word, difficulty, player):
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
    if difficulty == "1":
        player.lives = 9
    elif difficulty == "2":
        player.lives = 7
    elif difficulty == "3":
        player.lives = 5
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}Time to start guessing!")
    if player.score > 0:
        print(f"Your score is: {player.score}")
    while not guessed_correct and player.lives > 0:
        print(hangman(player.lives))
        for space in word_hint:
            print(space, end=" ")
        print("")
        print(f"The word has {len(word)} letters.")
        print("Letters guessed: " + ', '.join(letters_guessed))
        guess = input("Guess a letter or word:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                clear_screen()
                print(f"{Fore.YELLOW}You've already guessed {guess}, "
                      "try again.")
            elif guess not in word:
                clear_screen()
                print(f"{Fore.RED}{guess} is not in the word.")
                player.lives -= 1
                letters_guessed.append(guess)
            else:
                clear_screen()
                print(f"{Fore.GREEN}Great, {guess} is in the word!")
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
                clear_screen()
                print(f"{Fore.YELLOW}You've already guessed {guess},"
                      "try again.")
            elif guess != word:
                clear_screen()
                print(f"{Fore.RED}{guess} is not the word.")
                player.lives -= 1
                words_guessed.append(guess)
            else:
                guessed_correct = True
        elif len(guess) > 1 and len(guess) != len(word) and guess.isalpha():
            clear_screen()
            print(f"{Fore.YELLOW}{guess} is {len(guess)} letters long.")
            print(f"{Fore.YELLOW}The word is {len(word)} letters long, "
                  "try again.")
        else:
            clear_screen()
            print(f"{Fore.RED}{guess} is not a valid input.")
            print(f"{Fore.RED}Enter a letter or word.")
    if guessed_correct:
        clear_screen()
        print(hangman(player.lives))
        if difficulty == "1":
            player.score += 1
        elif difficulty == "2":
            player.score += 2
        elif difficulty == "3":
            player.score += 3
        if len(word) > 6:
            player.score += 1
        print(f"{Fore.GREEN}Congratulations! The word was {word}.")
    else:
        clear_screen()
        print(hangman(player.lives))
        if player.score < 1:
            print(f"{Fore.RED}Unlucky, the word was {word}.")
        else:
            player.score -= 1
            print(f"{Fore.RED}Unlucky, the word was {word}.")


def main():
    """
    Run game.
    Give user the option to restart the game once complete.
    """
    player = player_details()
    game_menu(player)
    while True:
        difficulty = game_difficulty()
        word = random_word()
        game(word, difficulty, player)
        reset_game = False
        while not reset_game:
            restart = input("Play again? (Y/N)\n")
            if restart.upper() == "Y":
                clear_screen()
                print("Starting again")
                reset_game = True
            elif restart.upper() == "N":
                print(f"{Fore.GREEN}Thanks for playing {player.name}!")
                print(f"Final score: {Fore.YELLOW}{player.score}")
                update_leaderboard(player)
                quit()
            else:
                clear_screen()
                print(f"{Fore.RED}{restart} is not valid.")
                print("Type Y or N.")


main()
