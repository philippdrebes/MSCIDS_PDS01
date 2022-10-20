# comprehensions.py


# Task 1 #######################################################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums   (something like a 'copy'!
print("\nfor n in nums => Loop:")
# my_list01 = []
# better:
my_list01 = []
for n in nums:
  my_list01.append(n)
print("my_list01: ", my_list01)


# Task 01: programm the same output as above with a 'list comprehension':
#
# your work!
#
#


# Task 2 #######################################################################
# I want 'n*n' for each 'n' in nums
my_list02 = []
for n in nums:
  my_list02.append(n*n)
print("my_list02: ", my_list02)

# Task 02: programm the same output as above with a 'list comprehension':
#
# your work!
#
#


# Task 3 #######################################################################
# Using a map + lambda
# have a short look on https://www.python-course.eu/python3_lambda.php => map()
# or consult the original docu!

print("\nwith map + lambda + for-Loop:")
myMap = map(lambda n: n*n, nums)
my_list03 = []
for item in myMap:
  my_list03.append( item )
print("my_list03: ",my_list03)


# Task 03: programm the same output as above ('with map + lambda + for-Loop') with a 'list comprehension':
#
# your work!
#
#

# Task 4: try to understand!  #################################################
# shorter if the result of map () is immediately converted into a list:
print("\nwith list + map + lambda:")
my_list04 = list(map(lambda n: n*n, nums))
print("my_list04: ", my_list04)




# Task 5 #######################################################################
# I want 'n' for each 'n' in nums if 'n' is even
print("\n'n' for each 'n' in nums if 'n' is even:")
my_list05 = []
for n in nums:
  if n%2 == 0:
    my_list05.append(n)
print("my_list05: ", my_list05)


# Task 05: programm the same output as above with a 'list comprehension':
#
# your work!
#
#



# Task 6: try to understand!  #################################################
# Using a filter + lambda
# The function 'filter (pFunc, pList)' offers an elegant
# possibility to filter out those elements from a list 'pList' (parameter-list)
# for which the function 'pFunc' a 'True'
# returns.
# We will convert the 'filter object'immediately to 'list' with list(....)!

print("\nlist + filter + lambda :")
my_list06 = list(filter(lambda n: n%2 == 0, nums))    # lambda  => pFunc ; nums => pList
print("my_list06: ",my_list06)


# Task 7 #######################################################################
# We want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
print("\nfor letter in 'abcd' and for num in range(4) build tupels :")
my_list07 = []
str01 = 'abcd'
ran01 = range(4)
for letter in str01:
  for num in ran01:
    my_list07.append((letter,num))
print("my_list07: ",my_list07)



# Task 07: programm the same output as above with a 'list comprehension':
#
# your work!
#
#


