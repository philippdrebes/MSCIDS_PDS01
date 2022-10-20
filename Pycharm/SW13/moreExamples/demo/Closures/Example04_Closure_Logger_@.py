# Example04_Closure_Logger_@.py

# Python program to illustrate Closures und Decorator
# in one example

import logging

logging.basicConfig(filename='example_Bsp04.log', level=logging.INFO)


def logger(func):                 # this function is a Closure!!!
    #                             # AND a callable that takes another function as argument
    #                             # the name of such a function is: "Decorator"
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func               # Necessary for closure to work (returning WITHOUT parenthesis)


@logger                           # the function 'add' is decorated with logger
def add(x, y):
    return x + y

# Question:     What is the goal of the '@' sign???
# try it out:   Comment out the 3 lines above and
#               uncomment the lines below ... follow the comments!


# def add(x, y):
#     return x + y
#
# print(add(13,15))            # no entry in log-file!  (IMPORTANT!!!)
#
# add = logger(add)            # from now on => We have also an entry in the log-file!
#                              # The 'add'-funcion on the right site is 'decorated'
#                              # with 'logger'-function!!!!!
#                              # from now on => We have on the left site a
#                              # 'decorated add'-function ... with logger-infos!!
#
# add(33,35)                   # => have a lock in the log file! add (...) is now 'decorated!
#                              # IMPORTANT: Use add(...) without a print(...) function surround
#                              # => else 'None' as return-value in the output


@logger
def sub(x, y):
    return x - y


def main():

    add(3, 3)
    add(4, 5)

    sub(10, 5)
    sub(20, 10)
    logging.info('End of program! *************************************************' )


if __name__ == '__main__':
    main()
