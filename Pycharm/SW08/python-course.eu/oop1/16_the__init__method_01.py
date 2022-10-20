#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# The __init__ Method

# We need a mechanism to initialize an instance right after its
# creation. This is the __init__-method

# __init__ is a method which is immediately and automatically
# called after an instance has been created. This name is
# fixed and it is not possible to chose another name.


class A:
    def __init__(self):
        print("__init__ has been executed!")


x = A()             # ein "Initialisator" eines neuen Objekts mit dem namen 'x'  => ruft __init__() auf
