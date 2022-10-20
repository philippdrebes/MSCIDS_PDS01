#!/usr/bin/env python3
# 2020-11, Bruno Grossniklaus, https://github.com/it-gro

# Shallow and Deep Copy
# Using the Methods copy, deepcopy from the Module copy
#
# Review with http://www.pythontutor.com/visualize.html#mode=edit

from copy import deepcopy, copy

lst_orig = ['a', 'b', ['ab', 'ba']]

lst_alias = lst_orig
lst_slice = lst_orig[:]
lst_copy = copy(lst_orig)
lst_deepcopy1 = deepcopy(lst_orig)
lst_deepcopy2 = deepcopy(lst_orig)

lst_slice[0] = "slice"
lst_copy[0] = "copy"
lst_copy[2][1] = "e"

lst_deepcopy2[0] = "deepcopy"
lst_deepcopy2[2][1] = "d"

print("1) ", lst_orig)
print("2) ", lst_copy)
print("3) ", lst_deepcopy1)
print("4) ", lst_deepcopy2)
print("5) ", lst_alias)
print("6) ", lst_slice)
