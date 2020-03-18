
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
            print()
            continue

SECRET = 7
GUESSES_ALLOWED = num_check("How many guesses do you want? ")
already_guessed = []

print("I have chosen a secret number that you have to guess, "
      "and you only have {} tries. ".format(GUESSES_ALLOWED))
print("Enter your guess below to start")

print()

# Initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = num_check("Guess: ") # replace this with function call in due course
    if guess in already_guessed:
        print("You already guessed that number. Please try again. "
              "You still have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    guesses_left -= 1

    # If user has guesses left...
    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a  higher number.")
            print()
        elif guess > SECRET:
            print("Too high, try a lower number.")
        else:
            print("Congratulations, you found the secret number (☞ﾟヮﾟ)☞")

        print("You have {} guesses left".format(guesses_left))
        print()
    else:
        print("Sorry you have run out of guesses. You lose ┐(￣ー￣)┌")
        print()
        print("The secret number was {}.".format(SECRET))
        break
