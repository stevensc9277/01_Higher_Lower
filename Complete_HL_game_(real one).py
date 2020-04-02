# HL component 12 - Final game with fully working program

# To do
# Find a way to reset already_guessed list for each round
# If possible, change the secret number for each round
# Replace functions with num_check and hl_statements (they are called functions right?)

import math
import random


def num_check(question, low=None, high=None):

    # sets up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))
            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()


print("**** Welcome to the Higher / Lower Game ****")           # Brief introduction and explanation
print()
print("To play, enter any number as the minimum value of your range.")
print("Then, enter another number as the maximum value of your range.")
print("The program will then choose a secret number within your range which you will try to guess.")
print()
print("You will be given a set amount of guesses for each round depending on your high / low numbers.")
print("If you have run out of guesses, then you lose the round.")
print("(Please note that the secret number for each round will not stay the same,")
print(" and duplicate guesses will not count towards the guesses you have left)")
print()

keep_going = ""
while keep_going == "":

    low_num = num_check("Please enter your low number: ")
    high_num = num_check("Please enter a higher number: ")
    while high_num <= low_num:       # Asks user to enter a higher number if 'high_num' is less than 'low_num'
        high_num = num_check("Please enter a higher number! ")

    range = high_num - low_num + 1
    max_raw = math.log2(range)  # Finds maximum # of guesses using binary search
    max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
    max_guesses = max_upped + 1     # Give user extra guess, just in case
    print("Max Guesses: {}".format(max_guesses))

    print()

    secret = random.randint(low_num, high_num)      # Pick a random number between 'low_num' and 'high_num'
    guesses_allowed = max_guesses
    already_guessed = []        # List collecting user 'guess'
    rounds = num_check("How many rounds do you want to play? ")
    while rounds < 1:       # Make sure that 'rounds' is a valid integer > 0
        rounds = num_check("Sorry, that is not valid. Please enter a number greater than or equal to 1. ")

    game_stats = []
    start = 1
    num_won = 0
    rounds_played = 0

    while rounds_played < rounds:
        guess = ""

        guesses_left = guesses_allowed

        start_round = hl_statement("### Round {} of {} ###".format(start, rounds), "#")
        start += 1

        while guess != secret and guesses_left >= 1:

            guess = num_check("Enter your guess: ")
            if guess in already_guessed:
                duplicate = hl_statement("!! You already guessed that number Please try again.   ￣へ￣    |   "
                                         "Guesses left: {} !!".format(guesses_left), "!")
                continue

            while guess < low_num or guess == 0:       # Checks to make sure that 'guess' is within boundaries
                guess = num_check("Please enter a number between {} and {}: ".format(low_num, high_num))
                continue
            while guess > high_num:     # Checks to make sure that 'guess' is within boundaries
                guess = num_check("Please enter a number between {} and {}: ".format(low_num, high_num))
                continue

            guesses_left -= 1
            already_guessed.append(guess)   # Stores guess in a list to prevent duplicate guesses later on

            if guesses_left >= 1:

                if guess < secret:
                    too_low = hl_statement("<< Too low, try a higher number.    ￣へ￣    |   "
                                            "Guesses left: {} <<".format(guesses_left), "<")

                elif guess > secret:
                    too_high = hl_statement("^^ Too high, try a lower number.   ￣へ￣    |   "
                                            "Guesses left: {} ^^".format(guesses_left), "^")

        else:
            if guess < secret:
                print("Too low!")

            elif guess > secret:
                print("Too high!")

        if guess == secret:
            if guesses_left == guesses_allowed - 1:     # Same as guessing in one try correctly
                print("Amazing! You got it in one guess (☞ﾟヮﾟ)☞")
                print()
            else:
                well_done = hl_statement("*** Well done! You got it in {} guesses"
                                         " ***".format(guesses_allowed - guesses_left), "*")
                print()
            num_won += 1
        else:
            print("Sorry - you lose this round as you have run out of guesses (╯°□°）╯︵ ┻━┻")
            print("The secret number was {}".format(secret))        # Reveal secret number
            print()
            guesses_left -= 1

        game_stats.append(guesses_allowed - guesses_left)

        print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))  # Show number of rounds won/lost
        rounds_played += 1
        print()
        if rounds_played >= 1:
            secret = random.randint(low_num, high_num)      # reset secret number after a round
            already_guessed.clear()     # Clear list to recycle guess / user input

    # Print each round's outcome
    print()
    print("*** Game Scores ***")
    list_count = 1
    for item in game_stats:
        print("Round {}: {}".format(list_count, item))  # Shows round played and number of guesses used in that round
        list_count += 1

    # Calculate statistics
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats) / len(game_stats)

    print()
    print("*** Summary Statistics ***")
    print("Best: {}".format(best))   # Least number of guesses used
    print("Worst: {}".format(worst))      # Most number of guesses used
    print("Average: {:.2f}".format(average))    # Average guesses used

    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()

print("Thank you for playing the Higher / Lower game. ( ﾟдﾟ)つ Bye~~~")
