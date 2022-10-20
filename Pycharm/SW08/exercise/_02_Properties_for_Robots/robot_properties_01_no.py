#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# robot_properties_01_no.py

class Robot:

    def __init__(self,
                 name=None,
                 build_year=None):
        self.name = name
        self.build_year = build_year

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
    x = Robot("Henry", 1990)
    y = Robot()
    y.name = "Marvin"
    y.build_year = 2000
    x.say_hi()
    y.say_hi()
    y.build_year = x.build_year + 5
    y.say_hi()


if __name__ == "__main__":
    my_main()
