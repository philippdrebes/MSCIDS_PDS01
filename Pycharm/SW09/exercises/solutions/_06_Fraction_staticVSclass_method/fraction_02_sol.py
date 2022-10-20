#!/usr/bin/env python3

# fraction_02_sol.py

class Fraction:

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        if type(other) == int:
            return self + Fraction(other, 1)
        elif type(other) == Fraction:
            numerator1 = self.num * other.den + self.den * other.num
            denominator1 = self.den * other.den
            common = self.gcd(numerator1, denominator1)
            return Fraction(numerator1 // common, denominator1 // common)
        else:
            return "NotImplemented"

    def __eq__(self, other):
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den

        return numerator1 == numerator2


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(3, 4)
    print("x:", x)
    print("y:", y)
    print("x + y:", x + y)
    print("x == y:", x == y)
    print("x + 42:", x + 42)
    print("x + 42.0:", x + 42.0)
    print("x + '42':", x + "42")
