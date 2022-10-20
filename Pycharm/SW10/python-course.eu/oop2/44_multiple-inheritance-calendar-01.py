#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance

# Example: CalendarClock
# We implement to independent classes: a "Clock" and a "Calendar2" class.
#
# After this, we will introduce a class "CalendarClock", which is, as the name
# implies, a combination of "Clock" and "Calendar2". CalendarClock inherits both
# from "Clock" and "Calendar2".
#
# https://docs.python.org/3/library/calendar.html
# => Calendar2 not Calendar

"""
The class Calendar2 implements a calendar.
"""


class Calendar2:

    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        """
        The method leapyear returns True if the parameter year
        is a leap year, False otherwise
        """
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    def __init__(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be
        a four digit year number
        """

        self.set_calendar(d, m, y)

    def set_calendar(self, d, m, y):
        """
        d, m, y have to be integer values and year has to be
        a four digit year number
        """

        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers!")

    def __str__(self):
        if Calendar2.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days,
                                                   self.__months,
                                                   self.__years)
        else:
            # assuming American style
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months,
                                                   self.__days,
                                                   self.__years)

    def advance(self):
        """
        This method advances to the next date.
        """

        max_days = Calendar2.months[self.__months - 1]
        if self.__months == 2 and Calendar2.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days = 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1


if __name__ == "__main__":
    x = Calendar2(31, 12, 2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("2012 was a leapyear:")
    x = Calendar2(28, 2, 2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    x = Calendar2(28, 2, 2013)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("1900 no leapyear: number divisible by 100 but not by 400: ")
    x = Calendar2(28, 2, 1900)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("2000 was a leapyear, because number divisibe by 400: ")
    x = Calendar2(28, 2, 2000)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("Switching to American date style: ")
    Calendar2.date_style = "American"
    print("after applying advance: ", x)
