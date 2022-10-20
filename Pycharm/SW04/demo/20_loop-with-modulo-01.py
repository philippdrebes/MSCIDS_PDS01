#!/usr/bin/env python3


def demo_while_with_modulo():
    row = 10
    col = 5
    i = 1
    while i <= row * col:
        print("x", end="")
        if i % col == 0:
            print()
        i += 1


if __name__ == "__main__":
    demo_while_with_modulo()
 