#!/usr/bin/env python3

#robot_PhysicianRobot_super.py

class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):

    def say_hi(self):
        super().say_hi()
        print("and I am a physician!")


if __name__ == "__main__":
    doc = PhysicianRobot("Dr. Frankenstein")
    doc.say_hi()
