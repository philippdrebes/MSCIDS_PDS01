#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# A More Complex Package
#
# sound_01/
# ├── effects
# │   ├── echo.py
# │   ├── __init__.py
# │   ├── reverse.py
# │   └── surround.py
# ├── filters
# │   ├── equalizer.py
# │   ├── __init__.py
# │   ├── karaoke.py
# │   └── vocoder.py
# ├── formats
# │   ├── aiffread.py
# │   ├── aiffwrite.py
# │   ├── auread.py
# │   ├── auwrite.py
# │   ├── __init__.py
# │   ├── wavread.py
# │   └── wavwrite.py
# └── __init__.py
#
# If we import the package "sound" by using the statement import sound, the
# package sound but not the subpackages effects, filters and formats will be
# imported. The reason for this consists in the fact that the file __init__.py
# doesn't contain any code for importing subpackages.
#

import sound_01

print(1, dir())
# sound_01.effects

# print(2, dir(sound_01))         # we don't see any subpackages of 'sound_01!!

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# sound package ' sound_01 ' is getting imported!
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'sound_01']
