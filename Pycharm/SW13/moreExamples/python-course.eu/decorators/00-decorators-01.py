#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Introduction
#
# Decorators belong most probably to the most beautiful and most powerful
# design possibilities in Python, but at the same time the concept is
# considered by many as complicated to get into. To be precise, the usage of
# decorators is very easy, but writing decorators can be complicated,
# especially if you are not experienced with decorators and some functional
# programming concepts.
#
# A decorator in Python is any callable Python object that is used to modify a
# function or a class. A reference to a function "func" or a class "C" is
# passed to a decorator and the decorator returns a modified function or
# class. The modified functions or classes usually contain calls to the
# original function "func" or class "C".
#
# First Steps to Decorators
#
# We introduce decorators by repeating some important aspects of
# functions. First you have to know or remember that function names are
# references to functions and that we can assign multiple names to the same
# function:
#
#


def succ(x):
    return x + 1


successor = succ
print(successor(10))
print(succ(10))

# We can delete either "succ" or "successor" without deleting the function
# itself.
del succ
print(successor(10))
