#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# A More Complex Package
#
# Your task:
# 1. if the package 'effects' is loaded then
#    - also (allways!)  the 'formats' package has to be loaded AND
#    - also (allways!) the 'karaoke'-module from the package 'filers'
#    (we don't discuss why - our boss wants it that way ....;-)!
# 2. on the end of your work: test your solution with the call of function:
#    sound_05.filters.karaoke.func1()
# => change the different __init_.py-files so that you get a correct solution!

# sound_05/effects/__init__.py
#   from ..filters import karaoke
#

import sound_05_Solution

print(1, dir())
print(2, dir(sound_05_Solution))

sound_05_Solution.filters.karaoke.func1()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_05_Solution.formats package is getting imported!
# sound_05_Solution.filters package is getting imported!
# Module karaoke.py has been loaded!
# sound_05_Solution.effects package is getting imported!
# sound_05_Solution package is getting imported!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#   '__loader__', '__name__', '__package__', '__spec__', 'sound_05_Solution']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__path__', '__spec__', 'effects', 'filters', 'formats']

# Result:
# Funktion func1 has been called!
