#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/tutorial/datastructures.html#sets
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(type(a))
    print(a)


def example10():
    ex = "example10"
    print("\n", ex, "-" * len(ex), sep="\n")

    d1 = {x: x**2 for x in (2, 4, 6)}
    print(type(d1))
    print(d1)


def example20():
    ex = "example20"
    print("\n", ex, "-" * len(ex), sep="\n")

    line_list = ['  line 1\n', 'line 2  \n', 'line 3  \n']

    # List comprehension -- returns list
    stripped_list = [line.strip() for line in line_list]
    print("stripped_list", type(stripped_list), stripped_list)

    # Generator expression -- returns iterator
    # upcoming ...
    stripped_iter = (line.strip() for line in line_list)
    print("stripped_iter", type(stripped_iter), stripped_iter)

    for elem in stripped_iter:
        print(elem)

    # https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Generator expressions return an iterator that computes the values as
    # necessary, not needing to materialize all the values at once.
    # This means that list comprehensions aren’t useful if you’re working with
    # iterators that return an infinite stream or a very large amount of data.


if __name__ == "__main__":
    example01()
    example10()
    example20()
