#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# _03_fraction_01_sol.py

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Fraction:
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
            common = gcd(numerator1, denominator1)
            return Fraction(numerator1 // common, denominator1 // common)
        else:
            return "NotImplemented"

    def __eq__(self, other):
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den

        return numerator1 == numerator2

def my_main():
    x = Fraction(1, 2)
    y = Fraction(3, 4)
    print("x:", x)
    print("y:", y)
    print("x + y:", x + y)
    print("x == y:", x == y)
    print("x + 42:", x + 42)
    print("x + 42.0:", x + 42.0)
    print("x + '42':", x + "42")

if __name__ == "__main__":
    my_main()

################
# output:
# x: 1/2
# y: 3/4
# x + y: 5/4
# x == y: False
# x + 42: 85/2
# x + 42.0: NotImplemented
# x + '42': NotImplemented
