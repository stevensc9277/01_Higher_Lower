# HL component 3 - compares user guess with secret number

SECRET = 7

guess = ""

while guess != SECRET:

    guess = int(input("Guess: "))  # replace this with function call in due corse

    if guess < SECRET:
        print("Too low, try a  higher number")
    elif guess > SECRET:
        print("Too high, try a lower number")
    else:
        print("Congratulations! You found the secret number")