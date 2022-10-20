#!/usr/bin/env python3


def demo_nested_for():
    row = 10
    col = 5

    for r in range(1, row + 1):
        for c in range(1, col + 1):
            print("x", end="")
        print()


if __name__ == "__main__":
    demo_nested_for()
 