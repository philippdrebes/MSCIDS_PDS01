def add(val1, val2):
    return val1 + val2


def multiply(val1, val2):
    return val1 * val2


def subtract(val1, val2):
    return val1 - val2


def divide(val1, val2):
    return val1 / val2


if __name__ == '__main__':
    while True:
        val1 = int(input('Please enter first number: '))

        print('Select operation.')
        print('1.Add')
        print('2.Subtract')
        print('3.Multiply')
        print('4.Divide')
        print('Q.Quit')

        choice = input('Enter choice(1/2/3/4/Q): ')
        if choice.lower() == 'q':
            break

        val2 = int(input('Please enter second number: '))

        res = 0

        if choice == '1':
            res = add(val1, val2)
        elif choice == '2':
            res = subtract(val1, val2)
        elif choice == '3':
            res = multiply(val1, val2)
        elif choice == '4':
            res = divide(val1, val2)

        print('Result: ', res)
