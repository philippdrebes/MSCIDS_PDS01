#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
# Using a 'return' in a Generator
#
# A return statement inside of a generator is equivalent to raise
# StopIteration()
#


def gen():
    yield 1
    raise StopIteration(42)
    # return 42


g = gen()
next(g)

next(g)
