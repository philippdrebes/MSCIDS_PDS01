#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# Importing Modules
#
# It's possible to import more than one module in one import statement. In this
# case the module names are separated by commas.
#
# import statements can be positioned anywhere in the program, but it's good
# style to place them directly at the beginning of a program
#
# https://www.python.org/dev/peps/pep-0008/#imports
# https://www.flake8rules.com/rules/E401.html


import math, random       # more than on import per line is bad style

# https://docs.python.org/3/library/random.html

random.seed()

print(math.pi)
print(random.randint(1, 42))
