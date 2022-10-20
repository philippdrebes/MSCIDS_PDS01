#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# Importing a Complete Package
#
# what happens, if we import the sound package with the star, i.e. from sound
# import
#
# sound_10/effects/__init__.py
#
# Only in sound_10: foobar.py
# sound_10/__init__.py

from sound_10 import *                          # bad style ... but why it don't work???

print(dir())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound package is getting imported!
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__']
#

# Result:
# we see that neither the module foobar nor the subpackages effects, filters
# and formats have been imported!  Wau....!
