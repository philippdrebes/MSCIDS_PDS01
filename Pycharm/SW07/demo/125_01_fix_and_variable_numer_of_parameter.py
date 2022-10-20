#!/usr/bin/env python3

# 125_01_fix_and_variable_numer_of_parameter.py
# Variable Length of Parameters (d)
# You need to calculate the arithmetic mean of any (!!)  number of numbers

# a frist solution (short and 'sec')
def arimean(first_value, *further_values):
    return (first_value + sum(further_values)) / (1 + len(further_values))

# a second solution of a aremean-function!!!
def arimean_with_loop(first_value, *further_values):
    number =1
    sum = first_value
    for zahl in further_values:
        sum += zahl
        number += 1
    return (sum/number)

print("arimean(1):",arimean(1))

print("arimean(1, 2):", arimean(1, 2))

print("arimean(35, 89, 103, 1, 17):",arimean(35, 89, 103, 1, 17))

# print("arimean(): ", arimean())          # what can we do to prevent this error?




#########
# Output:
########
# arimean(1): 1.0
# arimean(1, 2): 1.5
# arimean(35, 89, 103, 1, 17): 49.0