# __Hangman - Portfolio Project 3__
This is Python terminal game of Hangman and is deployed on Heroku using Code Institute's mock terminal template.

Users enter their name and location before being brought to the main menu where they can start a game, view the rules or look at the leaderboard. After choosing to start the game they must choose their difficulty and begin guessing letters or words until either the word is found or they run out of lives. The number of lives is determined by what difficulty they choose.

If the user gets the word correct they gain points depending on their difficulty level and length of the word. Easy gets you 1 point, normal 2 points and hard 3 points. The user is given an additional point if their word is longer than 6 letters. After the game is finished the user is given the choice to either play again or quit the game and the user can play the game as many times as they want with their points adding up after each game. If a user loses a game and their score is more than 1, they will lose 1 point.

On exit of the game, the user's score is checked against the current leaderboard and if the user is told whether or not they made the top 10.

[Live link to website](https://python-hangman-adam-gilroy.herokuapp.com/)

## __UX & Design__

### __User Stories__
- As a user, I want to be able to input my name and location and be given feedback if I entered invalid data.
- As a user, I want to be able to view the rules of the game.
- As a user, I want to be able to view the current leaderboard.
- As a user, I want to be able to choose the game's difficulty.
- As a user, I want to be able to see how many letters I need to guess.
- As a user, I want to be able to see what letters I've already guessed.
- As a user, I want to be notified if I try to guess a letter or word I've already guessed.
- As a user, I want a clear picture of how many guesses/lives I have left.
- As a user, I want to be able to restart the game after the game has finished without exiting the program to do so.
- As a user, I want to see if I've made the leaderboard after exiting the game after playing.

### __Flowchart__
I made this flowchart before writing my code to give myself a clear view of what needed to be implemented as I wrote the program. It clearly indicates the layout and structure of the program including where the user needs to be asked for input, where the computer much check the input and how to handle invalid inputs, where the program should subtract the user's lives and add to the user's score.

![Flowchart](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/flowchart/hangman-flowchart.png)

### __Colour Scheme__
As this program was built for the terminal, there wasn't much in terms of design or colour but I did use [Colorama](https://pypi.org/project/colorama/) to add a bit of colour where I felt was needed within the terminal to make certain parts stand out to the user.

## __Features__ 

- __Welcome Screen__
    - The user is welcomed to the game and prompted to input their name and location.

![Welcome Screen](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/welcome-screen.png)

- __Main Menu__
    - From the main menu, the user can start the game, view the game rules, view the current leaderboard, and exit the game.

![Main Menu](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/main-menu.png)

- __Rules__
    - This displays the rules and scoring system for the game and the user can be easily brought back to the main menu by hitting the enter key.

![Rules](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/rules.png)

- __Leaderboard__
    - This displays the current top 10 leaderboard so the user can see what score they'll need to beat while playing the game.

![Leaderboard](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/leaderboard.png)

- __Difficulty Selection__
    - This allows the user to select the difficulty which sets how many lives they begin the game with and will also award them more points for guessing a word correctly for harder difficulties.

![Difficulty Menu](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/difficulty-menu.png)

- __Hangman Game__
    - This is the main feature of the program. The user is met with a graphic displaying the hangman depending on how many lives they have with the graphic updating as their lives get lower and more of the hangman appearing.
    - The user is promtped with underscores ( _ ) to let them know how many letters are in the word.
    - The user can enter letters or full words of the same number of letters until they either get the word correct or run out of lives.

![Game Start](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-start.png)

![Wrong Guess](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-wrong-guess.png)

![Right Guess](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-right-guess.png)

![Wrong Word Length](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/wrong-word-length.png)

- __Letters Guessed__
    - As the user plays the game, the letters that they have already guessed will be displayed to them so they know which ones they haven't tried yet. If a user enters a letter that they have guessed previously, they will be reminded of this and prompted to try again without losing a life.

![Letters Guessed](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/letters-guessed.png)

![Already Guessed](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/guessed-already.png)

- __Lives Indicator__
    - As part of the hangman graphic that prints to display how close the user is to losing, the number of guesses they have left is displayed to let them know exactly how many lives they have remaining. The color also changes from green to yellow to red the closer you get to losing.

![Orange Warning](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-orange-warning.png)

![Red Warning](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-red-warning.png)

- __Restart Game__
    - Once the game is over and the user has either won or lost, they will be asked if they want to play again. If the user chooses Y, they will be brought back to the difficulty select menu where they can begin a new game and try to add to their existing score. If they choose N, their current score will be checked against the current leaderboard and updated if necessary before ending the game.

![Game Over - Lose](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-over-lose.png)

![Game Over - Win](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/game-over-win.png)

![Restart Game](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/restart-game.png)

![New Game](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/restart-game-score.png)

- __Leaderboard Update__
    - When the user decides to stop playing the game, their score will be checked against the current leaderboard. If their score gets them in the top 10 then they will be told and added to the board, if not they will get a message to try again next time. The most up to date version of the leaderboard is then printed for the user to see before the game exits.

![Didn't Make Leaderboard](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/end-game-not-top-10.png)

![Made Leaderboard](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/end-game-top-10.png)

- __Uninterrupted User Experience__
    - At all points during the program, a user is kept in a loop preventing the program from crashing or exiting if the player enters an invalid input. For example if a user was to enter a number instead of a letter when guessing, they will be alerted and looped back to be prompted to guess a letter or word without losing a life in the game. More of this can be seen in the [testing section](TESTING.MD)

![Invalid Input](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/invalid-input.png)

### __Features Left to Implement__
- __Local Leaderboard__
    - I plan to add local leaderboards so users can see how they compare to other users in their location.

- __Multiplayer Mode__
    - I plan to add multiplayer mode where one player types a word for the other player to guess with first to 5 points winning.

### __Technologies Used__
The following is a list of the technologies I used on this project.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - The program was written entirely in Python.
- [Github](https://github.com/)
    - Github was used to store the project's code after being pushed from Git.
- [Gitpod](https://gitpod.io/)
    - Gitpod terminal was used to commit my code using Git and push it to Github.
- [Git](https://git-scm.com/)
    - Git was used for version control through the Gitpod terminal.
- [Techsini](http://techsini.com/multi-mockup/index.php)
    - Techsini was used to generate mockups for the project.

## __Testing__
View testing [here.](TESTING.md)

## __Bugs__
I used GitHub's issues section to track and manage any bugs that I found during the development and testing of my program. I currently have 0 open bugs and a history of the bugs I tackled can be found [here](https://github.com/adamgilroy22/python-hangman/issues?q=is%3Aissue+is%3Aclosed)

## __Deployment__

### __Local Deployment__
In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/adamgilroy22/python-hangman.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/adamgilroy22/python-hangman)

## __Credits__

### __Code__
- Code to pull random word from words.txt taken from [here](https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/)
- Code to create clear_screen function taken from [here](https://www.geeksforgeeks.org/clear-screen-python/)
- Code to create Player class learned from [here](https://realpython.com/python3-object-oriented-programming/)
- Code to update leaderboard taken from [here](https://stackoverflow.com/questions/50938274/sort-a-spread-sheet-via-gspread) and [here](https://blog.aspose.com/2021/04/13/insert-and-delete-rows-and-columns-in-excel-using-python/)
- Code to display leaderboard in columns taken from [here](https://stackoverflow.com/questions/61285626/print-list-of-lists-in-neat-columns-table)

### __Content__
- Words.txt content taken from [here](https://github.com/Xethron/Hangman/blob/master/words.txt)
- Hangman graphics taken from [here](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)

### __Design__
- Flowchart was made using [Lucidchart.](https://www.lucidchart.com/pages/)

## __Acknowledgements__

I would like to give special thanks to my mentor, [Tim Nelson](https://www.linkedin.com/in/travel-tim-nelson/) for his guidance during the development of this project.