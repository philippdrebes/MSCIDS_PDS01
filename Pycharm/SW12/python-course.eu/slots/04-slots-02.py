#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_slots.php
#
# Slots
# Avoiding Dynamically Created Attributes
#
# You can't do this with built-in classes like 'int', or 'list':
#


x = 42
x.a = "not possible to do it"
# print(x.__dict__)
