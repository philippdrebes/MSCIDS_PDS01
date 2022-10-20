#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
# https://docs.python.org/3/library/functions.html#map
# https://docs.python.org/3/library/functions.html#filter


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    r = range(10, 20, 2)
    l1 = list(map(lambda x: [x, x / 2, x * 2, x ** 2], r))
    print(l1)

    l2 = list(map(lambda x: [x[0], x[3]], l1))
    print(l2)

    l3 = list(map(lambda x: {x[0]: x[3]}, l1))
    print(l3)

    l4 = list(map(lambda x: (x[0], x[3]), l1))
    print(l4)


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    r = range(10, 20, 2)
    l1 = list(map(lambda x: [x, x / 2, x * 2, x ** 2], r))

    d1 = dict(map(lambda x: (x[0], x[3]), l1))
    print(d1)


def example10():
    ex = "example10"
    print("\n", ex, "-" * len(ex), sep="\n")

    r = range(10, 30, 2)
    l1 = list(filter(lambda x: x % 3 == 0, r))
    print(l1)


def example11():
    ex = "example11"
    print("\n", ex, "-" * len(ex), sep="\n")

    lorem = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
    diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
    sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
    rebum. Stet clita gubergren, no sea takimata sanctus est Lorem ipsum dolor
    sit amet.  """

    l1 = list(filter(lambda t: t[0] == "a", lorem.strip().split()))
    print(l1)


if __name__ == "__main__":
    example01()
    example02()
    example10()
    example11()
