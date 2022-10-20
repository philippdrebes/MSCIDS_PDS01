#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Decorators with Parameters
#
# If we don't want or cannot use the "at" decorator syntax, we can do it with
# function calls:


def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


def foo(x):
    print(42)


foo = greeting("καλημερα")(foo)
foo("Hi")
