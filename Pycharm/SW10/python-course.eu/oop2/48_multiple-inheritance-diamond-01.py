#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance
# The Diamond Problem or the 'deadly diamond of death'

# Generally used term for an ambiguity that arises when two classes B and C
# inherit from a superclass A, and another class D inherits from both B and
# C.
#
# If there is a method "m" in A that B or C has overridden, and furthermore, if
# does not override this method, then the question is which version of the
# method does D inherit? It could be the one from A, B or C
#
#            +---+
#     ------>| A |<------
#     |      +---+      |
#     |                 |
#   +---+             +---+
#   | B |             | C |
#   +---+             +---+
#     ^                 ^
#     |      +---+      |
#     -------| D |-------
#            +---+
#


class A:
    def m(self): print("m of A called")
    pass


class B(A):
    # def m(self): print("m of B called")
    pass


class C(A):
    def m(self): print("m of C called")
    pass


class D(B, C):
    # def m(self): print("m of D called")
    pass


x = D()
x.m()
print(D.__mro__)
