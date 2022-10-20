#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# A More Complex Package
#
# Instead of using an absolute path we could have imported the effects-package
# relative to the sound package
#
# sound_03/__init__.py
#   from . import effects
#

import sound_03

print(1, dir())
print(2, dir(sound_03))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_03.effects package is getting imported!
# sound_03 package is getting imported!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#    '__loader__', '__name__', '__package__', '__spec__', 'sound_03']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__path__', '__spec__', 'effects']
