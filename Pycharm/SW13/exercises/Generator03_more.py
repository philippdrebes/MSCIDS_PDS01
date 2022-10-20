# Bsp04_Generator_more.py

# Task:
#######
# Complete the program (script) so that a main() function is used to start it.
# In addition, the next square numbers should always be returned
# =>  not always the same square numbers
# Modify the program to meet this requirement.
# e.g. Output:
# [1, 4, 9, 16, 25]
# [36, 49, 64, 81, 100]

def integers():          # generator-function!
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1


def squares():           # also a generator-function
    for i in integers():
        yield i * i      # why not 'return'? Discuss!!!


def take(n, seq):
    """Returns first n values from the given sequence."""
    seqGen = iter(seq)
    # print("type(seqGen):", type(seqGen))
    result = []
    try:
        for i in range(n):
            # result.append(seqGen.__next__())   # object-oriented ... ;-)
            result.append(next(seqGen))        # old fashion notation => often used!
    except StopIteration:
        pass
    return result


print(take(5, squares()))
print(take(5, squares()))

# Output:
# [1, 4, 9, 16, 25]
# [1, 4, 9, 16, 25]
