def add(matrix_a, matrix_b):
    print('Matrix A: {}'.format(matrix_a))
    print('Matrix B: {}'.format(matrix_b))

    if len(matrix_a) != len(matrix_b):
        print("can only add matrices of the same shape")
        return

    for row_index in range(len(matrix_a)):
        for col_index in range(len(matrix_a[row_index])):
            matrix_a[row_index][col_index] += matrix_b[row_index][col_index]

    return matrix_a


def multiply(matrix_a, matrix_b):
    print('Matrix A: {}'.format(matrix_a))
    print('Matrix B: {}'.format(matrix_b))

    if len(matrix_a) != len(matrix_b):
        print("cannot multiply those matrices")
        return

    result = [[0 for y in range(len(matrix_b[0]))] for x in range(len(matrix_a))]

    for row_index in range(len(matrix_a)):
        for col_index in range(len(matrix_b[0])):
            for x in range(len(matrix_b)):
                result[row_index][col_index] += matrix_a[row_index][x] * matrix_b[x][col_index]

    return result


if __name__ == "__main__":
    a = [
        [4, 5, 2],
        [7, 4, 3],
        [9, 4, 2],
    ]

    b = [
        [7, 2, 1],
        [1, 4, 8],
        [3, 9, 1],
    ]

    c = [
        [4, 5],
        [9, 9],
        [1, 0]
    ]

    print(add(a, b))
    print(multiply(a, c))
