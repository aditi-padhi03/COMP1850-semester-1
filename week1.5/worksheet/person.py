# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a person.

        Args: 
            name(str): The person's name, which must be a non-empty string.
            birth: The person's date of birth.

        Raises:
            TypeError: If name is not a string or birth is not a date object.
            ValueError: If name is an empty string
        """

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name:
            raise ValueError("Name cannot be an empty string.")
        if not isinstance(birth, date):
            raise TypeError("Birth date must be a date object.")
        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the initials/uppercased letters of each part of a name.
        """
        return "".join(letter[0].upper() for letter in self.name.split())

    def is_birthday(self):
        """
        Checks whether today is the person's birthday.

        Returns True if today's day and month match the date of birth, otherwise it returns False.
        """     
        today = date.today()
        if today.day == self.birth.day and today.month == self.birth.month:
            return True
        else:
            return False
   
