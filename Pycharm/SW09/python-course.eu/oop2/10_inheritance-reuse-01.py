#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_inheritance.php

# Overriding

# When we override a method, we sometimes want to reuse
# the method of the parent class and add some new stuff.


class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):

    def say_hi(self):
        Robot.say_hi(self)
        print("and I am a physician!")


doc = PhysicianRobot("Dr. Frankenstein")
doc.say_hi()
