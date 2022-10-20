#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Difference between type and isinstance

# We see that isinstance returns True if we compare an object
# either with the class it belongs to or with the
# superclass. Whereas the equality operator (for type) only
# returns True, if we compare an object with its own class.


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


x = Robot("Marvin")
y = PhysicianRobot("James")

print(isinstance(x, Robot), isinstance(y, Robot))
print(isinstance(x, PhysicianRobot))
print(isinstance(y, PhysicianRobot))

print(type(y) == Robot, type(y) == PhysicianRobot)


# Object type comparisons should always use isinstance()
# instead of comparing types directly.
