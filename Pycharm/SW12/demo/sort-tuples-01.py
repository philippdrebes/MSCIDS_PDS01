#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/howto/sorting.html
# https://docs.python.org/3/howto/sorting.html#operator-module-functions
# https://docs.python.org/3/library/operator.html#operator.itemgetter

from operator import itemgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sort1 = sorted(student_tuples, key=lambda student: student[2])
sort2 = sorted(student_tuples, key=itemgetter(2))
sort3 = sorted(student_tuples, key=itemgetter(1, 2))

print("1) ", sort1)
print("2) ", sort2)
print("3) ", sort3)
