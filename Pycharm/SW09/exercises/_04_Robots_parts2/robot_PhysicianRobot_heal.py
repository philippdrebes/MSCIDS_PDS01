#!/usr/bin/env python3

# robot_PhysicianRobot_heal.py

import random


class Robot:

    def __init__(self, name):
        self.name = name
        self.health_level = random.random()

    def needs_a_doctor(self):
        if self.health_level < 0.8:
            return True
        else:
            return False


class PhysicianRobot(Robot):

    def heal(self, robo):
        robo.health_level = random.uniform(robo.health_level, 1)
        print(robo.name + " has been healed by " + self.name + "!")


if __name__ == "__main__":
    doc = PhysicianRobot("Dr. Frankenstein")
    marvin = Robot("Marvin")
    if marvin.needs_a_doctor(): doc.heal(marvin)
