#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis

# Type Hints / Type Annotations
# Variables

# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
#
# type inference is not used in dynamically typed functions (those without a
# function type annotation) — every local variable type defaults to Any in such
# functions.
#


def example01():
    a: int
    a = 42
    a = "foo"
    print(f"01) a: {a}")


def example02() -> None:
    a: int = 42
    a = "foo"

    b: float = 24
    b = 24.24

    print(f"02) a: {a}")
    print(f"02) b: {b}")


# mypy --check-untyped-defs
# mypy --strict
# mymy --help
def example03():
    c = 42
    c = "foo"
    print(f"03) c: {c}")


if __name__ == "__main__":
    d: int = 42
    # d = "foo"
    print(f"00) d: {d}")

    example01()
    example02()
    example03()
