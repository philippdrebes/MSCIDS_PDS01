#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro
# 2021-10, Erwin Mathis

# robot_factory_id.py

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

    def __del__(self):
        print(self.name + " says bye-bye!")

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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ToDo
    def get_factory():
        return ""

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ToDo
    def factory_id(param):
        return ""


if __name__ == "__main__":
    print("Factory: " + Robot.get_factory())
    print("testing ...")
    r = Robot()
    print(r)
    print("producing ...")

    robots = []
    for i in range(10):
        r = Robot(f"Name {i}", 2020)
        print("%-30s | %s" % (r.factory_id(), r))
        robots.append(r)
    print(robots)      # only for development time!


###########################
# Goal is following output:
# Factory: ABB Robotics           (=> _factory)
# testing ...
# Name: , Build Year:
# producing ...
#  says bye-bye!
# ABB Robotics-2-2               | Name: Name 0, Build Year: 2020
# ABB Robotics-3-3               | Name: Name 1, Build Year: 2020
# ABB Robotics-4-2-2             | Name: Name 2, Build Year: 2020
# ABB Robotics-5-5               | Name: Name 3, Build Year: 2020
# ABB Robotics-6-2-3             | Name: Name 4, Build Year: 2020
# ABB Robotics-7-7               | Name: Name 5, Build Year: 2020
# ABB Robotics-8-2-2-2           | Name: Name 6, Build Year: 2020
# ABB Robotics-9-3-3             | Name: Name 7, Build Year: 2020
# ABB Robotics-10-2-5            | Name: Name 8, Build Year: 2020
# ABB Robotics-11-11             | Name: Name 9, Build Year: 2020
# Name 0 says bye-bye!
# Name 1 says bye-bye!
# Name 2 says bye-bye!
# Name 3 says bye-bye!
# Name 4 says bye-bye!
# Name 5 says bye-bye!
# Name 6 says bye-bye!
# Name 7 says bye-bye!
# Name 8 says bye-bye!
# Name 9 says bye-bye!
