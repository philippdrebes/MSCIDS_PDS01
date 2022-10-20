#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Public- Protected- and Private Attributes

# Every private attribute of our class has a getter and a setter.
# There are IDEs for object-oriented programming languages, who
# automatically provide getters and setters for every private
# attribute as soon as an attribute is created.

# There are at least two good reasons against such an approach.
# First of all not every private attribute needs to be accessed from outside.
# Second, we will create non-pythonic Code this way.


class A():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    def SetX(self, x):
        self.__x = x

    def SetY(self, y):
        self.__y = y


a = A(42, 24)
print(a.GetX())
a.SetX(84)
print(a.GetX())
