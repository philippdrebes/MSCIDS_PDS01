#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

# https://docs.python.org/3/library
# https://docs.python.org/3/library/numeric.html

# https://docs.python.org/3/library/statistics.html
# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/pprint.html

# https://en.wikipedia.org/wiki/Harmonic_mean#Average_speed
# ...

import statistics as S
import random as rand
import pprint


def demo_statistics_1(arg=list(range(1, 11))):
    print("arg:", arg)
    print("mean:", S.mean(arg))
    print("median:", S.median(arg))
    print("harmonic_mean:", round(S.harmonic_mean(arg), 2))


def demo_random_1():
    a = list(range(10))
    rand.shuffle(a)
    print(a)


def demo_random_2():
    a = list(range(rand.randint(5, 15)))
    a.append(rand.randint(-3, 3))
    rand.shuffle(a)
    print(a)
    return {'min': min(a), 'mean': S.mean(a),
            'median': S.median(a), 'max': max(a), 'count': len(a)}


def demo_pprint_1():
    d = demo_random_2()
    pprint.pprint(d, indent=2, width=10)


if __name__ == "__main__":
    print("1)", "~" * 20)
    demo_statistics_1()
    demo_statistics_1((54, 24, 36))

    print("2)", "~" * 20)
    demo_random_1()

    print("3)", "~" * 20)
    print(demo_random_2())

    print("4)", "~" * 20)
    demo_pprint_1()

#
# 1) ~~~~~~~~~~~~~~~~~~~~
# arg: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mean: 5.5
# median: 5.5
# harmonic_mean: 3.41
# arg: (54, 24, 36)
# mean: 38
# median: 36
# harmonic_mean: 34.11
#
# 2) ~~~~~~~~~~~~~~~~~~~~
# [0, 9, 5, 8, 4, 6, 1, 3, 2, 7]
# 3) ~~~~~~~~~~~~~~~~~~~~
# [9, -1, 8, 6, 7, 3, 4, 0, 5, 2, 1]
# {'min': -1, 'mean': 4, 'median': 4, 'max': 9, 'count': 11}
# 4) ~~~~~~~~~~~~~~~~~~~~
# [0, 3, 4, 6, 2, 5, -1, 1]
# { 'count': 8,
#   'max': 6,
#   'mean': 2.5,
#   'median': 2.5,
#   'min': -1}
