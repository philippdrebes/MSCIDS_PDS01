# Generator01_Expression.py

# Quelle: https://anandology.com/python-practice-book/iterators.html

# Generator Expressions are generator version of list comprehensions.
# They look like list comprehensions, but returns a generator back
# instead of a list.

print("a1 ***: a1 is a list")
a1 = [x*x for x in range(10)]        # a1 is a list
print(type(a1))
print(a1)
print(sum(a1))
print()

print("a2 ***: a1 is a generator:")
a2 = (x*x for x in range(10))         # a2 is a generator-object
print(type(a2))
print(a2)
print(sum(a2))
print()


print("   ***: shortform ... of a2: ")
print(sum((x*x for x in range(10))))



# # We can use the generator expressions as arguments to various functions
# # that consume iterators. => Important for 'pandas'
#
# print(sum((x*x for x in range(10))))
#
#
# # When there is only one argument to the calling function,
# # the parenthesis around generator expression can be omitted.
#
# print(sum(x*x for x in range(10)))


# Output:
# a1 ***: a1 is a list
# <class 'list'>
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 285
#
# a2 ***: a1 is a generator:
# <class 'generator'>
# <generator object <genexpr> at 0x00000137D019AF20>
# 285
#
#    ***: shortform ... of a2:
# 285
