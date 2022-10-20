#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Decorators with Parameters
#
# We want to add a parameter to the decorator to be capable of customizing the
# greeting, when we do the decoration. We have to wrap another function around
# our previous decorator function to accomplish this. We can now easy say "Good
# Morning" in the Greek way:
#


def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


@greeting("καλημερα")
def foo(x):
    print(42)


foo("Hi")
