# See README.md for instructions on what to do this program

import random

random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# random.seed() controls the randomness in Python such that we get the same sequence of random results every time the program is run
# makes the sequence predictable for each time you enter that number
# Each seed number starts the generator at a different point
