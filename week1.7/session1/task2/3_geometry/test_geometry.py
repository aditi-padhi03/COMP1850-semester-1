# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0
    
    
def test_circle_contructor():
    c = Circle(2.0)
    assert c.radius == 2.0
    assert c.centre.x == 0.0
    assert c.centre.y == 0.0
    circle2 = Circle(4.0, Point(1.0, 2.0))
    assert circle2.radius == 4.0
    assert circle2.centre.x == 1.0
    assert circle2.centre.y == 2.0

def test_cicle_area():
    c = Circle(1.0)
    assert c.area() == 3.141592653589793

def test_circle_perimeter():
    c = Circle(10)
    assert c.perimeter() == 62.83185307179586
    

