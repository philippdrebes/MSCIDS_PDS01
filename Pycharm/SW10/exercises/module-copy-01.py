#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

# https://docs.python.org/3/library
# https://docs.python.org/3/library/copy.html
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# https://www.python.org/dev/peps/pep-0498/

import copy as C


class Robot():
    FO_LEN_NAME = 8

    def __init__(self, name="", build_year=0):
        self.name = name
        self.build_year = build_year

    def __str__(self):
        sf = f"Name: %-{self.FO_LEN_NAME}s, Build Year: %04d"
        sr = sf % (self.name, self.build_year)
        return sr

    def say_hi(self):
        print("Hi, I am " + self.name)


if __name__ == "__main__":
    r1 = Robot("Robi_1")
    r2 = Robot("Robi_2", 2019)
    r3 = Robot("Robi_3", 2020)

    robots = [r1, r2, r3]
    my_copy_1 = robots
    my_copy_2 = C.copy(robots)
    my_copy_3 = C.deepcopy(robots)

    print("1)", "~" * 30)
    print(*robots, sep="\n", end="\n\n")
    print(*my_copy_1, sep="\n", end="\n\n")
    print(*my_copy_2, sep="\n", end="\n\n")
    print(*my_copy_3, sep="\n", end="\n\n")

    print("2)", "~" * 30)
    r2.name = "Marvin"
    robots.append(Robot("HAL", 2050))
    print(*robots, sep="\n", end="\n\n")
    print(*my_copy_1, sep="\n", end="\n\n")
    print(*my_copy_2, sep="\n", end="\n\n")
    print(*my_copy_3, sep="\n", end="\n\n")


#
# 1) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name: Robi_1  , Build Year: 0000
# Name: Robi_2  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
#
# Name: Robi_1  , Build Year: 0000
# Name: Robi_2  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
#
# Name: Robi_1  , Build Year: 0000
# Name: Robi_2  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
#
# Name: Robi_1  , Build Year: 0000
# Name: Robi_2  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
#
# 2) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name: Robi_1  , Build Year: 0000
# Name: Marvin  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
# Name: HAL     , Build Year: 2050
#
# Name: Robi_1  , Build Year: 0000
# Name: Marvin  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
# Name: HAL     , Build Year: 2050
#
# Name: Robi_1  , Build Year: 0000
# Name: Marvin  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
#
# Name: Robi_1  , Build Year: 0000
# Name: Robi_2  , Build Year: 2019
# Name: Robi_3  , Build Year: 2020
