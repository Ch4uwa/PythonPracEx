#number_guessing_game.py
import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Type a number greater then zero!')
        quit()
else:
    print('Need to be a number!')
    quit()

random_number = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('Your guess was to high.')
    else:
        print('You guessed to low.')


print(f'You got it in {guesses} guesses')
