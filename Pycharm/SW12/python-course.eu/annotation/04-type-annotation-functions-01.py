#!/usr/bin/env python3
#

# Type Hints / Type Annotations
# Functions
#
# http://mypy-lang.org/
#
# $ source ~/venv/pds01-3.8/bin/activate
# (pds01-3.8)$ pip3 list
# pip3 install mypy
# mypy foo.py


def greeting(name: str) -> str:
    return 'Hello ' + name


def f(x: str, y: int) -> str:
    return(x * y)


if __name__ == "__main__":
    s1 = greeting("Python")
    print("1)", s1)

    s1 = f("foo", 4)
    print("2)", s1)

    # s1 = f(42, 43)
    # print("3)", s1)

    # i = s1 + 4
    # print("4)", i)
