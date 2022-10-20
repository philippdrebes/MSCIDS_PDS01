#!/usr/bin/env python3
# 2020-05
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Functions as Parameters
#
# You may not be satisfied with the output. 'f' should write that it calls 'g'
# and not 'func'. Of course, we need to know what the 'real' name of func
# is. For this purpos, we can use the attribute __name__, as it contains this
# name:


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")


def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__)


f(g)
