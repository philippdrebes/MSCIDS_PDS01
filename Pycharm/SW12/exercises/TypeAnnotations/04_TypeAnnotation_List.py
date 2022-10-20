# 04_TypeAnnotation_list.py

# with the 'typing' package we can make many parts of the Pythoen programs type-safe!
# we only want to allow integers as list elements
# But a float (23.5) has crept into the list ...
# we don't notice that with the compiler, because Python adapts itself dynamically to the data types ...

import random
from typing import List                 # new: 'List' instead of 'list'

def silly_merge(x: List[int], y: List[int]) -> List[int]:
    endx = random.randint(0, len(x))
    endy = random.randint(0, len(y))
    return x[:endx] + y[:endy]

# here the following message is output with 'mypy':
# 18: error: List item 0 has incompatible type "float"; expected "int"
print(silly_merge([23.5, 27, 29, 21, 19],[101, 134, 156, 199]))   #

# here the following message is output with 'mypy':
# 22: error: List item 1 has incompatible type "str"; expected "int"
print(silly_merge([23, "step out of line", 19],[101, 134, 156, 199]))


# Question: (easy)
# How can you change the program so that Mypy doesn't display any errors?


#####################################################################################
# There's another new idea: type alias
# In the next code example 'sales' is a type alias
#####################################################################################

# Umsatz   = sales
# Ergebnis = result

from typing import List
sales = List[float]     # ATTENTION: This is a new data type from module 'typing': List (capitalized!)


def convert(sales_list : sales, factor : float) -> sales:
    result_list = []
    for sale in sales_list:
        result_list.append( sale * factor )
    return result_list

print( convert( [312.9, 543.9, 100.45, 98.99], 1.18 ) )

