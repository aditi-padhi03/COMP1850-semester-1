# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum


class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        if not isinstance(pounds, int):
            raise TypeError("Pounds must be an integer.")
        if pounds < 0:
            raise ValueError("Pounds must be non-negative.")

        if not isinstance(pence, int):
            raise TypeError("Pence must be an integer.")
        if not(0 < pence <= 99):
            raise ValueError("Pence must be non-negative and less than 99.")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence}"
        

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        if not isinstance(other, Money):
            raise TypeError("'other' must be a Money object")
        
        return Money(self.pounds + other.pence, self.pence + other.pence)
        

m1 = Money(1, 8)
m2 = Money(10, 11)
sum = m1 + m2
print(sum)