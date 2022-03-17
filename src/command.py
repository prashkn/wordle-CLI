from guesses import VALID_GUESSES


def user_starts():
    print("Welcome to Wordle CLI!")
    user_input = input("do you want to start the game? (y/n): ")

    if user_input == "y":
        return True
    
    return False


def get_board(guesses, solution):
    hints = [""] * 5
    print(guesses)

    for i in range(len(guesses)):
        for j in range(len(guesses[i])):
            if guesses[i][j] == solution[j]:
                hints[i] += "🟩"
            elif guesses[i][j] in solution:
                hints[i] += "🟨"
            else:
                hints[i] += "⬛"
    
    return hints

def print_pretty(current_board, guess):
    print("Your guess: " + guess)
    for row in current_board:
        print(row)

def close_game(stats):
    if stats[0] == False:
        print("You lost!")
        print("The word was " + stats[2])
    else:
        print("You won!")
        print("You found " + stats[2] + " in " + str(stats[1]) + " tries.")