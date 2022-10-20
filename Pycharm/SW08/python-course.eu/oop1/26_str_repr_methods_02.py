#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# If you apply str or repr to an object, Python is looking
# for a corresponding method __str__ or __repr__ in the class
# definition of the object. If the method does exist, it will
# be called.


class A:
    pass


a = A()
print(a)
print(repr(a))
print(str(a))

# As both methods are not available, Python uses the default
# output for our object "a".
