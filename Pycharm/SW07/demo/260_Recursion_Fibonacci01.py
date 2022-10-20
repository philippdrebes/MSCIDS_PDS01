#!/usr/bin/env python3

# 260_Recursion_Fibonacci01.py
# Example 6: Generate the fist 'n' numbers of a fibonacci-sequence
# Up to n = 30 it is OK in terms of performance. Then it starts to get very slow.
# Reason: Certain parts of the fibonacci-tree are calculated multiple times

# try yourself to change the nummer of 'n' !

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fibo_list = []
n = 12
for i in range(0,n):
    fibo_list.append(int(fib(i)))

print(fibo_list)

#########
# Output:
#########
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]