# Generator03_Expression.py

# an example (advanced!) for the use of generator expressions

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

# def squares():             # replaced with Pythagoras example below!
#     for i in integers():
#         yield i * i


def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.__next__())
    except StopIteration:
        pass
    return result


def main():
    # Pythagoras example with take () function in action!
    pyt = ((x, y, z) for z in integers() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)
    print(take(10, pyt))


if __name__ == "__main__":
    main()
