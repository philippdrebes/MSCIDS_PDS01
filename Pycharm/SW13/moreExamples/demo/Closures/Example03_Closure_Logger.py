# Example03_Closure_Logger.py

# Quelle: https://www.geeksforgeeks.org/python-closures/

# Python program to illustrate closures
# closures  (and the use of logger-info in a file)


import logging

logging.basicConfig(filename='example_Bsp03.log', level=logging.INFO)


def logger(func):              # this function is a Closure!!!
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func            # Necessary for closure to work (returning WITHOUT parenthesis!)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def main():
    add_logger = logger(add)
    sub_logger = logger(sub)
    #                            # better would be  (in next example!)
    add_logger(3, 3)             # add(3,3)   => this would be the goal + loggin included!!!
    add_logger(4, 5)             # add(4,5)

    sub_logger(10, 5)
    sub_logger(20, 10)
    logging.info('End of program! *************************************************' )


if __name__ == '__main__':
    main()






