#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Destructor

# python 3.6 is OK with this ...


class Robot():

    def __init__(self, name):
        self.name = name
        print(name + " has been created!")

    def __del__(self):
        print(self.name + " says bye-bye!")


if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y


