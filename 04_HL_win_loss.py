# HL component 4 - compares user guess with secret number

# To do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = 4

# Initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))  # replace this with function call in due course
    guesses_left -= 1

    # If user has guesses left...
    if guesses_left >= 1:
        print("You have {} guesses left".format(guesses_left))
    else:
        print("Sorry you have run out of guesses. You lose ┐(￣ー￣)┌")
        print()
        print("The secret number was {}.".format(SECRET))

        break

    if guess < SECRET:
        print("Try a  higher number.")
    elif guess > SECRET:
        print("Try a lower number.")
    else:
        print("Congratulations! You found the secret number.")
    print()
