#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# robot_factory_id_sol.py

class Robot():
    __counter = 0
    _factory = "ABB Robotics"

    def __init__(self,
                 name=None,
                 build_year=None):
        self.name = ""
        if name:
            self.name = str(name)
        self.build_year = build_year
        type(self).__counter += 1

    def __repr__(self):
        return("Robot(\"" + self.name +
               "\"," + self.xstr(self.build_year) + ")")

    def __str__(self):
        return("Name: " + self.name +
               ", Build Year: " + self.xstr(self.build_year))

    # def __del__(self):
    #     print(self.name + " says bye-bye!")

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    @staticmethod
    def xstr(s):
        return '' if not s else str(s)

    @staticmethod
    def prime_factors(n):
        d = 2
        factors = []
        while n >= d*d:
            if n % d == 0:
                n //= d
                factors.append(d)
            else:
                d = d+1
        if n > 1:
            factors.append(n)
        return factors

    @classmethod
    def count_robot_instances(cls):
        return cls.__counter

    @classmethod
    def get_factory(cls):
        return cls._factory

    @classmethod
    def factory_id(cls):
        id = cls._factory
        id += "-" + str(cls.__counter)
        primes = cls.prime_factors(cls.__counter)
        for p in primes:
            id += "-" + str(p)
        return id


if __name__ == "__main__":
    print("Factory: " + Robot.get_factory())
    print("testing ...")
    r = Robot()
    print(r)
    print("producing ...")

    robots = []
    for i in range(10):
        r = Robot(f"Name {i}", 2022)
        print("%-30s | %s" % (r.factory_id(), r))
        robots.append(r)
    print(robots)
