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
- As a user, I want to be able to see what letters I've already guessed
- As a user, I want to be notified if I try to guess a letter or word I've already guessed.
- As a user, I want a clear picture of how many guesses/lives I have left.
- As a user, I want to be able to restart the game after the game has finished without exiting the program to do so.
- As a usre, I want to see if I've made the leaderboard after exiting the game after playing.

### __Flowchart__
I made this flowchart before writing my code to give myself a clear view of what needed to be implemented as I wrote the program. It clearly indicates the layout and structure of the program including where the user needs to be asked for input, where the computer much check the input and how to handle invalid inputs, where the program should subtract the user's lives and add to the user's score.
![Flowchart](https://github.com/adamgilroy22/python-hangman/blob/main/documentation/flowchart/hangman-flowchart.png)

### __Colour Scheme__

## __Features__ 

- __Feature #1__
    - 

### __Features Left to Implement__
- __Local Leaderboard__
    - I plan to add local leaderboards so users can see how they compare to other users in their location.

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

## Deployment

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/adamgilroy22/stick-kick.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/adamgilroy22/stick-kick)

## __Credits__

### __Code__

### __Content__

- All website text content was created and written by me.

### __Design__

- Flowchart was made using [Lucidchart.](https://www.lucidchart.com/pages/)

## __Acknowledgements__

I would like to give special thanks to my mentor, [Tim Nelson](https://www.linkedin.com/in/travel-tim-nelson/) for his guidance during the development of this project.