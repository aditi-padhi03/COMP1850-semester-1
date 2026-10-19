
# function implementation

def rectangle_area():  # define suitable input data
    l = int(input("Enter length: "))
    b = int(input("Wnter breadth: "))               # implement the function
    return (l*b)              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area()}")   # provide suitable data matching your inputs


# find the even numbers up to some limit

def even_numbers(limit):
    return [n for n in range(limit+1) if n % 2 == 0]

print(even_numbers(20))