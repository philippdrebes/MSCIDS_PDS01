#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# First-class Everything
# run in python shell

x = 42
print(x)
print(type(x))

# mae
print(id(x))

x = 42
x
type(x)
print(id(x))


print("*"* 60)
# "One of my goals for Python was to make it
# so that all objects were "first class.
#
# more examples
# run in python

y = 4.34
print(y)
type(y)

def f(x):
    return x + 1

type(f)

import math
type(math)


# e.g list class

x = [3, 6, 9]
y = [45, "abc"]
print(x[1])
x[1] = 99
x.append(42)
x

y
last = y.pop()
print(last)
y

# The variables x and y of the previous example denote two instances
# of the list class. In simplified terms, we have said so far that
# "x and y are lists"
