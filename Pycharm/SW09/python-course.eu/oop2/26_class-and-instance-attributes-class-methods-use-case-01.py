#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Methods
#
# not elegant

# gcd
#  https://en.wikipedia.org/wiki/Greatest_common_divisor
#  https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm
# reduce
#  https://en.wikipedia.org/wiki/Fraction#Simplifying_(reducing)_fractions


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reduce(n1, n2):
    g = gcd(n1, n2)
    return (n1 // g, n2 // g)


class Fraction:

    def __init__(self, n, d):
        self.numerator, self.denominator = reduce(n, d)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)


if __name__ == "__main__":
    x = Fraction(8, 24)
    print(x)

    print(gcd(8, 24))
    print(gcd(4, 30))
    print(reduce(8, 24))
    print(reduce(4, 30))
