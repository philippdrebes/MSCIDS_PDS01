#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Overriding

# We could also use the super function.
#
# Super is not really necessary in this case. One could argue that it makes the
# code more maintainable, because we could change the name of the parent class


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):

    def say_hi(self):
        super().say_hi()
        print("and I am a physician!")


doc = PhysicianRobot("Dr. Frankenstein")
doc.say_hi()

# The real benefit of super shows when we use it with
# multiple inheritance.
