#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Methods
# Methods in Python are essentially functions


def hi(obj):
    print("Hi, I am " + obj.name + "!")
    # print("Hi, I am " + obj.name1 + "!")     # geht nicht, weil kein Attriubt name1!

class Robot:
    pass


x = Robot()

# mae
print("1)", x.__dict__)             # output: 1) {}

x.name = "Marvin"                  # dynamische Instantzvariable an x zufügen!
hi(x)                               # output: Hi, I am Marvin!


# mae
print("1)", x.__dict__)             # output: 1) {'name': 'Marvin'}
