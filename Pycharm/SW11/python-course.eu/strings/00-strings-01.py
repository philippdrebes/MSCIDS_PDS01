#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_sequential_data_types.php
#
# Sequential Data Types
# Slicing (Strings)
#
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Python is great"
    first_six = a_string[0:6]
    print(first_six)

    starting_at_five = a_string[5:]
    print(starting_at_five)

    a_copy = a_string[:]
    print(a_copy)

    without_last_five = a_string[0:-5]
    print(without_last_five)

    print("\n3")
    print(a_string[3])
    print(a_string[3:])
    print(a_string[:3])

    print("\n-3")
    print(a_string[-3])
    print(a_string[:-3])
    print(a_string[-3:])

    print("\n:")
    print(a_string[3:5])
    print(a_string[3:-3])
    print(a_string[-3:-1])

    print("\n::")
    print(a_string[3:8])
    print(a_string[3:8:2])


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
    first_three = cities[0:3]
    print(first_three)

    # or easier:
    first_three = cities[:3]
    print(first_three)

    all_but_last_two = cities[:-2]
    print(all_but_last_two)


def example03():
    ex = "example03"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = """
    foo
    bar
    demo='gugus'
    """

    print(a_string)

    print("~" * 10)
    a_string = """
foo
bar
demo='gugus'
    """

    print(a_string)

    print("~" * 10)
    a_string = (
        "foo "
        "bar "
        "demo='gugus' "
    )
    print(a_string)


def example04():
    ex = "example04"
    print("\n", ex, "-" * len(ex), sep="\n")

    # s[begin: end: step]

    a_string = "Python under Linux is great"
    a = a_string[::3]
    print(a)

    s = ("TPoyrtohnotno  ciosu rtshees  lianr "
         "gTeosrto nCtiot yb yi nB oCdaennasdeao")
    print(s)
    a = s[::2]
    print(a)


def example05():
    ex = "example05"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Toronto is the largest City in Canada"
    a_list = a_string.split(" ")
    print(a_list)
    s = ";".join(a_list)
    print(s)


def example06():
    ex = "example06"
    print("\n", ex, "-" * len(ex), sep="\n")

    txt = "Hello World"
    print(len(txt))


def example07():
    ex = "example07"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Python is easy!"
    if "y" in a_string:
        print("y is in a_string")
    if "x" in a_string:
        print("x is in a_string")


def example08():
    ex = "example08"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "xyz-"
    t = a_string + a_string + a_string + a_string
    print(t)
    t = a_string * 4
    print(t)


if __name__ == "__main__":
    example01()
    example02()
    example03()
    example04()
    example05()
    example06()
    example07()
    example08()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example01
# ---------
# Python
# n is great
# Python is great
# Python is
#
# 3
# h
# hon is great
# Pyt
#
# -3
# e
# Python is gr
# eat
#
# :
# ho
# hon is gr
# ea
#
# ::
# hon i
# hni
#
#
# example02
# ---------
# ['Vienna', 'London', 'Paris']
# ['Vienna', 'London', 'Paris']
# ['Vienna', 'London', 'Paris', 'Berlin']
#
#
# example03
# ---------
#
#     foo
#     bar
#     demo='gugus'
#
# ~~~~~~~~~~
#
# foo
# bar
# demo='gugus'
#
# ~~~~~~~~~~
# foo bar demo='gugus'
#
#
# example04
# ---------
# Ph d n  e
# TPoyrtohnotno  ciosu rtshees  lianr gTeosrto nCtiot yb yi nB oCdaennasdeao
# Toronto is the largest City in Canada
#
#
# example05
# ---------
# ['Toronto', 'is', 'the', 'largest', 'City', 'in', 'Canada']
# Toronto;is;the;largest;City;in;Canada
#
#
# example06
# ---------
# 11
#
#
# example07
# ---------
# y is in a_string
#
#
# example08
# ---------
# xyz-xyz-xyz-xyz-
# xyz-xyz-xyz-xyz-
