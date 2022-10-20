#!/usr/bin/env python3
#
# https://www.python-course.eu/python3_list_comprehension.php
#
# List Comprehension
# A more Demanding Example
#
# Calculation of the prime numbers between 1 and 100 using the sieve of
# Eratosthenes.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#


noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]

print("noprimes: ", noprimes)
print("primes: ", primes)


print("~" * 30)
# same without List Comprehension:

noprimes = []
primes = []

for i in range(2, 8):
    for j in range(i*2, 100, i):
        noprimes.append(j)

for x in range(2, 100):
    if x not in noprimes:
        primes.append(x)

print(primes)
