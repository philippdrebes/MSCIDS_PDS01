# Iterator03_Extended_Solution.py

# Idea form: https://www.journaldev.com/14620/python-iterator
# with some supplements

list_string = ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']

# Task 1:  Try to follow the next lines ... inspect the generated output.
##########
myIterator1 = iter(list_string)
print("myIterator1 = iter(list_string)")
print("iter(list_string):           ", myIterator1)
print("type(myIterator1):           ", type(myIterator1))
print("iter(myIterator1):           ", iter(myIterator1))        # => myIterator1 is also an iteralbe
print("type(iter(myIterator1)):     ", type(iter(myIterator1)))

# Task 2:  Try to follow the evidence:  An iterator is also iterable ....!
##########
# 1. list_string is an interable and also a sequence
# 2. iter(list_string) { == myIterator1 } gives back an list_iterator object  at 0x00000183301E3B20
# 3. iter(iter(list_string)) { ==iter(myIterator) } gives back an list_iterator object  at 0x00000183301E3B20
# 4. iter(list_string) == iter(iter(list_string) => iter(list_string) {==MyIterator1} has to be ALSO an interable!!!


print("***************************************************************")


# Task 3: Get the first element in list_string (easy!)
##########
output1 = next(myIterator1)     # ********** to do ************

# Task 4: Print out the value of 'output1'
##########
# ********** to do ************
print("1) next(myIterator1): ", output1)               # This will print 'student*in 1'


# Task 5: Change the values on position 1,2 and 3 in the list 'list_string[0 to 2]' to 'girl 1' and so on.
##########
list_string[0] = "girl 1"         # ********** to do ************
list_string[1] = "girl 2"         # ********** to do ************
list_string[2] = "girl 3"         # ********** to do ************

# Task 6: Does the iterator 'myIterator1' notice the change???? Proof it!
##########
# Answer: Yes !   # ********** to do ************
# Proof:
# point the next student*in, the second student*in of myIterator1

print("1) next(myIterator1): ", next(myIterator1))      # This will print 'girl 2'
print("2) next(myIterator1): ", next(myIterator1))      # This will print 'girl 3'
print("3) next(myIterator1): ", next(myIterator1))      # This will print 'student*in 4'
print("4) next(myIterator1): ", next(myIterator1))      # This will print 'student*in 5'


print("***************************************************************")

# Task 7: Create a second iterator 'myIterator2' of the list 'list_string'
##########
myIterator2 = iter(list_string)


# Task 8: Give out all values of our iterable with the iterator 'myIterator2'
##########

# ********** to do ************
print("0) next(myIterator2): ", next(myIterator2))     # This will print 'girl 1'
print("1) next(myIterator2): ", next(myIterator2))     # This will print 'girl 2'
print("2) next(myIterator2): ", next(myIterator2))     # This will print 'girl 3'
print("3) next(myIterator2): ", next(myIterator2))     # This will print 'student*in 4'
print("4) next(myIterator2): ", next(myIterator2))     # This will print 'student*in 5'

# myIterator1 = iter(list_string)
# iter(list_string):            <list_iterator object at 0x000002235DA73B20>
# type(myIterator1):            <class 'list_iterator'>
# iter(myIterator1):            <list_iterator object at 0x000002235DA73B20>
# type(iter(myIterator1)):      <class 'list_iterator'>
# ***************************************************************
# 1) next(myIterator1):  student*in 1
# 1) next(myIterator1):  girl 2
# 2) next(myIterator1):  girl 3
# 3) next(myIterator1):  student*in 4
# 4) next(myIterator1):  student*in 5
# ***************************************************************
# 0) next(myIterator2):  girl 1
# 1) next(myIterator2):  girl 2
# 2) next(myIterator2):  girl 3
# 3) next(myIterator2):  student*in 4
# 4) next(myIterator2):  student*in
