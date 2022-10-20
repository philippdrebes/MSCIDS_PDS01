# comprehensions_Solution.py


# Task 1 #######################################################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
print("\nfor n in nums => Schlaufe:")
my_list01 = []
for n in nums:
  my_list01.append(n)
print("my_list01: ", my_list01)


# Task 01: programm the same output as above with a 'list comprehension':
print ("\nList Comprehension01 => [n for n in nums] ",[n for n in nums])

# Task 2 #######################################################################
print("\nfor n in nums:")
# I want 'n*n' for each 'n' in nums
my_list02 = []
for n in nums:
  my_list02.append(n*n)
print("my_list02: ",my_list02)

# Task 02: programm the same output as above with a 'list comprehension':
print ("\nList Comprehension02 => [n*n for n in nums]:",[n*n for n in nums])


# Task 3 #######################################################################
# Using a map + lambda
# have a short look on page 310 chap. 30.2 => map()
# or consult the original docu!

print("\nwith map + lambda + for-Schlaufe:")
myMap = map(lambda n: n*n, nums)
my_list03 = []
for item in myMap:
  my_list03.append( item )
print("my_list03: ",my_list03)

# Task 03: programm the same output as above with a 'list comprehension':
print ("\nList Comprehension03 => [item for item in map(lambda n:n*n,nums)]:",[item for item in map(lambda n:n*n,nums)])

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
print ("\nList Comprehension05 => [n for n in nums if n%2==0]:",[n for n in nums if n%2==0])


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
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
print("\nfor letter in 'abcd' and for num in range(4) build tupels :")
my_list07 = []
str01 = 'abcd'
ran01 = range(4)
for letter in str01:
  for num in ran01:
    my_list07.append((letter,num))
print("my_list07: ",my_list07)

# Task 07: programm the same output as above with a 'list comprehension':
print("\nListComprehension08 =>  [(letter, num)for letter in str02 for num in ran02] :")
str02 = 'abcd'
ran02 = range(4)
my_list08 = [(letter, num)for letter in str02 for num in ran02]
print("my_list08: ",my_list08)


# ***************** More Example for later! ***********************************

# List Comprehensions mit 'zip()'   =>  list of tupel!!
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print("list(zip(names, heros)): ",list(zip(names, heros)))



# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict01 = {}
for name, hero in zip(names, heros):
    my_dict01[name] = hero
print("my_dict01: ", my_dict01)


# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set01 = set()          # leeres Set! => Jedes Element darf nur einmal in Set vorkommen!
for n in nums:
    my_set01.add(n)
print("my_set01: ",my_set01)
