#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance
# Polymorphism
#
# Polymorphism is the ability to present the same interface for differing
# underlying forms.
#
# Python is implicitly polymorphic.


def f(x, y):
    return(x * y)


if __name__ == "__main__":
    print("1)", f(42, 43))
    print("2)", f(42, 43.7))
    print("3)", f(42.3, 43))
    print("4)", f(42.0, 43.9))
    print("5)", f("foo", 4))
