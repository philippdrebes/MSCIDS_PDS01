#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# Importing Modules
#
# If only certain objects of a module are needed, we can import only those.
# The other objects, e.g. cos, are not available after this import.
# Prefix math not allowed (=> pi not math.pi)

from math import sin, pi

# https://docs.python.org/3/library/math.html


print("1)", pi)
print("2)", sin(pi/2))

# print(math.pi)
# print(math.cos(math.pi/2))
