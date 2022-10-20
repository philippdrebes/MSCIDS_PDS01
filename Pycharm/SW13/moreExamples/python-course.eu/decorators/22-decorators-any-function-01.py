#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Usual Syntax for Decorators in Python
#
# The previous function_wrapper works only for functions with exactly one
# parameter. We provide a generalized version of the function_wrapper, which
# accepts functions with arbitrary parameters in the following example:
#

from random import random, randint, choice


def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper


random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)

random()
randint(3, 8)
choice([4, 5, 6])
