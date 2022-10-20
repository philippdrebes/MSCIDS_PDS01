#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance
# Polymorphism
#
# Polymorphism is the ability to present the same interface for differing
# underlying forms.
#
# Python is implicitly polymorphic. We can apply our previously defined
# function f even to lists, strings or other types, which can be printed


def f(x, y):
    print("values: ", x, y)


if __name__ == "__main__":
    f(42, 43)
    f(42, 43.7)
    f(42.3, 43)
    f(42.0, 43.9)

    f([3, 5, 6], (3, 5))
    f("A String", ("A tuple", "with Strings"))
    f({2, 3, 9}, {"a": 3.4, "b": 7.8, "c": 9.04})
