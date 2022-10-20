def max_of_three(one, two, three):
    # return max(one, two, three)

    values = [one, two, three]
    maximum = values[0]
    for i in values[1:]:
        if i > maximum:
            maximum = i

    return maximum


def my_sum(values):
    # return sum(values)

    ret = 0;
    for i in values:
        ret += i

    return ret


def string_reverse(value):
    rev = ''
    for n in reversed(value):
        rev += n

    return rev


def is_even_num(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)

    return even


def unique_list(values):
    # return set(values)

    distinct = []
    for i in values:
        if i not in distinct:
            distinct.append(i)

    return distinct


if __name__ == '__main__':
    print('Exercise 1')
    print(max_of_three(3, 6, -5))

    print('Exercise 2')
    print(my_sum((8, 2, 3, 0, 7)))

    print('Exercise 3')
    print(string_reverse('1234abcd'))

    print('Exercise 4')
    print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print('Exercise 5')
    print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
