#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# A Minimal Class in Python
#
# We will design and use a robot class in Python as an example to
# demonstrate the most important terms and ideas of object
# orientation.
# We will start with the simplest class in Python.

class Robot:
    pass

# The body of a class consists of an indented block of
# statements.

# A class object is created, when the definition is left normally,
# i.e. via the end.
# This is basically a wrapper around the contents of the namespace
# created by the class definition.


if __name__ == "__main__":
    x = Robot()          # der Befehl ein Roboter-Objekt zu erstellen. x zeigt auf dieses Objekt!

    print (x.__dict__)

    y = Robot()
    print (y.__dict__)
    y2 = y                 # y ist ein "Wegweiser" (Pointer) und er Inhalt dieses Pointes wird auf
                        #  den Wegweiser y2 kopiert!!
    print(y == y2)
    print(y == x)

    print(type(Robot))     # Wau: Der typ einer Klasse ist 'type'!!!!!  siehe in einer Woche!
    print(type(x))

# mae
#   print(dir())
#    print(vars())

# later:
# print(x.__dict__)
# print(y.__dict__)
