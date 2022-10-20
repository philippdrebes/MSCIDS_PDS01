#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Functions as Parameters
#
# Another example:
#

import math


def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res


print(foo(math.sin))
print(foo(math.cos))
