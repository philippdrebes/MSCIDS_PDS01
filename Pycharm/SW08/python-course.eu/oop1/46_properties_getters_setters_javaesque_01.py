#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# Getters (also known as 'accessors') and setters
# (aka. 'mutators') are used in many object oriented
# programming languages to ensure the principle of data
# encapsulation.
#
# The Pythonic way to introduce attributes is to make them
# public.
#
# We demonstrate in the following example, how we can
# design a class in a Javaesque way with getters and setters
# to encapsulate the private attribute "self.__x":


class P:

    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


p1 = P(42)
p2 = P(4711)
print(p1.get_x())
p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
print(p1.get_x())

# show in lecture!
p1.__x = 7            # is this an "direct" assignment to our private __x variable? => NO!!!!! Why?
                      # Where is the '7' saved?
print(p1.get_x())

# to answer the question above =A check the two dict's:
# print("P.__dict__: ", P.__dict__)
# print("p1.__dict__: ", p1.__dict__)
