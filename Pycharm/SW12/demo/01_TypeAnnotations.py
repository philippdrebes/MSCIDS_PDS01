# 01_TypeAnnotations.py  (mae)

# only intro: function WITHOUT type annotation (already possible without any problems before Python 3.5)


def f(x, y):
    return x * y


# various examples that call this function "dynamically" / generically

try:
    print("f(3, 4):", f(3, 4))
    print("f(3.69, 11.39):", f(3.69, 11.39))
    print("f(25, '-'):", f(25, '-'))
    print("f('-', 25):", f('-', 25))
    print("f([3,5],2):", f([3, 5], 2))
    print("f('a','-'):", f('a', '-'))    # this line throws an error which is caught!
except TypeError as e:
    print(e)


print("Program normal finished!")

print("5*4:", 5*4)
