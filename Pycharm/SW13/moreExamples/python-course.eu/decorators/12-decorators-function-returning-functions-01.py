#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Functions returning Functions
#
# Functions can return references to function objects.
#


def f(x):
    def g(y):
        return y + x + 3
    return g


nf1 = f(x=1)
nf2 = f(3)


print(nf1(1))
print(nf2(y=1))
