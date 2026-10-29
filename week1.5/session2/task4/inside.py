# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import math 


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns string representation of this point
        """
        return f"({self.x}, {self.y})"

class Circle:
    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Creates a Circle, given values for radius & centre coordinates.

        Radius must always be supplied. Centre coordinates are optional
        but should be provided as a Point object. If they are omitted, the
        circle will be centred at the origin.
        """
        self.radius = radius
        self.centre = centre

    def __str__(self):
        """
        Returns the string representation of a circle.
        """
        return f"({self.radius},{self.centre})"

    def __contains__(self, point):

        distance = math.sqrt((point.x - self.centre.x)**2 + (point.y - self.centre.y)**2)
        
        # A point is inside the circle if its distance to the center <= radius
        if distance <= self.radius:
            return True
        else:
            return False