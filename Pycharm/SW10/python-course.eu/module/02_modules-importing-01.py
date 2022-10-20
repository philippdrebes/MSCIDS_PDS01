#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_modules_and_modular_programming.php

# Modular Programming and Modules
# Importing Modules
#
# Modular design means that a complex system is broken down into smaller parts
# or components, i.e. modules. These components can be independently created
# and tested. In many cases, they can be even used in other systems as well.
#
# Modular programming is a software design technique to split your code into
# separate parts. These parts are called modules. The focus for this separation
# should be to have modules with no or just few dependencies upon other
# modules. In other words: Minimization of dependencies is the goal.
#
# When creating a modular system, several modules are built separately and more
# or less independently. The executable application will be created by putting
# them together.
#
# Every file, which has the file extension .py and consists of proper Python
# code, can be seen or is a module! There is no special syntax required to make
# such a file a module.
#
# There are different ways to import a modules.

import math

# https://docs.python.org/3/library/math.html

# Every attribute or function can only be accessed by putting "math." in front
# of the name.

print("1)", math.pi)
print("2)", math.sin(math.pi/2))
print("3)", math.cos(math.pi/2))
print("4)", math.cos(math.pi))
