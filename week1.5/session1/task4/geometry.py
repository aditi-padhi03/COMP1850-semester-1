# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a point, given x and y coordinates
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this point from origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, point):
        """
        Returns distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)

class Circle:
    """
    A circle, with radius and centre coordinates.
    """
    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Creates a Circle object, with the given radius and centre coordinates.

        Centre coordinates default to the origin.
        """
        self.centre = centre
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi*(self.radius**2)

    
    def perimeter(self):
        """
        Returns the perimeter of the circle
        """
        return 2*math.pi*self.radius


