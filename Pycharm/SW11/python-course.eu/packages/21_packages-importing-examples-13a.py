#!/usr/bin/env python3
#  Bruno Grossniklaus, Erwin Mathis

# Packages in Python
# cherry picking
#
# sound_13/effects/__init__.py
#   from . import reverse
# sound_13/filters/__init__.py
#   from . import equalizer


import sound_13.effects.surround

print(1, dir())
print(2, dir(sound_13))
print(3, dir(sound_13.effects))
print(4, dir(sound_13.effects.surround))

sound_13.effects.surround.func1()
sound_13.effects.reverse.func2()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_13 package is getting imported!
# Module reverse.py has been loaded!
# sound_13.effects package is getting imported!
# Module surround.py has been loaded!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sound_13']
# 2 ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'effects']
# 3 ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'reverse', 'surround']
# 4 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'func1', 'func2', 'func3']
# Funktion func1 has been called!
# Funktion func2 has been called!
