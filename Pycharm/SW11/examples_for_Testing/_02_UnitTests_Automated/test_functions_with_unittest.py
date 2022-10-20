# filename must be test*.py     in UnitTests  => test_functions_with_unittest.py

import unittest

from FuncPackage.functions import my_sum

class TestMySum(unittest.TestCase):
    def test_my_sum_list(self):  # method names must start with "test" so the test runner discovers them.
        self.assertEqual(my_sum([1, 2, 3]), 6, "Should be 6")

    def test_my_sum_tuple(self):
        self.assertEqual(my_sum([1, 2, 3, 4]), 10, "Should be 10")

if __name__ == '__main__':
    print("in _02_UnitTests_Automated/test_function_with_unittest.py")
    unittest.main()


# only for didactical reasons => can be commented out when everthing is clear!
print("***************************************************************************************")
print("'Script'-Printout: _02_UnitTests_Automated/test_function_with_unittest.py was called!!!")
print("***************************************************************************************")