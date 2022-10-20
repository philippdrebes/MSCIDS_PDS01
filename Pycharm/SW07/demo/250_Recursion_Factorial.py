#!/usr/bin/env python3

# 250_Recursion_Factorial.py
# Example 5: Factorial with Recursion
# in principle EXACTLY (!!!) the same as the 'mult ()' function in the last example!)
# just written more elegantly!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

res = factorial(5)
print(res)


#########
# Output:
#########
# 120