#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# Importing Modules
# Renaming a Namespace
#
# It's also possible to import everything in the namespace of the importing
# module.
#
# A way to shrink the typing effort consists in renaming a namespace.

import math as m

print("1)", m.pi)
print("2)", m.sin(m.pi/2))
