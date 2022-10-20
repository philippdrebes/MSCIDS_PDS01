# Bsp04_Generator_more_Solution.py

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


def take(n, seqGen):
    """Returns first n values from the given sequence."""
    # print("type(seqGen):", type(seqGen))
    result = []
    try:
        for i in range(n):
            result.append(next(seqGen))
    except StopIteration:
        pass
    return result


def main():
    gen = iter(squares())
    print(take(5, gen))
    print(take(5, gen))
    print(take(4, gen))
    print(take(10, gen))


if __name__ == "__main__":
    main()

# Output:
# [1, 4, 9, 16, 25]
# [36, 49, 64, 81, 100]
# [121, 144, 169, 196]
# [225, 256, 289, 324, 361, 400, 441, 484, 529, 576]
