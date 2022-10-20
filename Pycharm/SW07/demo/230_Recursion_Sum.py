#!/usr/bin/env python3

# 230_Recursion_Sum.py
# Example 3: Sum with Recursion  => sum(n)
# Build the sum of all numbers from 1 to n
# Try also 'pythontutor.com/visualize.html'!

total=0

def sum(x):
    global total
    if x == 0:
        pass
    else:
       total = total + x
       x -= 1
       print("total - before sum(x): ", total)
       sum(x)                   # Recursion => loop without for or while!
       print("total - after sum(x): ", total)  # we see this output 6 times ... why?
    return total

res = sum(5)

print(res)

#########
# Output:
#########
# total - before sum(x):  5
# total - before sum(x):  9
# total - before sum(x):  12
# total - before sum(x):  14
# total - before sum(x):  15
# total - after sum(x):  15
# total - after sum(x):  15
# total - after sum(x):  15
# total - after sum(x):  15
# total - after sum(x):  15
# 15