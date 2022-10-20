#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# More on Modules
#
# Usually, modules contain functions or classes.
#
# There can be "plain" statements in them as well. These statements can be used
# to initialize the module. They are only executed when the module is imported.

# ln -s *_modules-more-01.py fibonacci2.py


def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


print("The module is imported now!")
