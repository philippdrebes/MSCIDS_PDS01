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
        self.x = x


p1 = P(42)
p2 = P(4711)
print(p1.x)
p1.x = 47
p1.x = p1.x + p2.x
print(p1.x)

# Yes, in this case there is no data encapsulation. We don't
# need it in this case. The only thing get_x and set_x in our
# starting example did was "getting the data through" without
# doing anything, no checks nothing.
