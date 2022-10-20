# filename must be test*.py     in pytest- Tests!!!    => test_functions_with_pytest.py

# first: install pytest in your virtual - environment!
# pip install pytest

import pytest
from FuncPackage.functions import my_sum


class TestMySum:

    def test_my_sum_list(self):  # method names must start with "test" so the test runner discovers them.
        assert my_sum([1, 2, 3]) == 6, "Should be 6"

    def test_my_sum_tuple(self):
        assert my_sum([1, 2, 3, 4]) == 10, "Should be 10"



# Mae FS2022

    def test_more_example(self):
        assert "loud noises".upper() == "LOUD NOISES"
        assert list(reversed([1,2,3,4])) == [4,3,2,1]
        assert 37 in {
            num
            for num in range(1,50)
            if num != 1 and not any([num % div ==0 for div in range(2,num)])
        }


# only for didactical reasons => can be commented out when everthing is clear!
# .... and WAUUUU:  in pytest this lines are NOT printed => the are NO test's!!!!
print("***********************************************************************************")
print("'Script'-Printout: _03_PyTest_Automated/test_functions_with_pytest.py was called!!!")
print("***********************************************************************************")







# or shorter: Go to File > Settings... > Tools > Python integrated tools > Testing
#             and choose as 'Default Test Runner':  pytest
#             You get a message to install a "TestRunner" => Fix (let it fix ;-)! )
