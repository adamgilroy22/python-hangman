## __User Stories Testing__
| User Goal | Requirement met | Image(s) |
| --------- | --------------- | -------- |
| As a user, I want to be able to input my name and location and be given feedback if I entered invalid data. | Yes | ![User test 1a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-1-a.png) ![User test 1b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-1-b.png) ![User test 1c](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-1-c.png) |
| As a user, I want to be able to view the rules of the game. | Yes | ![User test 2a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-2-a.png) ![User test 2b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-2-b.png) |
| As a user, I want to be able to view the current leaderboard. | Yes | ![User test 3a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-3-a.png) ![User test 3b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-3-b.png) |
| As a user, I want to be able to choose the game's difficulty. | Yes | ![User test 4a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-4-a.png) |
| As a user, I want to be able to see how many letters I need to guess. | Yes | ![User test 5a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-5-a.png) |
| As a user, I want to be able to see what letters I've already guessed. | Yes | ![User test 6a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-6-a.png) |
| As a user, I want to be notified if I try to guess a letter or word I've already guessed. | Yes | ![User test 7a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-7-a.png) ![User test 7b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-7-b.png) |
| As a user, I want a clear picture of how many guesses/lives I have left. | Yes | ![User test 8a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-8-a.png) ![User test 8b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-8-b.png) |
| As a user, I want to be able to restart the game after the game has finished without exiting the program to do so. | Yes | ![User test 9a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-9-a.png) ![User test 9b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-9-b.png) |
| As a user, I want to see if I've made the leaderboard after exiting the game after playing. | Yes | ![User test 10a](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-10-a.png) ![User test 10b](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-10-b.png) |

## __Program Validation Testing__
| Section Tested | Input To Validate | Expected Outcome | Actual Outcome | Pass/Fail |
| -------------- | ----------------- | ---------------- | -------------- | --------- |
| Start Program | N/A | Load welcome message and prompt user to enter name | As expected | PASS |
| Enter Name | Input "Adam" | Move on to ask user for location | As expected | PASS |
| Enter Name | Input "1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Name | Input "A1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Name | Input "Adam Gilroy" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Name | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Location | Input "Cork" | Move on to game menu | As expected | PASS |
| Enter Location | Input "Cork City" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Location | Input "0.1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Location | Input "a8pwj3" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Location | Input "5" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Location | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game Menu | Input "1" | Move on to difficulty select menu | As expected | PASS |
| Game Menu | Input "2" | Display game rules | As expected | PASS |
| Game Menu | Input "3" | Display leaderboard | As expected | PASS |
| Game Menu | Input "4" | Say goodbye to the user and exit program | As expected | PASS |
| Game Menu | Input "a" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game Menu | Input "6" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game Menu | Input "1a" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Game Menu | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Rules | User hits enter key | Return user to menu | As expected | PASS |
| Leaderboard | User hits enter key | Return user to menu | As expected | PASS |
| Difficulty Selection Menu | Input "1" | Set player lives to 9 and begin game | As expected | PASS |
| Difficulty Selection Menu | Input "2" | Set player lives to 7 and begin game | As expected | PASS |
| Difficulty Selection Menu | Input "3" | Set player lives to 5 and begin game | As expected | PASS |
| Difficulty Selection Menu | Input "4" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Difficulty Selection Menu | Input "easy" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Difficulty Selection Menu | Input "1a" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Difficulty Selection Menu | Input "n" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Difficulty Selection Menu | Press enter with no input | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Main Game | Input a single letter | Check if the letter is in the word to be guessed and notify the user if they guessed correct or not | As expected | PASS |
| Main Game | Input a word of the same length as the word to be guessed | Check if the word is correct and notify the user if they guessed correct or not | As expected | PASS |
| Main Game | Input a word not of the same length as the word to be guessed | Let the user know that their guess isn't the correct length and remind them how many letters are in the word | As expected | PASS |
| Main Game | Input "0" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Main Game | Input "appl3" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Play Again Menu | Input "y" | Bring user back to difficulty select menu to start the game again | As expected | PASS |
| Play Again Menu | Input "Y" | Bring user back to difficulty select menu to start the game again | As expected | PASS |
| Play Again Menu | Input "N" | Print players final score, let them know if they made the top 10 or not and print the leaderboard before thanking them for playing and exiting the program | As expected | PASS |
| Play Again Menu | Input "n" | Print players final score, let them know if they made the top 10 or not and print the leaderboard before thanking them for playing and exiting the program | As expected | PASS |
| Play Again Menu | Input "Yes" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Play Again Menu | Input "no" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Play Again Menu | Input "1" | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Play Again Menu | Input "Y1" | Notify user that this isn't a valid input and loop back | As expected | PASS |