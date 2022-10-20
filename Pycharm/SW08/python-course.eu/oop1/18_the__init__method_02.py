#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# The __init__ Method

# We add an __init__-method to our robot class:


class Robot:

    def __init__(self, name=None):
        self.name = name             # self.name ist ein neues Attribut von der Klasse Robot

    def say_hi(self):
        if self.name:    # d.h. nicht 'None' ist
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")


x = Robot()    # Robot wird OHNE Parameter aufgerufen!!
print(x.__dict__)
#x.name = "C34-W3"
x.say_hi()

y = Robot("Marvin")
y.say_hi()
