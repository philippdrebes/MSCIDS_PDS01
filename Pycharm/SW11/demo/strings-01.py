#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://docs.python.org/3/library/stdtypes.html#str.strip
# https://docs.python.org/3/library/stdtypes.html#str.split
# https://docs.python.org/3/library/stdtypes.html#str.splitlines
# https://docs.python.org/3/library/stdtypes.html#str.partition
# https://docs.python.org/3/library/stdtypes.html#str.find
# https://docs.python.org/3/library/stdtypes.html#str.index
# https://docs.python.org/3/library/stdtypes.html#str.count
# https://docs.python.org/3/library/stdtypes.html#str.replace


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "  foo    bar   foo  \n"
    a_string.strip()
    print(f"1) -{a_string}-")

    s1 = a_string.strip()
    print(f"2) -{s1}-")

    s1 = a_string.lstrip()
    print(f"3) -{s1}-")

    s1 = a_string.rstrip()
    print(f"4) -{s1}-")


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "row1\nrow2\nrow3\nrow4\nrow5\n"
    s1 = a_string.splitlines()
    print(s1)
    s1 = a_string.splitlines(True)
    print(s1)


def example03():
    ex = "example03"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Lorem ipsum, dolor sit amet, consetetur sadipscing"
    t1 = a_string.partition(",")
    print(type(t1))
    print(t1)
    print(*t1, sep="/")

    t1 = a_string.rpartition(",")
    print(*t1, sep="/")


def example04():
    ex = "example04"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Lorem ipsum, dolor sit amet, consetetur sadipscing"
    i = a_string.find("e")
    print(i)
    print(a_string[i:i+5])

    i = a_string.find("foo")
    print(i)

    i = a_string.find("e")
    print(i)

    i = a_string.find("e", 4)
    print(i)

    i = a_string.rfind("e")
    print(i)


def example05():
    ex = "example05"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Lorem ipsum, dolor sit amet, consetetur sadipscing"
    i = a_string.index("e")
    print(i)
    print(a_string[i:i+5])

    # ValueError: substring not found
    # i = a_string.index("foo")
    # print(i)

    i = a_string.rindex("e")
    print(i)


def example06():
    ex = "example06"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Lorem ipsum, dolor sit amet, consetetur sadipscing"
    i = a_string.count("e")
    print(i)

    i = a_string.count("dolor")
    print(i)


def example07():
    ex = "example07"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Lorem ipsum, dolor sit amet, consetetur sadipscing"
    s1 = a_string.replace("e", "~")
    print(a_string)
    print(s1)

    s1 = a_string.replace("dolor", "")
    print(s1)

    s1 = a_string.replace("e", "~").replace("a", "~")
    print(s1)

def example08():
    ex = "example08"
    print("\n", ex, "-" * len(ex), sep="\n")

    a_string = "Lorem ipsum, dolor sit amet, consetetur sadipscing"
    s1 = a_string.__contains__("tetu")
    print(a_string)
    print(s1)



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
# 1) -  foo    bar   foo
# -
# 2) -foo    bar   foo-
# 3) -foo    bar   foo
# -
# 4) -  foo    bar   foo-
#
#
# example02
# ---------
# ['row1', 'row2', 'row3', 'row4', 'row5']
# ['row1\n', 'row2\n', 'row3\n', 'row4\n', 'row5\n']
#
#
# example03
# ---------
# <class 'tuple'>
# ('Lorem ipsum', ',', ' dolor sit amet, consetetur sadipscing')
# Lorem ipsum/,/ dolor sit amet, consetetur sadipscing
# Lorem ipsum, dolor sit amet/,/ consetetur sadipscing
#
#
# example04
# ---------
# 3
# em ip
# -1
# 3
# 25
# 35
#
#
# example05
# ---------
# 3
# em ip
# 35
#
#
# example06
# ---------
# 4
# 1
#
#
# example07
# ---------
# Lorem ipsum, dolor sit amet, consetetur sadipscing
# Lor~m ipsum, dolor sit am~t, cons~t~tur sadipscing
# Lorem ipsum,  sit amet, consetetur sadipscing
# Lor~m ipsum, dolor sit ~m~t, cons~t~tur s~dipscing
#
#
# example08
# ---------
# Lorem ipsum, dolor sit amet, consetetur sadipscing
# True
