#!/usr/bin/env python3

# robot_say_hi.py

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


if __name__ == "__main__":
    x = Robot("Henry", 2008)
    y = Robot()
    y.name = "Marvin"
    x.say_hi()
    y.say_hi()
