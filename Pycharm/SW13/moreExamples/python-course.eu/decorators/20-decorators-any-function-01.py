#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Usual Syntax for Decorators in Python
#
# It is also possible to decorate third party functions, e.g. functions we
# import from a module. We can't use the Python syntax with the "at" sign in
# this case:
#

from math import sin, cos


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper


sin = our_decorator(sin)
cos = our_decorator(cos)


for f in [sin, cos]:
    f(3.1415)
