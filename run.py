import random

number = random.randint(1, 20)

player_name = input("Hello, What's your name?")

print('okay! '+ player_name+ ' I am Guessing a number between 1 and 20:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break