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

    def __init__(self, x):    # i := init
        print("ia: in __init__) => self.x, x: ", self.x, x)
        self.x = x                              # mae: "normal" initialisation
                                                # self.x ist ein int!
        print("ib: => type(self.x), self.x, x: ", type(self.x), self.x, x)           # => <class 'int'>
        #self.__x = x                              # mae: with hidden Attribute   WAU => 1001!!!!!

    @property          # g := getter
    def x(self):
        print("\ng1: in x(self) d.h.getter method => self.__dict__: ", self.__dict__)
        #print("g1_: self.__x: ", self.__x)   # first time => empty!!!
        try:
            if self.__x != None:
                print("g1a: self.__x: ", self.__x)
                print("g1a_: id(self.__x): ", id(self.__x))
                print("g1a__: id(self._P__x): ", id(self._P__x))
                return self.__x
        except AttributeError:
            print("g1b: None")
            return None

    @x.setter                 # s := setter
    def x(self, x):
        print("\ns1a: in @x.setter => self.__dict: ", self.__dict__)
        try:
            if self.__x != None:
                print("s1b: ", self.__x)
        except AttributeError:
            print("s1c: None")
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
        print("s2: in @x.setter => self.__dict: ", self.__dict__)
        print("s2: in @x.setter => self.__x: ", self.__x)


p1 = P(1001)
#mae
print("\n1) p1.x: ", p1.x)
p1.x = -12
#mae
print("\n2) p1.x: ", p1.x)

# mae
print("3a) p1.__dict__: ", p1.__dict__)
# print("3b) P.__dict__: ", P.__dict__)

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




#################
# output für:
# g1: in x(self) d.h.getter method => self.__dict__:  {}
# g1b: None
# ia: in __init__) => self.x, x:  None 1001
#
# s1a: in @x.setter => self.__dict:  {}
# s1c: None
# s2: in @x.setter => self.__dict:  {'_P__x': 1000}
# s2: in @x.setter => self.__x:  1000
#
# g1: in x(self) d.h.getter method => self.__dict__:  {'_P__x': 1000}
# g1a: self.__x:  1000
# g1a_: id(self.__x):  2842629524784
# g1a__: id(self._P__x):  2842629524784
#
# g1: in x(self) d.h.getter method => self.__dict__:  {'_P__x': 1000}
# g1a: self.__x:  1000
# g1a_: id(self.__x):  2842629524784
# g1a__: id(self._P__x):  2842629524784
# ib: => type(self.x), self.x, x:  <class 'int'> 1000 1001
#
# g1: in x(self) d.h.getter method => self.__dict__:  {'_P__x': 1000}
# g1a: self.__x:  1000
# g1a_: id(self.__x):  2842629524784
# g1a__: id(self._P__x):  2842629524784
#
# 1) p1.x:  1000
#
# s1a: in @x.setter => self.__dict:  {'_P__x': 1000}
# s1b:  1000
# s2: in @x.setter => self.__dict:  {'_P__x': 0}
# s2: in @x.setter => self.__x:  0
#
# g1: in x(self) d.h.getter method => self.__dict__:  {'_P__x': 0}
# g1a: self.__x:  0
# g1a_: id(self.__x):  140730716329600
# g1a__: id(self._P__x):  140730716329600
#
# 2) p1.x:  0
# 3a) p1.__dict__:  {'_P__x': 0}
#
# g1: in x(self) d.h.getter method => self.__dict__:  {'_P__x': 88, '__x': 7}
# g1a: self.__x:  88
# g1a_: id(self.__x):  140730716332416
# g1a__: id(self._P__x):  140730716332416
# 4a) p1.x:  88
# 4b) p1.__x:  7
# 4c) p1._P__x:  88
# 4d) p1.__dict__:  {'_P__x': 88, '__x': 7}
#
# s1a: in @x.setter => self.__dict:  {'_P__x': 88, '__x': 7}
# s1b:  88
# s2: in @x.setter => self.__dict:  {'_P__x': 1000, '__x': 7}
# s2: in @x.setter => self.__x:  1000
#
# g1: in x(self) d.h.getter method => self.__dict__:  {'_P__x': 1000, '__x': 7}
# g1a: self.__x:  1000
# g1a_: id(self.__x):  2842629524784
# g1a__: id(self._P__x):  2842629524784
#
# 5) p1.x:  1000
# 5a) p1.__dict__:  {'_P__x': 1000, '__x': 7}
# 5b) P.__dict__:  {'__module__': '__main__', '__init__': <function P.__init__ at 0x00000295C94874C0>,
#                   'x': <property object at 0x00000295C97ECA90>, '__dict__': <attribute '__dict__' of 'P' objects>,
#                   '__weakref__': <attribute '__weakref__' of 'P' objects>, '__doc__': None, '__x': 99}
