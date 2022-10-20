#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# Importing a Complete Package
#
# sound_12/effects/__init__.py
#   __all__ = ["echo", "surround", "reverse"]
#

from sound_12.effects import *

print(1, dir())
print(2, dir(surround))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_12 package is getting imported!
# sound_12.effects package is getting imported!
# Module echo.py has been loaded!
# Module surround.py has been loaded!
# Module reverse.py has been loaded!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
#    '__name__', '__package__', '__spec__', 'echo', 'reverse', 'surround']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#    '__package__', '__spec__', 'func1', 'func2', 'func3']


# Result:
# The recommended way is to import specific modules from a package instead of
# using *.
