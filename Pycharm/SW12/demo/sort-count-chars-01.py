#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/functions.html#sorted
# https://docs.python.org/3/howto/sorting.html

import string
chars = string.ascii_lowercase
print(chars)
lorem = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita gubergren, no sea takimata sanctus est Lorem ipsum dolor
sit amet.  """

counts = {c: lorem.count(c) for c in chars}
print(counts)
print(counts["e"])

sort1 = sorted(counts.items(), key=lambda kv: kv[0])
print("1) ", sort1)

sort2 = sorted(counts.items(), key=lambda kv: kv[1])
print("2) ", sort2)

sort3 = sorted(counts.items(), key=lambda kv: (kv[1]), reverse=True)
print("3) ", sort3)

sort4 = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print("4) ", sort4)

sort5 = sorted(counts.items(), key=lambda kv: str(kv[1]), reverse=True)
print("5) ", sort5)
