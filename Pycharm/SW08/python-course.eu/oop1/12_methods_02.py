#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Methods
# bind the function hi to a class attribute say_hi


def hi(obj):                               # funktion!!!
        print("Hi, I am " + obj.name)


class Robot:
    say_hi = hi      # method   say_hi ist ein Zeiger auf die gleiche Stelle wie 'hi' und hi ist eine Funktions-Objekt


x = Robot()
x.name = "Marvin"
Robot.say_hi(x)

# But you shouldn't do it like this
#
# The proper way to do it:
# * Instead of defining a function outside of a class definition
#   and binding it to a class attribute, we define a method
#   directly inside (indented) of a class definition.
# * A method is "just" a function which is defined inside of a
#   class.
# * The first parameter is used a reference to the calling
#   instance.
# * This parameter is usually called self.
# * Self corresponds to the Robot object x.
