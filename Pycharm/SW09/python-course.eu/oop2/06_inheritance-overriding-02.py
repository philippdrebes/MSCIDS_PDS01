#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Overriding

# If a method is overridden in a class, the original method
# can still be accessed, but we have to do it by calling
# the method directly with the class name


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):

    def say_hi(self):
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")


y = PhysicianRobot("Doc James")
y.say_hi()
print("... and now the 'traditional' robot way of saying hi :-)")
Robot.say_hi(y)
