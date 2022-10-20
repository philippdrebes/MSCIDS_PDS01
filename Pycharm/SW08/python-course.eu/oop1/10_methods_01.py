#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Methods
# Methods in Python are essentially functions


def hi(obj):
    print("Hi, I am " + obj.name + "!")


class Robot:
    pass

Robot.name = "Gugus"
x = Robot()
print("1) ", x.__dict__)

x.name = "Marvin"
print("2) ", x.__dict__)
hi(x)

y = Robot()
hi(y)
