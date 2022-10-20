# 02_TypeAnnotatoins_mit_mypy.py
# -*- coding: latin-1 -*-
# from Python 3.6 with type annotation:
# module: mypy

def f(x: int, y: str) -> str:
    return x * y

# print(f(3, 4))
# print(f(3.69, 11.39))


print(f(25, "-"))
# print(f("-", 25))


# As of Python 3.6, variables can also be "typed"
# this is a "letter of intent" and during the
# Runtime can also violate this planning again
# at least up to Python 3.9 ...
# This may change in the future!?

x: int
x = 42

y: int = 17

print("x:", x)
print("isinstance(x, int):", isinstance(x, int))

print("y:", y)
print("isinstance(y, int):", isinstance(y, int))

# deliberate violation of type declaration:
x = "Hallo"

print("x:", x)
print("isinstance(x, int):", isinstance(x, int))
# output: Incompatible types in assignment (expression has type "str", variable has type "int") (35:1)
