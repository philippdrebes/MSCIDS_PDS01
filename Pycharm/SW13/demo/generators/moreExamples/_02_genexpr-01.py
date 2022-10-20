#!/usr/bin/env python3
# 2020-05, Bruno Grossniklaus, https://github.com/it-gro
#
# https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
# https://docs.python.org/3/library/sys.html#sys.stdin
#
# ./_02_genexpr-01.py < sortme2.txt
# python.exe _02_genexpr-01.py < sortme2.txt
#
# ping -c 5  google.com | ./_02_genexpr-01.py
# ping.exe   google.com | python.exe _02_genexpr-01.py
#

import sys


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-)
    for line in sys.stdin:
        data = len(line)
        print(data)


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-(
    lines = list(sys.stdin)
    print("lines: ", lines)
    data = list(map(lambda l: len(l), lines))
    print(data)


def example10():
    ex = "example10"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-(
    data = [
        len(line)
        for lines in sys.stdin
        for line in lines.splitlines(True)
    ]
    print(data)


def example11():
    ex = "example11"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-)
    data = (
        len(line)
        for lines in sys.stdin
        for line in lines.splitlines(True)
    )
    for d in data:
        print(d)


if __name__ == "__main__":
    # example01()
    # example02()
    # example10()
    example11()
