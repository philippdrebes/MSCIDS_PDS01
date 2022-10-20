#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# You can start with the simplest implementation imaginable,
# and you are free to later migrate to a property version without
# having to change the interface! So properties are not just a
# replacement for getters and setter!
#
# Something else you might have already noticed:
# For the users of a class, properties are syntactically identical
# to ordinary attributes.


class OurClass:

    def __init__(self, a):
        self.our_attribute = a

    @property
    def our_attribute(self):
        return self.__our_attribute

    @our_attribute.setter
    def our_attribute(self, val):
        if val < 0:
            self.__our_attribute = 0
        elif val > 1000:
            self.__our_attribute = 1000
        else:
            self.__our_attribute = val


x = OurClass(10)
print(x.our_attribute)

