#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# A More Complex Package
#
# If you also want to use the package effects, you have to import it explicitly
# with import sound.effects.
#
# sound_02/__init__.py
#   import sound_02.effects
#

import sound_02.effects

print(1, dir())
print(2, dir(sound_02))
print(3, dir(sound_02.effects))
print(4, sound_02.effects)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_02.effects package is getting imported!
# sound_02 package is getting imported!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#   '__loader__', '__name__', '__package__', '__spec__', 'sound_02']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
#   '__name__', '__package__', '__path__', '__spec__', 'effects', 'sound_02']
# 3 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__path__', '__spec__']
# 4 <module 'sound_02.effects' from 'C:\\Users\\Erwin Mathis\\switchdrive\\SyncVM
#   \\PDS_F22\\Pycharm\\SW11\\python-course.eu\\packages\\sound_02\\effects\\__init__.py'>
