#!/usr/bin/env python3
#

# Packages in Python
#
# When a module named spam is imported, the interpreter first searches for a
# built-in module with that name. If not found, it then searches for a file
# named spam.py in a list of directories given by the variable
# sys.path. sys.path is initialized from these locations:
#
#  The directory containing the input script (or the current directory when no
#  file is specified).
#
#  PYTHONPATH (a list of directory names, with the same syntax as the shell
#  variable PATH).
#
#  The installation-dependent default.
#
# https://docs.python.org/3/tutorial/modules.html#the-module-search-path
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
#

import os
print(os.getenv('PYTHONPATH'))



# in my environment:
# C:\Users\Erwin Mathis\switchdrive\SyncVM;
# C:\Users\Erwin Mathis\switchdrive\SyncVM\PDS_F22\Pycharm\SW11\UnitTests;
# C:\Program Files\JetBrains\PyCharm 2020.2.4\plugins\python\helpers\pycharm_matplotlib_backend;
# C:\Program Files\JetBrains\PyCharm 2020.2.4\plugins\python\helpers\pycharm_display
