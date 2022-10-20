#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Example with Class Attributes
#
# how you can count instance with class attributes


class C:

    counter = 0

    def __init__(self):
        C.counter += 1

    def __del__(self):
        type(self).counter -= 1   # more elegant than C.counter but the same


if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
