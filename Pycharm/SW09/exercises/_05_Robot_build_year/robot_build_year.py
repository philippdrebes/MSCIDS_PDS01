#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# robot_build_year.py

class Robot:
    def __init__(self, build_year=None):
        self.build_year = build_year

    @property
    def build_year(self):
        return self.__build_year

    @build_year.setter
    def build_year(self, build_year):
        if build_year:
            self.__build_year = build_year
            if self.__build_year < 1995:
                self.__build_year = 1995

def my_main():
    x = Robot(1950)
    print(x.build_year)

    # z = Robot("2015")
    # print(z.build_year)
    #
    # y = Robot()
    # print(y.build_year)

if __name__ == "__main__":
    my_main()

