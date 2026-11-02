# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
import shapes

circle = shapes.Circle(2.5)

print(circle)

print(f"Area = {circle.area():.3f}")
print(f"Perimeter = {circle.perimeter():.3f}")

print("Moving the circle...")
circle.set_position(shapes.Point(1.6, 3.2))
print(circle)

print("Changing the circle's colour...")
circle.set_colour("green")
print(circle) 

