#!/usr/bin/env python3
# 2020-05, Bruno Grossniklaus, https://github.com/it-gro
#
# https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
# https://docs.python.org/3/library/sys.html#sys.stdin
#
# ./_02_genexpr-01_MAE.py < sortme2.txt          # Linux: durch ausführbar gemacht (grün ;-)) + Shebang demo
# python.exe _02_genexpr-01_MAE.py < sortme2.txt
#
# ping -c 5  google.com | ./_02_genexpr-01_MAE.py     (da muss man ca. 5 Sek. warten bis alles herunter geladen ist!
# ping.exe   google.com | python.exe _02_genexpr-01_MAE.py

# mae:
# ping google.com | python _02_genexpr-01_MAE.py      (endlos Stream => example10 geht doch!!)

import sys



# ctrl + D zu unterbrechen der Eingaben
def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-)
    for line in sys.stdin:
        data = len(line)
        print(data)


def example02():              # Nachteil: lange warten bis ganzer Stream geladen
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-(
    lines = list(sys.stdin)
    print("lines: ", lines)
    data = list(map(lambda l: len(l), lines))
    print(data)


def example10():
    ex = "example10"
    print("\n", ex, "-" * len(ex), sep="\n")

    # # :-(
    # data = [
    #     len(line)
    #     for lines in sys.stdin
    #     for line in lines.splitlines(True)         # \n ist bewusst "behalten"
    # ]
    # print("data: ", data)
    # print("type(data): ", type(data))


# mae ERGÄNZUNG:
# folgende Eingabe wurde jeweils gemacht:

# Ein Versuch
#
# a
# bb
# ccc

    # for lines in sys.stdin:
    #    print(len(lines))
                                                    # Ein Versuch
                                                    # 13
                                                    #
                                                    # 1
                                                    # a
                                                    # 2
                                                    # bb
                                                    # 3
                                                    # ccc
                                                    # 4


    # myData = []
    # for lines in sys.stdin:
    #     myData.append(len(lines))
    # print("myData: ", myData)                       # myData:  [12, 1, 2, 3, 4]

    # myData = []
    # for lines in sys.stdin:
    #     print(lines.splitlines(True))
    # print("myData: ", myData)                     # => ['Ein Versuch\n']  and so on!

    # myData = []
    # for lines in sys.stdin:
    #     for line in lines.splitlines(True):
    #         myData.append(line)
    # print("myData: ", myData)                     # myData:  ['Ein Versuch \n', '\n', 'a\n', 'bb\n', 'ccc\n']

    # myData = []
    # for lines in sys.stdin:
    #     for line in lines.splitlines(True):
    #         myData.append(len(line))
    # print("myData: ", myData)                     # myData:  [12, 1, 2, 3, 4]


    myData3 = [len(lines) for lines in sys.stdin]   # mit windows-file ein Zeichen länger!!!
    print(myData3)                                  # [13, 1, 2, 3, 4]

# mae - end


def example11():
    ex = "example11"
    print("\n", ex, "-" * len(ex), sep="\n")

    # :-)

    # data = (
    #     len(line)
    #     for lines in sys.stdin
    #     for line in lines.splitlines(True)
    # )
    #
    # print("data: ", data)
    # for d in data:
    #     print(d)

# mae
    myData4= (len(lines) for lines in sys.stdin)              # mit windows-file ein Zeichen länger!!!
    print("myData4: ", myData4)
    print("type(myData4): ", type(myData4))
    for d in myData4:
         print("d: ", d)
# mae



if __name__ == "__main__":
    #example01()
    #example02()
    example10()
    #example11()
