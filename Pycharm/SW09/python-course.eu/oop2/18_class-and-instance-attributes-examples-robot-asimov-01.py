#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_class_and_instance_attributes.php

# Class and Instance Attributes
# Example with Class Attributes
#
# Isaac Asimov devised and introduced the so-called "Three Laws of Robotics" in
# 1942.


class Robot:

    Three_Laws = (
        "A robot may not injure a human being or, through inaction, "
        "allow a human being to come to harm.",

        "A robot must obey the orders given to it by human beings, "
        "except where such orders would conflict with the First Law., ",

        "A robot must protect its own existence as long as such "
        "protection does not conflict with the First or Second Law."
    )

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    # other methods as usual


if __name__ == "__main__":
    for number, text in enumerate(Robot.Three_Laws):
        print(str(number+1) + ":\n" + text)
