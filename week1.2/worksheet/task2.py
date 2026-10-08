# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys
numbers = read_numbers()
if numbers ==[]:
    sys.exit("Error: no numbers provided")
else:
    print(numbers)

max_num = max(numbers)
print(f"Maximum = {max_num}")

min_num = min(numbers)
print(f"Minumum = {min_num}")

mean_num = sum(numbers)/len(numbers)
print(f"Mean = {mean_num}")

numbers.sort()
if len(numbers)% 2 == 0:
    