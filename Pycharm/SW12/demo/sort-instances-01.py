#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/howto/sorting.html
# https://docs.python.org/3/howto/sorting.html#operator-module-functions
# https://docs.python.org/3/library/operator.html#operator.attrgetter

from operator import attrgetter


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sort1 = sorted(student_objects, key=lambda student: student.age)
sort2 = sorted(student_objects, key=attrgetter('age'))
sort3 = sorted(student_objects, key=attrgetter('grade', 'age'))

print("1) ", sort1)
print("2) ", sort2)
print("3) ", sort3)
