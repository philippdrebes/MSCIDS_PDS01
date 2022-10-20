#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance
# super and MRO
#
# In which order the base classes are browsed through?
# => Defined by "Method Resolution Order" (MRO)


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")
        super().m()


class C(A):
    def m(self):
        print("m of C called")
        super().m()


class D(B, C):
    def m(self):
        print("m of D called")
        super().m()
        # A.m(self)


if __name__ == "__main__":
    x = D()
    x.m()
    print(D.__mro__)

# =>
# m of D called
# m of B called
# m of C called
# m of A called
