#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# __str__- and __repr__-Methods

# quick side-trip


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
