import random

number = random.randint(1, 20)


def validate_number_input(data):
    """ This method validates that the input is a number from 1 to 20 """
    if data.isdigit():
        if int(data) > 0 and int(data) < 21:
            return True
        else:
            print('opps')
            print(f'Your guess of {data} is not a number from 1 to 20')
            return False
    else:
        print('What you entered is not a number!')
        return False
    return True


def get_player_namer():
    player_name = input("Hello, tell me your name, if you enter nothing we will call you player one:").strip().lower()
    """This method validates that either a name is entered, or a default is used"""
    if player_name == "":
        player_name = "player one"
    return player_name


def game_loop(player_name):
    """Game loop functions to help the user through the game and make guesses"""
    number_of_guesses = 0
    print(f'okay! {player_name} I am guessing a number bewween 1 and 20, what am i guessing?')

    while number_of_guesses < 5:
        player_guess = input().strip()
        # check that what is entered is a number
        check_guess = validate_number_input(player_guess)

        if check_guess:
            guess = int(player_guess)

            number_of_guesses += 1
            if guess < number:
                print('Your guess is too low')
            if guess > number:
                print('Your guess is too high')
            if guess == number:
                print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
                break
    if number_of_guesses >= 5:
        print('You did not guess the number, The number was ' + str(number))   
    
def main():
    """When the game is over, this loop will suggest the user contine or end the game"""
    player_name = get_player_namer()
    while True:
        game_loop(player_name)
        ask_at_end = input('Would like like another game? Hit any key to go again or type n or no to stop').strip().lower()
        answer_no = ['n', 'no']
        if ask_at_end in answer_no:
            print(f"Thank's for playing {player_name}, hope to see you again soon")
            exit()
        else:
            continue


if __name__ == "__main__":
    main()
