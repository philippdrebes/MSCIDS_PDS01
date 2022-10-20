# 04_TypeAnnotation_list_Solution.py

# with the 'typing' package we can make many parts of the Pythoen programs type-safe!
# we only want to allow integers as list elements
# But a float (23.5) has crept into the list ...
# we don't notice that with the compiler, because Python adapts itself dynamically to the data types ...


# Question: (easy)
# How can you change the program so that Mypy doesn't display any errors?

# Answer: Change the wrong values on line 24 and 28!!!

import random
from typing import List                 # new: 'List' instead of 'list'

def silly_merge(x: List[int], y: List[int]) -> List[int]:
    endx = random.randint(0, len(x))
    endy = random.randint(0, len(y))
    return x[:endx] + y[:endy]

# here the following message is output with 'mypy':
# 18: error: List item 0 has incompatible type "float"; expected "int"
print(silly_merge([23, 27, 29, 21, 19],[101, 134, 156, 199]))   #

# here the following message is output with 'mypy':
# 22: error: List item 1 has incompatible type "str"; expected "int"
print(silly_merge([23, 22, 19],[101, 134, 156, 199]))

