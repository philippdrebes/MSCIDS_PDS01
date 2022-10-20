#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# Importing a Complete Package
#
# Python provides a mechanism to give an explicit index of the subpackages and
# modules of a packages, which should be imported.
#
# __all__ is taken as the list of module and package names to be imported when
# from package import * is encountered.
#
# sound_11/__init__.py
#   __all__ = ["formats", "filters", "effects", "foobar"]
#

from sound_11 import *

print(1, dir())
print(2, dir(foobar))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound package is getting imported!
# formats package is getting imported!
# filters package is getting imported!
# effects package is getting imported!
# The module foobar is getting imported
#
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'effects', 'filters',
# 'foobar', 'formats']
#
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'foo']
