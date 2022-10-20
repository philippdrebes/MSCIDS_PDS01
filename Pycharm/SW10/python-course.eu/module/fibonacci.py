#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# Designing and Writing Modules
#
# A Module is just a file containing Python definitions and statements. The
# module name is moulded out of the file name by removing the suffix .py.
#
# ln -s *_modules-writing-modules-01.py fibonacci.py


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def ifib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
