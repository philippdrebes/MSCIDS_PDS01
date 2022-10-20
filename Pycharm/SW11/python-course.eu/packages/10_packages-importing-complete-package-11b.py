#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# Importing a Complete Package
#
# what will be imported, if we use * in a subpackage  (e.g. sound_11.effects)
#

from sound_11.effects import *

print(dir())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound package is getting imported!
# effects package is getting imported!
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__']
#

# Result:
# The modules inside of effects have not been imported automatically.
