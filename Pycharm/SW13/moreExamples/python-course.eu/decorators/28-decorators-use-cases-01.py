#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Use Cases for Decorators
#
# Counting Function Calls with Decorators
#
# Use the *args and **kwargs notation to write decorators which can cope with
# functions with an arbitrary number of positional and keyword parameters.
#


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper


@call_counter
def succ(x):
    return x + 1


@call_counter
def mul1(x, y=1):
    return x*y + 1


print(succ.calls)
for i in range(10):
    succ(i)
mul1(3, 4)
mul1(4)
mul1(y=3, x=2)

print(succ.calls)
print(mul1.calls)
