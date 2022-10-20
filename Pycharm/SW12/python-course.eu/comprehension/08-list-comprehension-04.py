#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_list_comprehension.php
#
# List Comprehension
# Generator Comprehension
#
# The syntax and the way of working is like list comprehension, but a generator
# comprehension returns a generator instead of a list.
# (upcoming https://www.python-course.eu/python3_generators.php)
#


x = (x ** 2 for x in range(20))

print(x)

y = list(x)
print(y)
