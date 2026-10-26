# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """Creates a point, given x and y coordinates"""
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

p = Point(1.5, 4.2)
q = Point(3.7, 2.6)
print(p.distance_to(q))


