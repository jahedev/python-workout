"""
Write a function (guessing_game) that takes no arguments.
When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.

Each time the user enters a guess, the program indicates one of the following:
–Too high
–Too low
–Just right

If the user guesses correctly, the program exits. 
Otherwise, the user is asked totry again.
The program only exits after the user guesses correctly.
"""

import random

def guessing_game():
    expected_number = random.randint(10,30)

    user_input = ''
    num_tries = 1

    print('\nWelcome to the number guessing game!')
    print('Guess a number between 10 and 30.\n')

    while not user_input or not user_input.isdigit():
        user_input = input('Guess a number: ')

        guess = int(user_input)

        if (guess == expected_number):
            guessed_correctly = True
            break
        elif (guess < expected_number):
            print('Too Low!')
        else:
            print('Too High')
        
        num_tries += 1
        user_input = ''

    print(f'\nYou guessed correctly! It took you {num_tries} tries.')

if __name__ == '__main__':
    guessing_game();
