#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_packages.php

# Packages in Python
# A Simple Example
#
# A package is basically a directory with Python files and a file with the name
# __init__.py.
#
# It's possible to put several modules into a Package.
#
# Packages are a way of structuring Python’s module namespace by using "dotted
# module names". A.B stands for a submodule named B in a package named A.
#
# Two different packages like P1 and P2 can both have modules with the same
# name, let's say A, for example. The submodule A of the package P1 and the
# submodule A of the package P2 can be totally different.
#
# A package is imported like a "normal" module.
#
# First of all, we need a directory. The name of this directory will be the
# name of the package, which we want to create.
#
# simple_package_01/
# ├── a.py
# ├── b.py
# └── __init__.py
#


# import simple_package_01
# we can't access neither "a" nor "b" by solely importing simple_package.

from simple_package_01 import a, b


a.bar()
b.foo()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hello, function 'bar' from module 'a' was called!
# Hello, function 'foo' from module 'b' was called!



# # Rule:
# # import package.modul.func()
#
# # comment the code above and
# # comment out the code below ...                =>  Understood?

# from simple_package_01.a import bar, bar2
# from simple_package_01.b import foo, foo1
#
# bar()
# foo()


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hello, function 'bar' from module 'a' was called!
# Hello, function 'foo' from module 'b' was called!
# Hello, function 'bar2' from modul 'a' was called!
# Hello, function 'foo1' from module 'b' was called!
