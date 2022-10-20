# Iterator02_with_Errorhandling_Solution.py

# Quelle: https://www.journaldev.com/14620/python-iterator
# same example as 'Bsp01_Iterator.py' BUT with error-handling!

# Task 1:  try to change this code so that we don't get an error
#          => implement an 'exceptionhandling'!

list_string = ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']

print("list_string:", list_string)
myIterator1 = iter(list_string)
print(myIterator1)
print("type(myIterator1): ", type(myIterator1))

# point the first student*in
output1 = next(myIterator1)
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

# Your Task 1:   ********** to do ************
# Implement a 'exceptionhandling'!!!

# Try in PyCharm Ctr+Alt+T  => Surround with ....  => Woow!
try:
    output1 = next(myIterator1)
    print("6. Ausgabe: ")       # never reached with our list!
except StopIteration as si_err:
    print("Exceptionhandling: ", si_err.__repr__())
    #  print(repr(si_err))      # dito!


# This print will execute => once more 'student*in 5'
print("'output1' once more:", output1)


# desired Output:
# list_string: ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']
# <list_iterator object at 0x000001CB18623730>
# type(myIterator1):  <class 'list_iterator'>
# next(myIterator1):  student*in 1
# next(myIterator1):  student*in 2
# next(myIterator1):  student*in 3
# next(myIterator1):  student*in 4
# next(myIterator1):  student*in 5
# Exceptionhandling:  StopIteration()
# 'output1' once more: student*in 5
