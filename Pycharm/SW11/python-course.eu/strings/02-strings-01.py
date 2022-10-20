#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_formatted_output.php
#
# Formatted Output
# Other string methods for Formatting
#
# https://docs.python.org/3/library/string.html#formatspec
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    s = "Python"
    s1 = s.center(10)
    print(s1)

    s1 = s.center(10, "*")
    print(s1)


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    s = "Training"
    s1 = s.ljust(12)
    print(s1)

    s1 = s.ljust(12, ":")
    print(s1)


def example03():
    ex = "example03"
    print("\n", ex, "-" * len(ex), sep="\n")

    s = "Programming"
    s1 = s.rjust(15)
    print(s1)

    s1 = s.rjust(15, "~")
    print(s1)


def example04():
    ex = "example04"
    print("\n", ex, "-" * len(ex), sep="\n")

    account_number = "43447879"
    a1 = account_number.zfill(12)
    print(account_number)
    print(a1)


if __name__ == "__main__":
    example01()
    example02()
    example03()
    example04()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example01
# ---------
#   Python
# **Python**
#
#
# example02
# ---------
# Training
# Training::::
#
#
# example03
# ---------
#     Programming
# ~~~~Programming
#
#
# example04
# ---------
# 43447879
# 000043447879

