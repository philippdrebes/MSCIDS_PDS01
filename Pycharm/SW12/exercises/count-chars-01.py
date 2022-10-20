#!/usr/bin/env python3
#
#

# Task to do:  Cont character occurences of the following text ' lorem'



import string
chars = string.ascii_lowercase

lorem = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita gubergren, no sea takimata sanctus est Lorem ipsum dolor
sit amet.  """

count1 = {}
# count1 = dict(map( ... ))

print(count1)
# print(count1["e"])

count2 = {}
# count2 = # use dict comprehension
print(count2)
# print(count2["e"])




# The result will be:
# ~~~~~~~~~~~~~~~~~~~~
# {'a': 21, 'b': 3, 'c': 6, 'd': 12, 'e': 28, 'f': 0, 'g': 4, 'h': 0, 'i': 15,
# 'j': 1, 'k': 1, 'l': 9, 'm': 16, 'n': 10, 'o': 21, 'p': 5, 'q': 1, 'r': 16,
# 's': 17, 't': 25, 'u': 15, 'v': 3, 'w': 0, 'x': 0, 'y': 2, 'z': 0}
#
# 28
