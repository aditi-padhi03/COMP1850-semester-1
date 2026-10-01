# Fill out the code to make a very simple calculator
try:
# ask the user to enter number1:
    num1 = int(input("Enter first number: "))

# ask the user to enter number 2:
    num2 = int(input("Enter second number: "))

# calculate the result of adding those numbers together
    answer = num1 + num2

# print out the answer
    print(f"{num1} + {num2} = {answer}")
except:
    print("Please enter numbers only")