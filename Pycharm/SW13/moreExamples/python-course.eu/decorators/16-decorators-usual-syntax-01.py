#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Usual Syntax for Decorators in Python
#
# The decoration in Python is usually not performed in the way we did it in our
# previous example.
#


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))


foo("Hi")
