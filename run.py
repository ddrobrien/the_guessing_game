import random

def validate_number_input(data):
    """ This method validates that the input is a number from 1 to 20 """
    if data.isdigit():
        if int(data) > 0 and int(data) < 21:
            return True
        else:
            print('opps')
            print (f'Your guess of {data} is not a number from 1 to 20')
            return False
    else:
        print('What you have entered is not a number!')
        return False
    return True

number = random.randint(1, 20)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('Hello '+ player_name+ ' I am Guessing a number between 1 and 20. Can you guess the number? You only 5 attempts to guess')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))