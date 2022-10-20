#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# quick side-trip


#mae  (https://www.geeksforgeeks.org/str-vs-repr-in-python/)

# str() is used for creating output for end user while repr() is mainly used for debugging and development.
# repr’s goal is to be unambiguous and str’s is to be readable. For example,
# if we suspect a float has a small rounding error, repr will show us while str may not.

# repr() compute the “official” string representation of an object (a representation that has
# all information about the object) and str() is used to compute the “informal” string representation
# of an object (a representation that is useful for printing the object).

# The print statement and str() built-in function uses __str__ to display the string representation
# of the object while the repr() built-in function uses __repr__ to display the object.



li = ["Python", "Java", "C++", "Perl"]
print("1)", li,       type(li))
print("2)", str(li),  type(str(li)))
print("3)", repr(li), type(repr(li)))

d = {"a": 3497, "b": 8011, "c": 8300}
print("4)",      d,  type(d))
print("5)",  str(d), type(str(d)))
print("6)", repr(d), type(repr(d)))

x = 587.78
print("7)", str(x),  type(str(x)))
print("8)", repr(x), type(repr(x)))
