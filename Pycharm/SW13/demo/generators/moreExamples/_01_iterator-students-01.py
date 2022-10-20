#!/usr/bin/env python3
# 2020-05, Bruno Grossniklaus, https://github.com/it-gro


class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age


students = [Student("Name1", 21), Student("Name2", 21), Student("Name3", 25),
            Student("Name4", 20), Student("Name5", 28), ]

my_class = iter(students)
while my_class:
    try:
        student = next(my_class)
        print(student.name)
    except StopIteration:
        break

my_class = iter(students)
while my_class:
    try:
        student = next(my_class)
        print(student.age)
    except StopIteration:
        break


for s in students:
    print(s.name, s.age)


print("done")
