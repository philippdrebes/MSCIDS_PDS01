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

TRACE = True


def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0

    if TRACE: print("Starting while ...")
    while True:
        if (counter > n):
            if TRACE: print("now return")
            return

        if TRACE: print(f"yield a: {a}")
        yield a
        if TRACE: print("yield done")
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
for x in f:
    print(f"({x}) ", end="")

print()
