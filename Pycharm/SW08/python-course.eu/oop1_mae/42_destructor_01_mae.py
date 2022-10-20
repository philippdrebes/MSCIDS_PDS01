#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_object_oriented_programming.php

# Destructor

# What we said about constructors holds true for destructors
# as well. There is no "real" destructor, but something
# similar, i.e. the method __del__. It is called when the
# instance is about to be destroyed and if there is no other
# reference to this instance.


class Robot():

    def __init__(self, name):
        self._name = name
        print(self._name + " has been created!")

    def __del__(self):
        print("Robot has been destroyed:", self._name)


if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print(z._name)
    print("Deleting x")
    del x
    print("Deleting y")
    del y
    print("Still there?", z._name)
    print("Deleting z")
    del z
    print("end")


# possible output:
# Tik-Tok has been created!
# Jenkins has been created!
# Tik-Tok
# Deleting x
# Deleting y
# Robot has been destroyed: Jenkins
# Still there? Tik-Tok
# Deleting z
# Robot has been destroyed: Tik-Tok
# end
