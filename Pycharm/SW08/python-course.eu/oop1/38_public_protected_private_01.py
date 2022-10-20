#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Public- Protected- and Private Attributes

# Attribute types
# Naming Type      Meaning
# name   Public    These attributes can be freely used inside or
#                  outside of a class definition
# _name  Protected Protected attributes should not be used outside
#                  of the class definition, unless inside of a
#                  subclass definition.
# __name  Private  This kind of attribute is inaccessible and
#                  invisible. It's neither possible to read nor
#                  write to those attributes, except inside of
#                  the class definition itself.


class A():

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


a = A()
print("1)", a.__dict__)
print("2)", a.pub)
print("3)", a._prot)
# print("4)", a._priv)
print("4)", a._A__priv)   # don't do it
