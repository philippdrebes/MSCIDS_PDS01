#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Decorator - Properties

# * A method which is used for getting a value is
#   decorated with "@property".
# * The method which has to function as the setter is decorated
#   with "@x.setter"
# * If the function had been called "f", we would have to
#   decorate it with "@f.setter".

# This is the Pythonic way to do it.

########
# new business rule: only values  (0 <= value <= 1000) are correct!
# goal => the object p1 should not be created and set wrong!
#         examples: entered = 1001 => set = 1000
#                   entered -12    => set = 0)
# and
#          all old code should continue to run (unchanged!!!)
########

class P:

    def __init__(self, x):
        self.x = x                               # mae: "normal" initialisation

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


# a simple 'old' script/program
p1 = P(1001)
print("1) p1.x: ", p1.x)
p1.x = -12
print("2) p1.x: ", p1.x)

# new part in the old script:
print("3) ", p1.__dict__)

################################3

# in der Vorlesung kurz zeigen:
p1.__x = 7            # ist das Zugriff auf _P__x?  nein!!! => "dynamisch" d.h. während der Laufzeit
                      #                                         wird neue Variable erzeugt!
p1._P__x = 88         # so ist also ein Zugriff auch auf private Variablen IMMER möglich! (don't do it!)

print("4a) p1.x: ", p1.x)
print("4b) p1.__x: ", p1.__x)
print("4c) p1._P__x: ", p1._P__x)
print("4d) p1.__dict__: ", p1.__dict__)

p1.x = 5000           # reduziert auf 1000!
print("\n5) p1.x: ",p1.x)

# create also a (dynamic-generated) class-Variable
P.__x = 99
print("5a) p1.__dict__: ", p1.__dict__)
print("5b) P.__dict__: ", P.__dict__)


#######################
# output:
# 1)  1000
# 2)  0
# 3)  {'_P__x': 0}
# 4a) p1.x:  88
# 4b) p1.__x:  7
# 4c) p1._P__x:  88
# 4d) p1.__dict__:  {'_P__x': 88, '__x': 7}
#
# 5) p1.x:  1000
# 5a) p1.__dict__:  {'_P__x': 1000, '__x': 7}
# 5b) P.__dict__:  {'__module__': '__main__', '__init__': <function P.__init__ at 0x00000218FA5F7820>,
#                   'x': <property object at 0x00000218FA939720>, '__dict__': <attribute '__dict__' of 'P' objects>,
#                   '__weakref__': <attribute '__weakref__' of 'P' objects>, '__doc__': None, '__x': 99}
