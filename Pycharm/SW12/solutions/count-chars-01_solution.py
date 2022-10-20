#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#

import string
chars = string.ascii_lowercase

lorem = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita gubergren, no sea takimata sanctus est Lorem ipsum dolor
sit amet.  """

count1 = dict(map(lambda c: (c, lorem.count(c)), chars))
print(count1)
print(count1["e"])

count2 = {c: lorem.count(c) for c in chars}
print(count2)
print(count2["e"])
