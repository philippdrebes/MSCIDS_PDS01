# 06_TypeAnnotation_Callable_Solution.py

# 'Typing' also has a 'callable' and a 'union' type
# Errors in Mypy can e.g. on line 6 can be provoked with: float => int

# Question:
# How can you change the next program so that Mypy doesn't display any errors?
# The program works without any Problem ... but there is an error of thought!

# Answer: Change the second element of the Callable-List on line 15 to 'float'


from typing import Callable, Union     # Union is superfluous / not used in this example!

p1: Callable[[float], float]           # Mypy:  float instead of int
p2: Callable[[float], float]


def polynomial_creator(a: float, b: float, c: float) -> Callable[[float], float]:
    def polynomial(x: float) -> float:
        return a * x**2 + b * x + c
    return polynomial


p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))
