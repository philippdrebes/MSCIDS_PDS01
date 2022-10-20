# Iterator06_How2Create.py

from itertools import count


# Frist: We can create our one Iterator with a class:
class square_all_class:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self


# Second option of a Iterator-Creation with a function:
def square_all_func(numbers):
    for n in numbers:
        yield n ** 2


# Third option of a Iterator-Creation with a generator expression
def square_all_gen(numbers):
    return (n**2 for n in numbers)


def main():
    numbers = count(5)
    print(numbers)
    print(type(numbers))
    square_class = square_all_class(numbers)
    print(next(square_class))
    print(next(square_class))
    print(next(square_class))
    print(next(square_class))

    print("*" * 60)

    square_func = square_all_func(numbers)
    print(next(square_func))
    print(next(square_func))
    print(next(square_func))
    print(next(square_func))

    print("*" * 60)

    square_gen = square_all_gen(numbers)
    print(next(square_gen))
    print(next(square_gen))
    print(next(square_gen))
    print(next(square_gen))


if __name__ == "__main__":
    main()


# Output:
# count(5)
# <class 'itertools.count'>
# 25
# 36
# 49
# 64
# ************************************************************
# 81
# 100
# 121
# 144
# ************************************************************
# 169
# 196
# 225
# 256
