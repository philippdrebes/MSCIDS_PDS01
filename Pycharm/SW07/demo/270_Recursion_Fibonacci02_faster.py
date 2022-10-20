#!/usr/bin/env python3

# 270_Recursion_Fibonacci02_faster.py
# Example 7: Fibonacci sequence with recursion much faster ....
# This version of Fibonacci computation is
# much faster because it remembers interim results

# "Trick": we save already calculated Fibo values in one Dictionary 'memo':

memo = {0:0, 1:1}
def fibo_memo(n):
    if not n in memo:       # n = 0 and n = 1 are safely skipped (at the end)
                            # because these values are already contained
                            # in the dictionary 'memo'
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]


fibo_list = []
n = 12
for i in range(0,n):
    fibo_list.append(int(fibo_memo(i)))
print(fibo_list)

#########
# Output:
#########
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
