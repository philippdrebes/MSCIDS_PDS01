# Iterator01.py

# Quelle: https://www.journaldev.com/14620/python-iterator
# easily supplemented / changed!


# Task: Solve the 6 Task's below!
#       First try to understand what happens => e.g. fill out the Task 1 - Task 3
#       with good and correct comments!!

list_string = ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']
print("list_string:", list_string)                # Task 1: ********** to do ************
myIterator1 = iter(list_string)                   # Task 2: ********** to do ************
print(myIterator1)                                # proof 1 for line above!
print("type(myIterator1): ", type(myIterator1))   # proof 2 for two lines above!


# 'iterator' points to the first student*in
output1 = next(myIterator1)                       # Task 3: ********** to do ************
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


# Task 4: how can we throw a 'StopIteration' exception?
# output1 = ********** to do ************

# This print will execute => once more 'student*in 5'
print("'output1' once more:", output1)


# Task 5: How can we iterate once more over the list 'list_string'?
print("*" * 50)
# myIterator1 =  ********** to do ************    # comment out!!!


# Task 6: advanced!
# How can we get back the third-element the list 'list_string'?
# Hint: https://stackoverflow.com/questions/2300756/get-the-nth-item-of-a-generator-in-python

# output1 =   ********** to do ************       # student*in 3 is the solution
print(output1)                                    # student*in 3 is the solution

# Goal - Output: ( Task 4 is commented out!)
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
