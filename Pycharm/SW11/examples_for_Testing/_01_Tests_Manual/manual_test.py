#!/usr/bin/env python3

from FuncPackage.functions import my_sum


def test_my_sum_list():
    assert my_sum([1, 2, 3]) == 6, "Test failed"


def test_my_sum_tuple():
    assert my_sum([1, 2, 3, 4]) == 10, "Test failed"


def main():
    test_my_sum_list()
    test_my_sum_tuple()


if __name__ == '__main__':
    print("in _01_Tests_manual/manual_test.py")
    main()
    print("All manual tests passed.")


# only for didactical reasons => can be commented out when everthing is clear!
print("****************************************************************")
print("'Script'-Printout: _01_Tests_manual/manual_test.py was called!!!")
print("****************************************************************")