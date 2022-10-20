#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance
# Introduction
#
# We have covered inheritance, or more specific "single inheritance". As we
# have seen, a class inherits in this case from one class.
#
# Multiple inheritance on the other hand is a feature in which a class can
# inherit attributes and methods from more than one parent class.
#
# A class definition, where a child class SubClassName inherits from the parent
# classes BaseClass1, BaseClass2, BaseClass3, and so on, looks like this:


import inspect

class BaseClass1:
    pass


class BaseClass2:
    pass


class BaseClass3:
    pass


class SubclassName(BaseClass1, BaseClass2, BaseClass3):
    pass


b2 = BaseClass2()
s = SubclassName()

print("1: b2:", b2)
print("2: s:", s)

print("3: Base-classes for BaseClass2 are: " ,inspect.getmro(BaseClass2) )
print("4: Base-classes for SubclassName are: " ,inspect.getmro(SubclassName) )

# dito (gleiche Ausgabe ... ohne import inspect!
print("5: Base-classes for BaseClass2 are: " , BaseClass2.__mro__)
print("6: Base-classes for SubclassName are: " , SubclassName.__mro__)


# 1: b2: <__main__.BaseClass2 object at 0x7f0071e96040>
# 2: s: <__main__.SubclassName object at 0x7f0071e96070>
# 3: Base-classes for BaseClass2 are:  (<class '__main__.BaseClass2'>, <class 'object'>)
# 4: Base-classes for SubclassName are:  (<class '__main__.SubclassName'>, <class '__main__.BaseClass1'>, <class '__main__.BaseClass2'>, <class '__main__.BaseClass3'>, <class 'object'>)