# some more examples for map(), filter(), reduce()



##########################################################################################
# map() examples:
print(1, list(map(lambda var: var*2,range(0,10))))         # nimm 0 => 0*2 = 0 => speichere in Liste
                                                           # nimm 1 => 1*2 = 2 => speichere in Liste


print(2, list(map(lambda var: var%2 == 0, range(0,10))))   # nimm 0 => 0%2 == 0 ist 'true' => speichere in liste!
                                                           # nimm 1 => 1%2 == 0 ist 'false' => speichere nicht in liste! usw.
                                                           # nimm 2 => 2%2 == 0 ist 'true' => speichere in liste! usw.


##########################################################################################
# filter() examples:
# Rule:
# wenn die 'callback-fuction' (lambda ...) mit dem x-ten Wert der liste (range (...)) TRUE ergibt, dann nehmen!

print(3, list(filter(lambda var: var*2,range(0,10))))        # nimm 0 => ist 0*2  true/false => false also nimm es nicht!
                                                             # nimm 1 => ist 1*2 != 0 ja => true (nimm die Zahl) usw.


print(4, list(filter(lambda var: var%2 == 0, range(0,10))))  # nimm 0 => 0%2==0 true/false? => True also aufnehmen in list
                                                             # nimm 1 => 1%2==0 true/false? => false d.h. nicht aufnehmen! usw.

##################################
# a first biger filter example:
# a function that returns True if letter is vowel

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)     # first paramter (a function)  has to return True or False!!!!!
print(5, filtered_vowels)
# converting to tuple
vowels = list(filtered_vowels)
print(6, vowels)

##################################
# filter => second example:
# random list
# filter all elements which don't evaluate to FALSE: e.g. 1 => true, 'a' => true, 0 => false, False => false
#                                                              True => true, '0' (a character!) => true
random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)
print(7, type(filtered_iterator))
#converting to list
filtered_list = list(filtered_iterator)

print(8, filtered_list)

##########################################################################################
# reduce() examples
fibo = [1,1,2,3,5,8,13,21,34]

import functools
fibosum = functools.reduce(lambda x,y: x+y, fibo)
print(8, fibosum)

fibomult = functools.reduce(lambda x,y: x*y, fibo)
print(9, fibomult)



# result:
# 1 [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# 2 [True, False, True, False, True, False, True, False, True, False]
# 3 [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 4 [0, 2, 4, 6, 8]
# 5 <filter object at 0x000001C5141FDE20>
# 6 ['a', 'e', 'i', 'o']
# 7 <class 'filter'>
# 8 [1, 'a', True, '0']
# 8 88
# 9 2227680
