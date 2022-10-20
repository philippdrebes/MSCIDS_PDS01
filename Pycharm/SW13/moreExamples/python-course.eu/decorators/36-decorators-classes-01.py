#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Classes instead of Functions
#
# A decorator is simply a callable object that takes a function as an input
# parameter.
#
# A callable object is an object which can be used and behaves like a function
# but might not be a function. It is possible to define classes in a way that
# the instances will be callable objects. The __call__ method is called, if the
# instance is called "like a function", i.e. using brackets.
#


class A:

    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)


x = A()
print("now calling the instance:")
x(3, 4, x=11, y=10)
print("Let's call it again:")
x(3, 4, x=11, y=10)
