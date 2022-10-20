#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Overriding

# An instance of a PhysicianRobot should say hi in a
# different way
#
# A method of a parent class gets overridden by simply
# defining in the child class a method with the same name.


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):

    def say_hi(self):
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")


y = PhysicianRobot("James")
y.say_hi()
