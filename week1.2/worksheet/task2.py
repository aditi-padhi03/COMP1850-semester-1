# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys
numbers = read_numbers()
if numbers ==[]:
    sys.exit("Error: no numbers provided")
else:
    min_num = min(numbers)
    print(f"Minimum = {min_num}")

    max_num = max(numbers)
    print(f"Maximum = {max_num}")

    mean_num = sum(numbers)/len(numbers)
    print(f"Mean = {mean_num}")

    numbers.sort()
    mid = len(numbers)// 2
    if len(numbers)%2 != 0:
        print(f"Median: {numbers[mid]}")
    elif len(numbers)%2 == 0:
        print(f"Median = {(numbers[mid-1]+numbers[mid])/2}")
    