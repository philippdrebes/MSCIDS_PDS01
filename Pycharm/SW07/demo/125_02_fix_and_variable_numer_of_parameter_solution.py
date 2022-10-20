#!/usr/bin/env python3

# 125_02_fix_and_variable_numer_of_parameter_solution.py
# Variable Length of Parameters (e)
# You need to calculate the arithmetic mean of any (!!)  number of numbers

# New problem: We want to call our function with a list 'lst'
# Solution: write in the function-call an astrix '*' in front of the parameter

# a frist solution (short and 'sec'
def arimean(first_value, *further_values):
    return (first_value + sum(further_values)) / (1 + len(further_values))

lst = [4, 7, 9, 45]
res01 = arimean(*lst)            # that works!!!! Wow!
print(res01)


#########
# Output:
########
# 16.25