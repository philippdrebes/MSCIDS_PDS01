#!/usr/bin/env python3
# 2020-04
# https://www.python-course.eu/python3_multiple_inheritance.php

# Multiple Inheritance

# Example: CalendarClock
# We implement to independent classes: a "Clock" and a "Calendar" class.
#
# After this, we will introduce a class "CalendarClock", which is, as the name
# implies, a combination of "Clock" and "Calendar". CalendarClock inherits both
# from "Clock" and "Calendar".

# $ ln -s *_multiple-inheritance-clock-01.py clock.py
# $ ln -s *_multiple-inheritance-calendar-01.py calendar2.py

"""
Modul, which implements the class CalendarClock.
"""

# mae new:   Zeigen warum main() wichtig ist in Modulen .... => ;-)



print("__name__: ", __name__)
from clock_MAE import Clock
from calendar2_MAE import Calendar2

# class CalendarClock(Clock, Calendar2):
#     """
#         The class CalendarClock implements a clock with integrated
#         calendar. It's a case of multiple inheritance, as it inherits
#         both from Clock and Calendar2
#     """
#
#     def __init__(self, day, month, year, hour, minute, second):
#         Clock.__init__(self, hour, minute, second)
#         Calendar2.__init__(self, day, month, year)
#
#     def tick(self):
#         """
#         advance the clock by one second
#         """
#         previous_hour = self._hours
#         # Clock.tick(self)
#         super().tick()
#         if (self._hours < previous_hour):
#             self.advance()
#
#     def __str__(self):
#         return Calendar2.__str__(self) + ", " + Clock.__str__(self)
#
#
# print("Ein Befehl in der Klasse 'CalendarClock'")
#
#
# if __name__ == "__main__":
#     x = CalendarClock(31, 12, 2013, 23, 59, 59)
#     print("One tick from ", x, end=" ")
#     x.tick()
#     print("to ", x)
#
#     x = CalendarClock(28, 2, 1900, 23, 59, 59)
#     print("One tick from ", x, end=" ")
#     x.tick()
#     print("to ", x)
#
#     x = CalendarClock(28, 2, 2000, 23, 59, 59)
#     print("One tick from ", x, end=" ")
#     x.tick()
#     print("to ", x)
#
#     x = CalendarClock(7, 2, 2013, 13, 55, 40)
#     print("One tick from ", x, end=" ")
#     x.tick()
#     print("to ", x)
#
# # Mae:
#     print("0: Base-classes for CalendarClock are: " ,CalendarClock.__mro__)
