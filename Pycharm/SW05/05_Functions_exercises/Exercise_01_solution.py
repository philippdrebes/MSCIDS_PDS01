# solution exercise 01


def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


def main():
    print(max_of_three(3, 6, -5))
    print(max_of_three(55, 23, 1))


if __name__ == "__main__":
    main()
