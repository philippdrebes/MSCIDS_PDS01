import math


def exercise1():
    print('Exercise 1')
    values = [(2, 7, 3, 5), (1, 5, 2), (4, 1, 8, 6, 2, 4), (2, 3), (2, 1), (0, 3, 5, 2, 0)]
    print(values)
    values.sort(key=lambda x: x[-1])
    print(values)


def exercise2():
    print('Exercise 2')
    values = [(2, 7, 3, 5), (1, 5, 2), (4, 1, 8, 6, 2, 4), (2, 3), (2, 1), (0, 3, 5, 2, 0)]
    print(values)
    values.sort(key=lambda x: x[0])
    print(values)


def exercise3():
    print('Exercise 3')
    values = [(2, 7, 3, 5), (1, 5, 2), (4, 1, 8, 6, 2, 4), (2, 3), (2, 1), (0, 3, 5, 2, 0)]
    print(values)
    values.sort(key=lambda x: x[-2])
    print(values)


def exercise4():
    print('Exercise 4')
    values = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(values)
    values.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
    print(values)


def exercise5():
    print('Exercise 5')
    values = [(3, 7, 3, 5), (1, 5, 2), (3, 1, 8, 6, 2, 4), (2, 3), (2, 1), (0, 3, 5, 2, 0)]
    print(values)
    values.sort(key=lambda x: x[-2] % 2)
    print(values)


def exercise6():
    print('Exercise 6')
    values = [0, 1, 2, 3, 4, 5]
    for i in range(0, len(values), 2):
        tmp = values[i]
        values[i] = values[i + 1]
        values[i + 1] = tmp
    print(values)


def exercise7():
    print('Exercise 7')
    values = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    res = list()
    for e in values:
        if e:
            res.append(e)
    print(res)


def exercise8():
    print('Exercise 8')
    values = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(values)
    values.sort(key=lambda x: float(x[1]), reverse=True)
    print(values)


def exercise9():
    print('Exercise 9')
    values = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
              {"V": "S009"}]
    print(values)

    res = set()
    for e in values:
        for v in e.values():
            res.add(v)

    print(res)


def exercise10():
    print('Exercise 10')
    values = {5, 10, 3, 15, 2, 20}
    min_val = None
    max_val = None

    for i in values:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i

    print(f'MinVal = {min_val} MaxVal = {max_val}')


if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
