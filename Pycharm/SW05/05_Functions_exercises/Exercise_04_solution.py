# solution exercise 04

def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum


def main():
    print( is_even_num( [1, 2, 3, 4, 5, 6, 7, 8, 9] ) )

if __name__ == "__main__":
    main()
