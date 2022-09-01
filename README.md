# The Guessing Game

The Guesing Game is created as a simple number game. It randomly generates a number and asks users to guess the number between 1 - 20. Depending on the users guess, the game will let you know if a user as guessed too high, or too low to the generated number. Users have 5 attempts to guess the number. 

The project was created using Python. 

![The Guessing Game on multiple platforms](assets/images/Multiscreen%20image.png)

## Features

The purpose of the game is to demonstrate my use of Python. No HTML, CSS or JavaScript has been used. The project released through Heroku displays a simple Python engine in which the code created can be displayed and used. 

## Game start

![Opening screen](assets/images/Start%20screen.png)

The game opens with a welcome message, and to enter your name to begin the game. 

## Playing the game

![Game beginning](assets/images/game%20beginnning.png)

The game then welcomes the user to the start of the game. It then states that the game is thinking of a number between 1 and 20. Then gives the user an opportunity to make their first guess. 

## Guess attempts

![Guess attempts](/assets/images/first%20guess.png)

Once the user has entered their first guess, the game will give the user a hint if their guess was too low or too high to the number the game has generated. Users have a total of 5 attempts to guess the generated number. 

## Game outcome

![Game outcome/ loss](assets/images/game%20outcome.png)

If a user cannot guess the number within 5 attempts the game will end. It will explain that a user didn't guess the number within 5 attempts, and give the name it was looking for. 

## Game win

![Game win](assets/images/Game%20win.png)

If a user guesses the number within 5 attempts, then the user wins. The game will give a success message showing that the user won the game, and how many attempts they did it in.

## Game continuation

![Contiue Game](assets/images/continue%20game.jpg)

Once the game is complete, is will ask whether the user wants to continue the game, or whether the user wants finish the game. It will give options to which buttons to use to continue, and which buttons to use to exit the game. 

## Validation

Validation used within the game is to ensure that:

1) That a number is entered during the guessing part of the game
2) that a number between 1 and 20 is used, any other numbers entered and the game will show an error message explaining that only numbers between 1 and 20 can be entered. 

## Testing

The Guessing Game was tested in the terminal on Github at each stage after code was written using various 'print' statements to ensure that code written is going to work as it should. This also allowed me to progress through the code knowing that each stage was correct so any faults found could only be with the code just created. 

The code has also been tested using the PEP8 platform and shows no errors in the code. 

[PEP8 result](/assets/images/PEP8%20results.jpg)

The PEP8 results returned 8 "line too long" errors. I have ignored these as they are for comments within the print statements, which I cannot shorten anymore. 
The result also returned 3 space errors within the code, upon inspecting these, any changes I made cretaed errors in the code, and stopped the game from working. I have ignored those as well as the game works with all of the above errors found in the code checker. 

## Deployment

The game was created with a repository in GitHub and the code written using the Code Institue Python template in GitPod.
Once the code was written the game was published in the Python simulator Heroku. 

In GitPod the code was created and saved using various git commits and git pushes to save history versions of the code in case of error. 

In Heroku, the code was uploaded to the platform and went through Heroku automated checks to make sure it is going to operate correctly. Once those checks were done, the program or "app" is ready to be launched. Once launched, then it creates a URL which can be shared. 

## Credits

[Django Central](https://djangocentral.com/creating-a-guessing-game-in-python/)