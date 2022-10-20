#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Class Methods
#
# The use cases of class methods:
#
# the are used in the definition of the so-called factory methods, which we
# will not cover here.
#
# They are often used, where we have static methods, which have to call other
# static methods. To do this, we would have to hard code the class name, if we
# had to use static methods. This is a problem, if we are in a use case, where
# we have inherited classes.


class Fraction:

    def __init__(self, n, d):
        self.numerator, self.denominator = Fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)


if __name__ == "__main__":
    x = Fraction(8, 24)
    print(x)

    print(Fraction.gcd(8, 24))
    print(Fraction.gcd(4, 30))
    print(Fraction.reduce(8, 24))
    print(Fraction.reduce(4, 30))
