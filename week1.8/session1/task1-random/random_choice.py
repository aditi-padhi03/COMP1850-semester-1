import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

number = int(input("Enter a number: "))
chosen_names = random.sample(names, number)

for name in chosen_names:
    print(name)

