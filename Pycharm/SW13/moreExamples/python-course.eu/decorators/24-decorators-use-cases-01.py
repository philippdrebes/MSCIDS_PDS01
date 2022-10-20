#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Use Cases for Decorators
#
# Summarizing we can say that a decorator in Python is a callable Python object
# that is used to modify a function, method or class definition. The original
# object, the one which is going to be modified, is passed to a decorator as an
# argument. The decorator returns a modified object, e.g. a modified function,
# which is bound to the name used in the definition.
#
#
# Checking Arguments with a Decorator


def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an positve integer")
    return helper


@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(1, 10):
    print(i, factorial(i))

print(factorial(-1))
