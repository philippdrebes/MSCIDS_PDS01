#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_descriptors.php
#
# Descriptors
# Descriptor Protocol
#
# The general descriptor protocol consists of three methods:
# descr.__get__(self, obj, type=None) -> value
# descr.__set__(self, obj, value) -> None
# descr.__delete__(self, obj) -> None
#
# If you define one or more of these methods, you will have created a
# descriptor.


class SimpleDescriptor(object):
    """
    A simple data descriptor that can set and return values
    """

    def __init__(self, initval=None):
        print("__init__ of SimpleDecorator called with initval: ", initval)
        self.__set__(self, initval)

    def __get__(self, instance, owner):
        print(instance, owner)
        print('Getting (Retrieving) self.val: ', self.val)
        return self.val

    def __set__(self, instance, value):
        print('Setting self.val to ', value)
        self.val = value


class MyClass(object):

    x = SimpleDescriptor("green")


m = MyClass()
print(m.x)
m.x = "yellow"
print(m.x)
