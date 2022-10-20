# Generator05_Intro.py

# Source: https://wiki.python.org/moin/Generators

##############
# Start point: Without any 'Generator' / 'Iterator'
##############

# First task: Let us consider the simple example of building
# a list and returning it.
# Second task: Build the sum of all numbers of this list!

def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(firstn(10))

sum_of_first_n = sum(firstn(10))
print("sum(firstn(10)): ", sum_of_first_n)


# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum(firstn(10)):  45

