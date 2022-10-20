#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
# https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    def all_the_same_1(limit):
        squares = []
        for x in range(limit):
            squares.append(x**2)
        return squares

    def all_the_same_2(limit):
        return list(map(lambda x: x**2, range(limit)))

    def all_the_same_3(limit):
        return [x**2 for x in range(limit)]

    print("1) ", all_the_same_1(10))
    print("2) ", all_the_same_2(10))
    print("3) ", all_the_same_3(10))


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    def all_the_same_1():
        combs = []
        for x in [1, 2, 3]:
            for y in [3, 1, 4]:
                if x != y:
                    combs.append((x, y))
        return combs

    def all_the_same_2():
        return [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

    print("1) ", all_the_same_1())
    print("2) ", all_the_same_2())


def example03():
    ex = "example03"
    print("\n", ex, "-" * len(ex), sep="\n")

    vec = [-4, -2, 0, 2, 4]
    print("v) ", vec)

    # create a new list with the values doubled
    l1 = [x*2 for x in vec]
    print("1) ", l1)

    # filter the list to exclude negative numbers
    l2 = [x for x in vec if x >= 0]
    print("2) ", l2)

    # apply a function to all the elements
    l3 = [abs(x) for x in vec]
    print("3) ", l3)

    # call a method on each element
    l4 = freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print("4) ", l4)

    l5 = [fruit.strip() for fruit in freshfruit]
    print("5) ", l5)

    # create a list of 2-tuples like (number, square)
    l6 = [(x, x**2) for x in range(6)]
    print("6) ", l6)

    # flatten a list using a listcomp with two 'for'
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("\nv) ", vec)
    l7 = [elem for elem in vec]
    print("7) ", *l7, sep=" / ")
    l8 = [num for elem in vec for num in elem]
    print("8) ", l8)


def example04():
    ex = "example04"
    print("\n", ex, "-" * len(ex), sep="\n")

    from math import pi
    l1 = [str(round(pi, i)) for i in range(1, 6)]
    print(l1)


def example10():
    ex = "example10"
    print("\n", ex, "-" * len(ex), sep="\n")

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print("len(matrix): ", len(matrix))

    def all_the_same_1():
        return [[row[i] for row in matrix] for i in range(len(matrix) + 1)]

    def all_the_same_2():
        transposed = []
        for i in range(len(matrix) + 1):
            transposed.append([row[i] for row in matrix])
        return transposed

    def all_the_same_3():
        transposed = []
        for i in range(len(matrix) + 1):
            # the following 3 lines implement the nested listcomp
            transposed_row = []
            for row in matrix:
                transposed_row.append(row[i])
            transposed.append(transposed_row)
        return transposed

    def all_the_same_4():
        return list(zip(*matrix))

    print("1) ", all_the_same_1())
    print("2) ", all_the_same_2())
    print("3) ", all_the_same_3())
    print("4) ", all_the_same_4())


if __name__ == "__main__":
    example01()
    example02()
    example03()
    example04()
    example10()
