#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
# Method of Operation
#
# Generators offer a comfortable method to generate iterators, and that's why
# they are called generators.
#


def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0

    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
for x in f:
    print(x, " ", end="")

print()

for x in fibonacci(5):
    print(x, " ", end="")

print()
