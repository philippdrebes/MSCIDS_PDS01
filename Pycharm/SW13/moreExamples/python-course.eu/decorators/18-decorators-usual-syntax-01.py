#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Usual Syntax for Decorators in Python
#
# We can decorate every other function which takes one parameter with our
# decorator 'our_decorator'.


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def succ(n):
    return n + 1


succ(10)
