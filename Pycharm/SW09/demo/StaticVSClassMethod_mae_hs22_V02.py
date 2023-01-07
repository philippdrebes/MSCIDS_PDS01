#!/usr/bin/env python3

# StaticVSClassMethod.py

# Python program to demonstrate
# use of class method and static method.

# Goal: Program some (not only __init__(...)! ) 'constructors' (="factory functions" for Person-objects

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # # Original-Code:
    # # a class method to create a Person object by birth year.
    # @classmethod
    # def from_birth_year(cls, name, year):
    #     return cls(name, date.today().year - year)


    # ff     := factory function
    # n      := name parameter
    # by     := birth year parameter
    # ay     := age years (age of the person) parameter
    # no_n   := no name parameter
    # no_by  := no birth year parameter
    # no_ay  := no age years parameter

    @classmethod
    def ff_n_by(cls, name, birth_year):
        return cls(name, date.today().year-birth_year)         # creates a person object => "factory function"

    @classmethod
    def ff_n_ay(cls, name, age_year):
        return cls(name, age_year)                             # creates a person object => "factory function"

    @classmethod
    def ff_no_n_by(cls, birth_year):
        return cls("no name:", date.today().year-birth_year)   # creates a person object => "factory function"

    @classmethod
    def ff_n_no_by(cls, name):
        # return cls(name, "undefined age!")                   # don't work together with is_adult()-method!!!
        return cls(name, 0)                                    # creates a person object => "factory function"

    # and so on!!!!



    # a static method to check if a Person is adult or not.
    @staticmethod
    def is_adult(age):
        return age > 18

    # def is_adult(self):                      # forbidden => NO Method-Overloading in Python!!!!!
    #     return self.age

person1 = Person('mayank1:', 21)               # call __init__(....) from Person class!!!!
person2 = Person.ff_n_by('mayank2:', 1999)     # factory function call!
person3 = Person.ff_n_ay('mayank3:', 13)       # factory function call!
person4 = Person.ff_no_n_by(1970)              # factory function call!
person5 = Person.ff_n_no_by('mayank3:')        # factory function call!

print(person1.name, person1.age)
print(person2.name, person2.age)
print(person3.name, person3.age)
print(person4.name, person4.age)
print(person5.name, person5.age)

# print the result
print(Person.is_adult(22))                     # call staticmethod  with a class
print(person1.is_adult(22))                    # call staticmethod with an object (possible!)


print(person1.name, "is older then 18 is" , person1.is_adult(person1.age))
print(person2.name, "is older then 18 is" , person2.is_adult(person2.age))
print(person3.name, "is older then 18 is" , person3.is_adult(person3.age))
print(person4.name, "is older then 18 is" , person4.is_adult(person4.age))
print(person5.name, "is older then 18 is" , person5.is_adult(person5.age))
