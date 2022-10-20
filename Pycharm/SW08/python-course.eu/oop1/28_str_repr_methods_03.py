#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# If a class has a __str__ method, the method will be used for an instance x of
# that class, if either the function str is applied to it or if it is used in a
# print function.
# __str__ will not be used, if repr is called, or if we try to output the value
# directly in an interactive Python shell:


class A:
    def __str__(self):
        return "42"


a = A()
print(a)
print(repr(a))
print(str(a))
