#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
# Method of Operation
#
# A Version which is capable of returning an endless iterator.


def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
counter = 0
for x in f:
    print(x, " ", end="")
    counter += 1
    if (counter > 10):
        break

print()
