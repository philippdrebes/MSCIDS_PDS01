#!/usr/bin/env python3

# 220_Count_from_10_recursive.py
# Example 2 : count form  10 to 'count'-Parameter e.g. 7 and print out the numbers

def CountToTen (count):
  if (count <= 10):
    CountToTen (count + 1)     # recursion
    print(count)               # output


CountToTen(7)


# important: Have a look what has changed in the code?
#            Do you understand why a little change has so much 'impact'?


#########
# Output:
#########
# 10
# 9
# 8
# 7