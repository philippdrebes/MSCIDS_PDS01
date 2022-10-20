# solution exercise 03

def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1


def main():
    print(string_reverse('1234abcd'))
    print('1234abcd'[::-1])


if __name__ == "__main__":
    main()
 