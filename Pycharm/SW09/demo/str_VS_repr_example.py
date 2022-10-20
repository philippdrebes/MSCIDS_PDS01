#!/usr/bin/env python3

# str_VS_repr_example.py

# in this example you see with the Roboter11-Version
# the difference between the function __repr__() and __str__():

# Remember:
# 1.  __repr__() we have the goal: Return a string which creates a Roboter11-Object!
# 2. __str__() we have the goal: Make a 'nice' visual Representation of a Roboter11-Object!

# Task 1: run the program ... try to understand the output!
# Task 2: Comment out the function __repr__()! What happens?
# Task 3: Instead of __repr__() comment out now __str__()! What happens?
# Task 4: Comment out __repr__() AND __str__()! What happens?


class Roboter11:
    def __init__(self, name, build_year):
        self.__name = name
        self.build_year = build_year

    def __repr__(self):
        return "Roboter11('" + self.__name + "'," + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build year: " + str(self.build_year)

    # IMPORTANT: New 2 objects should be the same if they have the same name and the same build year!
    def __eq__(self, other):
        return self.__name == other.__name and self.build_year == other.build_year


def main():
    x = Roboter11("Marvin", 1979)

    print("x.__str__(): ", x.__str__())
    print("x.__repr__():" , x.__repr__())

# Task 5:
# __repr__() AND __str__() are NOT commented out ....then
# comment out this code below! Try to understand it!
#     new = eval(repr(x))           # create a 'new' Roboter11-Object with the same 'values' as Roboter11 'x'!
#     print("Are 'x' and 'new' equal i.e. x == new?                  => Solution: {}".format(x == new))
#     print("Are 'x' and 'new' identical i.e. id (x) == id (new)?    => Solution: {}".format(id(x) == id(new)))


if __name__ == "__main__":
    main()


################
# output:
################

# Task 1:  nothing commented out
# x.__str__():  Name: Marvin, Build year: 1979
# x.__repr__(): Roboter11('Marvin',1979)

# Task 2:  only __repr__() commented out
# x.__str__():  Name: Marvin, Build year: 1979
# x.__repr__(): <__main__.Roboter11 object at 0x7fe2ab40ff10>

# Task 3:  only __str__() commented out
# x.__str__():  Roboter11('Marvin',1979)
# x.__repr__(): Roboter11('Marvin',1979)

# Task 4:  __str__() AND __repr__() commented out
# x.__str__():  <__main__.Roboter11 object at 0x7ffb5e48ff10>
# x.__repr__(): <__main__.Roboter11 object at 0x7ffb5e48ff10>
