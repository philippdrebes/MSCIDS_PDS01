#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Attributes

# Binding attributes to objects is a general concept in Python.
# Even function names can be attributed.


def f(x):
    return 42


f.x = 21
print(f.x)

print(f(21))


# This can be used as a replacement for the static function
# variables of C and C++, which are not possible in Python.


def f(x):
    f.counter = getattr(f, "counter", 0) + 1   # zählen wir oft eine funktion aufgerufen wird
    return "Monty Python"


for i in range(3):
    print(f(i))

print(f.counter)
