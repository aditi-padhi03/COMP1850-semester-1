# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0
    """For a given input, the program goes through all its characters to see if its a string of words. 

    It looks for upper and lower case characters. Everytime an upper case character is found using .isupper(), the value of upper gets increased by 1. 
    Same is the case for when a lower case character is found (by using the built-in function .islower()). 
    
    The function returns the number of uppercase and lowercase characters in the format (upper, lower)
    """

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

print(mystery_func("X"))
print(mystery_func("[2, 3]")) #the class type in the def funtion is a 'string' while in this case we have entered a 'list'
