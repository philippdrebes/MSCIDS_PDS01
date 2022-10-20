#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_lambda.php
#
# Lambda, filter, reduce and map
# The map() Function
#
# Starting point
# map() returns an iterator
#


def fahrenheit(t):
    return ((float(9)/5)*t + 32)


def celsius(t):
    return (float(5)/9)*(t-32)


temperatures = (36.5, 37, 37.5, 38, 39)

F = map(fahrenheit, temperatures)
print(type(F))

for f in F:
    print("1)", f)

for f in F:
    print("2)", f)


F2 = map(fahrenheit, temperatures)
C = map(celsius, F2)

print(type(C))

for c in C:
    print("3)", c)

print("~" * 30)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)
