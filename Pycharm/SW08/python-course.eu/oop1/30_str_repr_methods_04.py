#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# if a class has only the __repr__ method and no __str__ method,
# __repr__ will be applied in the situations, where __str__would
# be applied, if it were available:


class A:
    def __repr__(self):                     # immer winn __repr__ vorhanden ist, dann wird repr() ausgeführt
                                            # und auch zusätzlich __str__()
        return "42"


a = A()
print(a)
print(repr(a))
print(str(a))


# * __str__ is always the right choice, if the output should be for the end user
#   or in other words, if it should be nicely printed
# * __repr__ on the other hand is used for the internal representation of an
#   object
