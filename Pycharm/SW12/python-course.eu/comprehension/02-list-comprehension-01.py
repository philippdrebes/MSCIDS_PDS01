#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_list_comprehension.php
#
# List Comprehension
# Examples
#

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [((float(9)/5)*x + 32) for x in Celsius]
print(Fahrenheit)
