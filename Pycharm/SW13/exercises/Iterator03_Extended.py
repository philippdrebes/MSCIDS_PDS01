# Iterator03_Extended.py

# Idea form: https://www.journaldev.com/14620/python-iterator
# with some supplements

list_string = ['student*in 1', 'student*in 2', 'student*in 3', 'student*in 4', 'student*in 5']

# Task 1:  Try to follow the next lines ... inspect the generated output.
##########
myIterator1 = iter(list_string)
print("myIterator1 = iter(list_string)")
print("iter(list_string):           ", myIterator1)
print("type(myIterator1):           ", type(myIterator1))
print("iter(myIterator1):           ", iter(myIterator1))        # => myIterator1 is also an iterable
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
output1 = 1  # ********** to do ************ delete the '1'!

# Task 4: Print out the value of 'output1'
##########
# ********** to do ************            # This will print 'student*in 1'


# Task 5: Change the values on position 1,2 and 3 in the list 'list_string[0 to 2]' to 'girl 1' and so on.
##########
list_string[0] = 1       # ********** to do ************ delete the '1'!
list_string[1] = 1       # ********** to do ************ delete the '1'!
list_string[2] = 1       # ********** to do ************ delete the '1'!

# Task 6: Does the iterator 'myIterator1' notice the change???? Proof it!
##########
# Answer:   ********** to do ************
# Proof:    Output of all values in the list with the iterator 'myIterator1':

# ********** to do ************
# ********** to do ************
# ********** to do ************
# ********** to do ************


print("***************************************************************")

# Task 7: Create a second iterator 'myIterator2' of the list 'list_string'
##########

# ********** to do ************


# Task 8: Give out all values of our iterable list with the iterator 'myIterator2'
##########

# ********** to do ************
# ********** to do ************
# ********** to do ************
# ********** to do ************
# ********** to do ************

# GOAL - Output:
###############
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
# 4) next(myIterator2):  student*in 5
