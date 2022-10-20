#!/usr/bin/env python3
#
#
# Packages in Python
# cherry picking


import sound_13.effects.surround as sound_surround

print(1, dir())
print(2, dir(sound_surround))

sound_surround.func1()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_13 package is getting imported!
# Module reverse.py has been loaded!
# sound_13.effects package is getting imported!
# Module surround.py has been loaded!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sound_surround']
# 2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'func1', 'func2', 'func3']
# Funktion func1 has been called!
