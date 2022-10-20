#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/functions.html#sorted
# https://docs.python.org/3/howto/sorting.html

lines = []
with open('sortme1.txt', 'r') as f:
    for line in f:
        lines.append(line.strip().split(","))
print(lines)
sort1 = sorted(lines, key=lambda r: r[1])
print("1) ", *sort1, sep="\n")


# ~~~~~~~~~~~~~~~~~~~~
lines = []
with open('sortme2.txt', 'r') as f:
    for line in f:
        lines.append(line.strip().split(","))
print(lines)
sort2 = sorted(lines, key=lambda r: r[1])
print("2) ", *sort2, sep="\n")

sort3 = sorted(lines, key=lambda r: int(r[1]))
print("3) ", *sort3, sep="\n")
