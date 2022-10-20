# solution exercise 05

def unique_list(a_list):
    result = []
    for element in a_list:
        if element not in result:
            result.append(element)
    return result


def main():
    print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
    print(set([1, 2, 3, 3, 3, 3, 4, 5]))


if __name__ == "__main__":
    main()
