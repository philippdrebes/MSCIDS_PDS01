# 50_keyword_parameter_solution.py

# Keyword parameters
# If we want call the function circumference(2) with the 'width' 2
# we have a problem: The number '2' is by default assigned to the first
# Parameter and that is 'length' ...
#
# Task: Change the calls so that the function
# circumference(2) is called with 'width' 2!
# Solution: use Keyword parameter!!!
 

def circumference(length=2, width=1):
    return 2 * (length + width)

c1 = circumference(width=2)          # 2 should be the width !!!
print(c1)

# or with length 5 and width 3:
c2 = circumference(length=5, width=3)
print(c2)

# how could the function also have been called
# with length 5 and width 3
c3 = circumference(5, 3)
print(c3)

# you can even change the order of keyword parameters
# try it: Change the order of  parameters!
c4 = circumference(width=3, length=5)    # keyword parameter order swapped!
print(c4)
