# 02_RoboterCallable.py

# Example how to make an object "callable":
# We define in the RoboterCallable class a method __call__(....)


class RoboterCallable:                           # a class in module '02_RoboterCallable.py'
    def __init__(self):
        print("__init__() aufgerufen")

    def __call__(self, *args):                 # '*' means 0 to n arguments (variadic function)
        if args.__len__() == 0:
            print("no arg!")
        else:
            print(args[args.__len__()-1])      # print allways last argument!

    def hallo_method(self, para="Class HSLU"):   # method of class "RoboterCallable"!!!
        print(para)


def hallo_function(self, para="Function HSLU"):  # a 'module-function'!
    print(para)


def main():                                      # a 'module-fuction'!
    func = RoboterCallable()
    print(func)
    print("type(func):", type(func))   # func is a object of class Roboter!
    print("callable(hallo_function):", callable(hallo_function))
    print("callable(hallo_method):", callable(func.hallo_method))
    print("callable(func):", callable(func))
    func.hallo_method( "Grüezi!" )

    print("~"*40)
    func()                      # without __call__-funcion in class  => error!!!
    func("1111")
    func("1111","222")
    func("1111","222", 3)
    print(type(func("1111")))   # <class 'NoneType'>  ... Woow!

if __name__ == '__main__':
    main()


# Result:  => # if 'def __call__(...) is commented out!!!
# __init__() aufgerufen
# <__main__.RoboterCallable object at 0x0000023B8465C1F0>
# type(func): <class '__main__.RoboterCallable'>
# callable(hallo_function): True
# callable(hallo_method): True
# callable(func): False
# Grüezi!
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Result:  => # if 'def __call__(...) is NOT commented out!!!
# __init__() aufgerufen
# <__main__.RoboterCallable object at 0x000002ECE408C1F0>
# type(func): <class '__main__.RoboterCallable'>
# callable(hallo_function): True
# callable(hallo_method): True
# callable(func): True
# Grüezi!
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# no arg!
# 1111
# 222
# 3
# 3
# <class 'NoneType'>
