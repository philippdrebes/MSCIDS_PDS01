#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_generators.php
#
# Generators
# yield from
#
# The yield from <expr> statement can be used inside the body of a
# generator. <expr> has to be an expression evaluating to an iterable, from
# which an iterator will be extracted.
#


def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city


def squares():
    for number in range(10):
        yield number ** 2


def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number


def generator_splitted():
    yield from cities()
    yield from squares()


lst1 = [el for el in generator_all_in_one()]
lst2 = [el for el in generator_splitted()]
print(lst1 == lst2)

print(lst1)
