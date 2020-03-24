# HL component 8 - set up score mechanics

# To do
# Set up round and win counter
# update feedback statements

SECRET = 7
GUESSES_ALLOWED = int(input("How many guesses do you want? "))
rounds = int(input("How many rounds do you want to play? "))    # replace with num_check
game_stats = []

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess: "))  # replace this with function call in due course
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))
                print()

            elif guess > SECRET:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
                print()

    else:
        if guess < SECRET:
            print("Too low!")

        elif guess > SECRET:
            print("Too high!")

    if guess == SECRET:
        if guesses_left == GUESSES_ALLOWED - 1:
            print("Amazing! You got it in one guess 👌")
            print()
        else:
            print("Well done, you got it in {} guesses (☞ﾟヮﾟ)☞".format(GUESSES_ALLOWED - guesses_left))
            print()
        num_won += 1
    else:
        print("Sorry - you lose this round as you have run out of guesses (╯°□°）╯︵ ┻━┻")
        guesses_left -= 1

    game_stats.append(GUESSES_ALLOWED - guesses_left)

    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1
    print()

# Print each round's outcome
print()
print("*** Game Scores ***")
list_count = 1
for item in game_stats:

    # indicates if game has been won or lost
    if item > GUESSES_ALLOWED:
        status = "Lost, ran out of guesses"
    else:
        status = "Won"

    print("Round {}: {}".format(list_count, item))
    list_count += 1

# Calculate then print game statistics
game_stats.sort()
best = game_stats[0]    # first item in sorted list
worst = game_stats[-1]  # last item in sorted list
average = sum(game_stats) / len(game_stats)

print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))
