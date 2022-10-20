#!/usr/bin/env python3
#

# Type Hints / Type Annotations
#
# https://docs.python.org/3/library/typing.html
#   https://docs.python.org/3/library/typing.html#typing.Any
#   https://docs.python.org/3/library/typing.html#type-aliases
#
# A type alias is defined by assigning the type to the alias. In this example,
# Vector and List[float] will be treated as interchangeable synonyms


import typing
Vector = typing.List[float]


def add(x: typing.Any) -> typing.Any:
    return x + x


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]  # list comprehension


if __name__ == "__main__":
    print("1)", add(42), add("42"), add([42]))

    # typechecks; a list of floats qualifies as a Vector.
    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    print("2)", new_vector)

    # new_vector = scale(2.0, [1.0, -4.2, "42"])
    # print("3)", new_vector)
