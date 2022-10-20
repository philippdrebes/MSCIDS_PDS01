# Iterator01_Solution.py

# Quelle: https://www.journaldev.com/14620/python-iterator
# easily supplemented / changed!

# Task: Solve the six task's below!
#       First try to understand what happens => e.g. fill out all task in the comments!!

list_string = ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']
print("list_string:", list_string)               # Task 1: list_string is a 'iterable'
myIterator1 = iter(list_string)                  # Task 2: myIterator1 is a 'iterator'-object
print(myIterator1)                               # proof 1 for line above!
print("type(myIterator1): ", type(myIterator1))  # proof 2 for two lines above!


# 'iterator' points to the first student*in
output1 = next(myIterator1)                     # Task 3: get the first element in the sequence (list)
# This will print 'student*in 1'
print("next(myIterator1): ", output1)

# point the next student*in, the second student*in
output1 = next(myIterator1)
# This will print 'student*in 2'
print("next(myIterator1): ", output1)

# point the next student*in, the third student*in
output1 = next(myIterator1)
# This will print 'student*in 3'
print("next(myIterator1): ", output1)

# point the next student*in, the fourth student*in
output1 = next(myIterator1)
# This will print 'student*in 4'
print("next(myIterator1): ", output1)

# point the next student*in, the fifth student*in
output1 = next(myIterator1)
# This will print 'student*in 5'
print("next(myIterator1): ", output1)

# point the next student*in, but there is no student*in left
# so raise 'StopIteration' exception

# Task 4: how can we throw a 'StopIteration' exception?
# output1 = next(myIterator1)

# This print will execute => once more 'student*in 5'
print("'output1' once more:", output1)


# Task 5: How can we iterate once more over the list 'list_string'?
print("*" * 50)
myIterator1 = iter(list_string)


# Task 6: advanced!
# How can we get back the third-element the list 'list_string'?
# Solution: For example with a list comprehension ...
# Hint: https://stackoverflow.com/questions/2300756/get-the-nth-item-of-a-generator-in-python

output1 = next((x for i, x in enumerate(myIterator1) if i == 2), None)
print(output1)

# Output: (without Task 4)
# list_string: ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']
# <list_iterator object at 0x000002253CC43730>
# type(myIterator1):  <class 'list_iterator'>
# next(myIterator1):  student*in 1
# next(myIterator1):  student*in 2
# next(myIterator1):  student*in 3
# next(myIterator1):  student*in 4
# next(myIterator1):  student*in 5
# 'output1' once more: student*in 5
# **************************************************
# student*in 3
