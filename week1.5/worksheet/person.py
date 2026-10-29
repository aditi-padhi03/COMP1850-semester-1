# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a person's name and date of birth
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
        

        


    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)