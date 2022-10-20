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

from sound_11.effects import echo
from sound_11 import foobar


print(1, dir())
print(2, dir(foobar))

echo.func1()
foobar.foo()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_11 package is getting imported!
# sound_11.effects package is getting imported!
# Module echo.py has been loaded!
# The module foobar is getting imported
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#   '__loader__', '__name__', '__package__', '__spec__', 'echo', 'foobar']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__spec__', 'foo']
# Funktion func1 has been called!
# I am 'foo()' in  module 'foobar'

