# Generator08_Expression.py

# Quelle: https://wiki.python.org/moin/Generators

#############
# Third way: We use a 'Generator Expression' to create a 'generator'!
#            => looks like a 'list comprehension with ( ) instead of []
#############

# list comprehension
print("n1_list ***: n1_list is a list")
n1_list = [n for n in range(10)]
print(n1_list)
print(type(n1_list))
print(sum(n1_list))
print()

# same as the list comprehension above => but now a 'Generator Expression'!!!
print("n2_gen ***: n2_gen is a Generator")
n2_gen = (n for n in range(10))          # ( ...) => Generator Expression!!!
print(n2_gen)
print(type(n2_gen))
print(sum(n2_gen))
print()

# same as above 'short'! => Generator Expression!!!
print("n3 ***: n3 is a 'int' (result of 'sum()' ")
n3 = sum(list(n for n in range(10)))
print(n3)
print(type(n3))


# Output:
# n1_list ***: n1_list is a list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# <class 'list'>
# 45
#
# n2_gen ***: n2_gen is a Generator
# <generator object <genexpr> at 0x0000027FC179AF20>
# <class 'generator'>
# 45
#
# n3 ***: n3 is a 'int' (result of 'sum()'
# 45
# <class 'int'>
