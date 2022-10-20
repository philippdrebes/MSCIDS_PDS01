#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# A More Complex Package
#
# It is also possible to automatically import the package formats, when we are
# importing the effects package.
#
# sound_04/effects/__init__.py
#   from .. import formats
#

import sound_04

print(1, dir())
print(2, dir(sound_04))

# Question: How can we call a function inside the effects-package?
###########################################
# from sound_04.formats import aiffread
# from sound_04.effects import echo
# echo.func1()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_04.formats package is getting imported!
# sound_04.effects package is getting imported!
# sound_04 package is getting imported!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#    '__loader__', '__name__', '__package__', '__spec__', 'sound_04']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#    '__package__', '__path__', '__spec__', 'effects', 'formats']


# comment out code above...
# Module aiffread.py has been loaded!
# Module echo.py has been loaded!
# Funktion func1 has been called!
