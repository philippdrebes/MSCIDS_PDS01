# Example01_CallableIntro.py

# Quelle:  https://stackoverflow.com/questions/111234/what-is-a-callable

# A callable is an object allows you to use round parenthesis ( )
# and eventually pass some parameters, just like functions.
#
# Every time you define a function python creates a callable object.
# In example, you could define the functions func1/func2 in these
# ways (it's the same):

# more about callable:
# Quelle: https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/


class A:
    def __call__(self, *args):
        print('Hello1')


func1 = A()
print(func1)            # <__main__.A object at 0x000001DB41AEC1F0>
print(type(func1))      # func1 is a object of <class '__main__.A'>

func1()                 # Hello1    => object of class A is here 'callable'!
print(callable(func1))  # True

print("~" * 40)
# or ... every function is a callable!


def func2(*args):
    print('Hello2')

print(func2)
print(type(func2))      # <class 'function'>
func2()                 # Hello2
print(callable(func2))  # True

# <__main__.A object at 0x000001EEFF44C1F0>
# <class '__main__.A'>
# Hello1
# True
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# <function func2 at 0x000001EEFF4A6790>
# <class 'function'>
# Hello2
# True
