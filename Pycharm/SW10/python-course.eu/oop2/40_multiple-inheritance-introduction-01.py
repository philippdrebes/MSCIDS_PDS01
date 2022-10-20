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
