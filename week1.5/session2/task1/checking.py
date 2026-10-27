# Week 1.5, Session 2: Task 1

# Add type checking to the constructor of Point

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

        if not isinstance(x, (int, float)):
            raise TypeError("x must be an integer.")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be an integer.")
        
    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Test program

p = Point("two", "one")
print(p.distance())
