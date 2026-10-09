# Worksheet 1.2: Task 1 Solution
import sys
grade_inp = input("Enter an integer grade in the range 0 to 100: ")

try: 
    grade = int(grade_inp)
    if 0 <= grade <= 100:
        if 0 <= grade <= 39:
            print(f"{grade} is a Fail")
        elif 40 <= grade <= 69:
            print(f"{grade} is a Pass")
        else:
            print(f"{grade} is a Distinction")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except: 
    sys.exit("Error: Grade must be an integer between 0 and 100")

