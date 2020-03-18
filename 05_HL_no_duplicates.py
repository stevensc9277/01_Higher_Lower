# HL component 4 - compares user guess with secret number

# To do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = int(input("How many guesses do you want? "))


already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))  # replace this with function call in due course

    # Checks that guess is not duplicate
    if guess in already_guessed:
        print("You already guessed that number. Please try again. "
              "You still have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("Try a  higher number.")
            print()
        elif guess > SECRET:
            print("Try a lower number.")
        else:
            print("Congratulations, you found the secret number (☞ﾟヮﾟ)☞")

        print("You have {} guesses left".format(guesses_left))
        print()
    else:
        print("Sorry you have run out of guesses. You lose ┐(￣ー￣)┌")
        print()
        print("The secret number was {}.".format(SECRET))
        break
