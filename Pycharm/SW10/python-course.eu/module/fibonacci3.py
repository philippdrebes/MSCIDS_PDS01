#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# More on Modules
# Executing Modules as Scripts
#
# Usually, modules contain functions or classes.
#
# There can be "plain" statements in them as well. These statements can be used
# to initialize the module. They are only executed when the module is imported.

# ln -s *_modules-more-03.py fibonacci3.py


def fib3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib3(n-1) + fib3(n-2)


if __name__ == "__main__":
    print("The module is imported now!")

# run this (PyCharm or cli)
# python3 fibonacci3.py
