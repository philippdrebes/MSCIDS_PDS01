#!/usr/bin/env python3

# 240_Recursion_Mult.py
# Example 4: Mult with Recursion  => mult(n)
# Multiply all numbers from 1 to n
# Try also 'pythontutor.com/visualize.html'!


total=1

def mult(x):
    global total
    if x == 1:
        pass
    else:
       total = total * x
       x -= 1
       print("total - befor mult(x): ", total)
       mult(x)                   # Recursion => loop without for or while!
       print("total - after mult(x): ", total)   # we see this output 5 times ... why?
    return total

res = mult(5)

print(res)

#########
# Output:
#########
# total - befor mult(x):  5
# total - befor mult(x):  20
# total - befor mult(x):  60
# total - befor mult(x):  120
# total - after mult(x):  120
# total - after mult(x):  120
# total - after mult(x):  120
# total - after mult(x):  120
# 120