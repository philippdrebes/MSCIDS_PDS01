#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis
# https://www.python-course.eu/python3_object_oriented_programming.php

# _01_robot_all_08_sol.py

class Robot():

    def __init__(self,
                 name=None,
                 build_year=None):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)

    def __del__(self):
        print(self.name + " says bye-bye!")

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

def my_main():
    x = Robot("Tik-Tok")
    print("Deleting x")
    del x

    x = Robot("Henry", 2008)
    y = Robot()
    y.name = "Marvin"
    x.say_hi()
    y.say_hi()

if __name__ == "__main__":
    my_main()

###############
# output:
# Deleting x
# Tik-Tok says bye-bye!
# Hi, I am Henry
# I was built in 2008
# Hi, I am Marvin
# It's not known, when I was created!
# Henry says bye-bye!
# Marvin says bye-bye!
