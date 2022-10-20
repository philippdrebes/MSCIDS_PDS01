#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_list_comprehension.php
#
# List Comprehension
# Examples
# The following list comprehension creates the Pythagorean triples:


l1 = [
    (x, y, z)
    for x in range(1, 30)
    for y in range(x, 30)
    for z in range(y, 30)
    if x**2 + y**2 == z**2
]

print(l1)
