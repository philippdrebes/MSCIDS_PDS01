#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_lambda.php
#
# Lambda, filter, reduce and map
# Mapping a List of Functions
#
# The map function of the previous chapter was used to apply one function to
# one or more iterables. We will now write a function which applies a bunch of
# functions, which may be an iterable such as a list or a tuple, for example,
# to one Python object.
#

from math import sin, cos, tan, pi


family_of_functions = (sin, cos, tan)


# ~~~~~~~~~~~~~~~~~~~~
def map_functions(x, functions):
    """ map an iterable of functions on the the object x """
    res = []
    for func in functions:
        res.append(func(x))
    return res


print("1)", map_functions(pi, family_of_functions))


# ~~~~~~~~~~~~~~~~~~~~
# same with lambda
l1 = list(map(lambda f: f(pi), family_of_functions))
print("2)", l1)


# ~~~~~~~~~~~~~~~~~~~~
# same with list comprehension 1
def map_functions_lc(x, functions):
    return [func(x) for func in functions]


print("3)", map_functions_lc(pi, family_of_functions))


# ~~~~~~~~~~~~~~~~~~~~
# same with list comprehension 2
l1 = [func(pi) for func in family_of_functions]
print("4)", l1)
