# solution exercise 02


def my_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def main():
    print(my_sum((8, 2, 3, 0, 7)))
    print(my_sum((18, 2, 13, 0, 7)))

if __name__ == "__main__":
    main()


 
