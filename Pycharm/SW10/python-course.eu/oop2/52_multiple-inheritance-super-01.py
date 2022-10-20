#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance
# super and MRO
#
# The super function is often used when instances are initialized with the
# __init__ method:


class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()


if __name__ == "__main__":
    print("1)", "~" * 10)
    print(D.__mro__)
    d = D()

    print("2)", "~" * 10)
    c = C()

    print("3)", "~" * 10)
    b = B()

    print("4)", "~" * 10)
    a = A()

# =>
# 1) ~~~~~~~~~~
# D.__init__
# B.__init__
# C.__init__
# A.__init__
# 2) ~~~~~~~~~~
# C.__init__
# A.__init__
# 3) ~~~~~~~~~~
# B.__init__
# A.__init__
# 4) ~~~~~~~~~~
# A.__init__
