# HL component 2 - Generates random number between low and high

import random

low_num = 1
high_num = 4

for item in range(1, 20):
    secret = random.randint(low_num, high_num)
    print(secret, end="\t")
