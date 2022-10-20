#!/usr/bin/env python3

# 210_Count_to_10_recursive.py
# Intro in recrusion
# Most DataScientists do not fully understand recursion right away.
# The principle is clear ... but the consequences of a recursive call are not.

# Therefore an ABSOLUTE MUST: Visit the awesome (!) website:

# http://pythontutor.com/visualize.html#mode=edit

# Paste the recursive code there.
# With this tool you can still see the recursion 'optically'
# much more plausible than with the PyCharm debugger!


# Question: What we do to start?
# Answer: We count from a number e.g. 7 to 10 without a loop!
# Target Output:
# 7
# 8
# 9
# 10

# Example 1: count from e.g. 7 to 10

def CountTo (count):
  if (count <= 10):
    print(count)            # output
    CountTo (count + 1)     # recursion


CountTo(7)                  # change the number e.g. to -3 or 4 and so on


#########
# Output:
#########
# 7
# 8
# 9
# 10