#!/usr/bin/env python3

# robot_del.py

class Robot():

    def __init__(self, name):
        self.name = name
        print(name + " has been created!")

    def __del__(self):
        print(self.name + " says bye-bye!")


if __name__ == "__main__":
    x = Robot("Tik-Tok")
    print("Deleting x")
    del x
