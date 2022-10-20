#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Classes instead of Functions
# Using a Class as a Decorator
#


def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper


@decorator1
def foo1():
    print("inside foo1()")


foo1()


# The following decorator implemented as a class does the same "job":
class decorator2:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()


@decorator2
def foo2():
    print("inside foo2()")


foo2()
