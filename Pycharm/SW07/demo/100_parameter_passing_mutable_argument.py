#!/usr/bin/env python3      # ;-)!!

# 100_parameter_passing_mutable_argument.py
# parameter passing with mutable argument  (here a list!)
# => side effects are possible => is usually seen as bad style!!! Therefore avoid!


def listAdder(liste):
    print( "Inside:   id(liste), liste, len(list):", id( liste ),liste, len(liste) )
    # liste += [47,11]
    # liste = liste + [47,11]     // dito
    # liste.extend([47,11])       // dito

    print( "Inside:   id(liste), liste, len(list)::", id( liste ),liste, len(liste) )


fib = [0,1,1,2,3,5,8]
print("Outside:  id(fib), fib, len(fib):", id(fib),",", fib, len(fib))

# adds a perfume (4711) to the 'fib' list ;-)
listAdder(fib)

print("Outside:  id(fib), fib, len(fib):", id(fib),",", fib, len(fib))

#########
# Output:
#########
# Outside:  id(fib), fib, len(fib): 2080578746624 , [0, 1, 1, 2, 3, 5, 8] 7
# Inside:   id(liste), liste, len(list): 2080578746624 [0, 1, 1, 2, 3, 5, 8] 7
# Inside:   id(liste), liste, len(list):: 2080578746624 [0, 1, 1, 2, 3, 5, 8] 7
# Outside:  id(fib), fib, len(fib): 2080578746624 , [0, 1, 1, 2, 3, 5, 8] 7