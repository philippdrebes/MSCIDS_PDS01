#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Decorators with Parameters
#
# These two decorators are nearly the same, except for the greeting.
#


def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper


def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper


@evening_greeting
def foo(x):
    print(42)


foo("Hi")
