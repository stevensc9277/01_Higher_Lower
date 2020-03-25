# HL component 11 - Maximum Guesses Calculator

import math

for item in range (0, 4):   # Loop component for easy testing...
    low = int(input("Low: "))   # use num_check in due course
    high = int(input("High: ")) # use num_check in due coure

    range = high - low + 1
    max_raw = math.log2(range)  # Finds maximum # of guesses using binary search
    max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
