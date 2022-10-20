#!/usr/bin/env python3

# 125_02_fix_and_variable_numer_of_parameter.py
# Variable Length of Parameters (e)
# You need to calculate the arithmetic mean of any (!!)  number of numbers

# New problem: We want to call our function with a list 'lst'

# a frist solution (short and 'sec'
def arimean(first_value, *further_values):
    return (first_value + sum(further_values)) / (1 + len(further_values))

lst = [4, 7, 9, 45]
arimean(lst)            # don't work!

# A cumbersome solution
# print( arimean( lst[0], lst[1], lst[2], lst[3] ), lst[4] )

# BUT we often don't even know how many parameters we have
# then we have a problem!!!!!!!!!!!!


#########
# Output:
########
# Traceback (most recent call last):
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/Kap14_Functions_english/125_02_fix_and_variable_numer_of_parameter.py", line 12, in <module>
#     arimean(lst)            # geht nicht!
#   File "C:/Users/Erwin Mathis/PycharmProjects/IDS_Python/Kap14_Functions_english/125_02_fix_and_variable_numer_of_parameter.py", line 9, in arimean
#     return (first_value + sum(further_values)) / (1 + len(further_values))
# TypeError: can only concatenate list (not "int") to list