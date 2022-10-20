#!/usr/bin/env python3
# 2021-10: mae
# https://www.python-course.eu/python3_properties.php

# Properties

# Alternatively, we could have used a different syntax
# without decorators to define the property


class P:

    def __init__(self, x):
        self.set_x(x)                           # mae: initialisation  with a set_x() -Method
        print("0)", self.__dict__)

    def get_x(self):
        return self.__x


    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


    # https://docs.python.org/3/library/functions.html#property
    x = property(get_x, set_x)


p1 = P(1001)
# mae
print("1)", p1.__dict__)
print("2)", P.__dict__)
print("3) ", p1.x)
print("3a) ", p1.__dir__())
print("3a) type(p1.x) ", type(p1.x))

p1.x = -12


# mae some code more:
print("4)", p1.__dict__)
print("5)", P.__dict__)
print("6) ", p1.x)

print("7) ", p1._P__x)

###########
# output
# 0) {'_P__x': 1000}
# 1) {'_P__x': 1000}
# 2) {'__module__': '__main__', '__init__': <function P.__init__ at 0x0000020A47E275E0>,
#     'get_x': <function P.get_x at 0x0000020A47E273A0>, 'set_x': <function P.set_x at 0x0000020A47E271F0>,
#     'x': <property object at 0x0000020A47DDDEA0>, '__dict__': <attribute '__dict__' of 'P' objects>,
#     '__weakref__': <attribute '__weakref__' of 'P' objects>, '__doc__': None}
# 3)  1000
# 3a)  ['_P__x', '__module__', '__init__', 'get_x', 'set_x', 'x', '__dict__', '__weakref__', '__doc__',
#       '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__',
#       '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__',
#       '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
# 3a) type(p1.x)  <class 'int'>
# 4) {'_P__x': 0}
# 5) {'__module__': '__main__', '__init__': <function P.__init__ at 0x0000020A47E275E0>,
#     'get_x': <function P.get_x at 0x0000020A47E273A0>, 'set_x': <function P.set_x at 0x0000020A47E271F0>,
#     'x': <property object at 0x0000020A47DDDEA0>, '__dict__': <attribute '__dict__' of 'P' objects>,
#     '__weakref__': <attribute '__weakref__' of 'P' objects>, '__doc__': None}
# 6)  0
# 7)  0
