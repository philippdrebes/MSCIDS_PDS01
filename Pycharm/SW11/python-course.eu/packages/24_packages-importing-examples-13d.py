#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# Packages in Python
# cherry picking


from sound_13 import effects as e, filters as f

print(1, dir())
print(2, dir(e))
print(3, dir(f))

e.reverse.func1()
f.equalizer.func1()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound_13 package is getting imported!
# Module reverse.py has been loaded!
# sound_13.effects package is getting imported!
# Module equalizer.py has been loaded!
# sound_13.filters package is getting imported!
# 1 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'e', 'f']
# 2 ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'reverse']
# 3 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'equalizer']
# Funktion func1 has been called!
# Funktion func1 has been called!
