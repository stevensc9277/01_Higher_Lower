# HL component 4 - compares user guess with secret number

# To do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
guess = ""

while guess != SECRET:

    guess = int(input("Guess: "))  # replace this with function call in due course

    if guess < SECRET:
        print("Too low, try a  higher number")
    elif guess > SECRET:
        print("Too high, try a lower number")
    else:
        print("Congratulations! You found the secret number")
    print()

    rounds = +1
    if rounds > 10:
        print("You have passed the number of rund")
