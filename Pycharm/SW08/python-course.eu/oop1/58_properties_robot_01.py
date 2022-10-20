#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# The following example shows a class, which has internal
# attributes (=private), which can't be accessed from outside. These are
# the private attributes
#       self.__potential_physical and
#       self.__potential_psychic.
# Furthermore we show that a property can be deduced from the values of more than one
# attribute. The property "condition" of our example returns
# the condition of the robot in a descriptive string. The
# condition depends on the sum of the values of the psychic
# and the physical conditions of the robot.


class Robot:

    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"


    def condition_func(self):
        '''
        make the same taks like the 'decorator'-property in the
        the code above!

        :return: the state of our Robot
        '''
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"



if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)              # not x.condition() !!!!!!!!!!!!!!!!
    print(y.condition)

    print(x.condition_func())
    print(y.condition_func())
