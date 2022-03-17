from command import *
from guesses import *
import random

if not user_starts():
    exit()

is_Done = False
stats = ()
guesses = []
key_word = random.choice(VALID_GUESSES)

while not is_Done:
    guess = input("What's your guess: ")
    if len(guess) != 5 or guess not in VALID_GUESSES:
        print("Please enter a valid guess")
    else:
        guesses.append(guess)
        current_board = get_board(guesses, key_word)
        print_pretty(current_board, guess)
    
    is_Done = len(guesses) == 5
    if is_Done:
        stats = (guesses[4] == key_word, len([x for x in guesses if len(x) == 5]), key_word)

close_game(stats)