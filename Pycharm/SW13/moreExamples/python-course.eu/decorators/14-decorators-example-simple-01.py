#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# A Simple Decorator
#
# After the decoration "foo = our_decorator(foo)", foo is a reference to the
# 'function_wrapper'. 'foo' will be called inside of 'function_wrapper', but
# before and after the call some additional code will be executed, i.e. in our
# case two print functions.


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


def foo(x):
    print("Hi, foo has been called with " + str(x))


print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with our_decorator:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)
