#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Simple Inheritance Example

# The syntax for a subclass definition looks like this:
#
# class DerivedClassName(BaseClassName):
#     pass
#
# Instead of the pass statement, there will be methods
# and attributes like in all other classes.

# We define a class PhysicianRobot, which inherits from Robot.


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


x = Robot("Marvin")
y = PhysicianRobot("James")

print(x, type(x))
print(y, type(y))

y.say_hi()


# As the class PhysicianRobot is a subclass of Robot, it
# inherits in this case both the method __init__ and say_hi.
#
# Inheriting these methods means that we can use them as if
# they had been defined in the PhysicianRobot class.
#
# When we create an instance of PhysicianRobot, the __init__
# function will also create a name attribute.
