#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_decorators.php
#
# Decorators
# Classes instead of Functions
#
# A class for the fibonacci function by using the __call__ method:
#


class Fibonacci:

    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]


fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")

print("\n", "~" * 30)


# ##################################################
# without __call__

class Tools:

    def __init__(self):
        self.fib_cache = {}

    def fib(self, n):
        if n not in self.fib_cache:
            if n == 0:
                self.fib_cache[0] = 0
            elif n == 1:
                self.fib_cache[1] = 1
            else:
                self.fib_cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.fib_cache[n]


tools = Tools()

for i in range(15):
    print(tools.fib(i), end=", ")

print()
