#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#

# mkdir data
# cd data
# curl -LO http://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip
# unzip bank.zip

# "age";"job";"marital";"education";"default";"balance";"housing";"loan";"contact";
#   "day";"month";"duration";"campaign";"pdays";"previous";"poutcome";"y"

FILE_NAME = "./data/bank.csv"
SEP = ";"
HEADER = ["age", "job", "marital", "education", "default", "balance",
          "housing", "loan", "contact", "day", "month", "duration",
          "campaign", "pdays", "previous", "poutcome", "y"]

COLS = dict(zip(HEADER, range(len(HEADER))))
WIDTH = -12


def example01():
    ex = "example01"
    print("\n", ex, "-" * len(ex), sep="\n")

    with open(FILE_NAME) as file:

        header = file.readline()
        print(header)
        print("~" * 20)

        line = file.readline()
        print(line)
        print("~" * 20)

        data = line.split(sep=SEP)
        print(*data, "end")
        print("~" * 20)

        print(data[0], type(data[0]))
        print(data[-1], type(data[-1]))
        print("~" * 20)

        line = file.readline()
        data = line.strip().split(sep=SEP)
        print(data[0], type(data[0]))
        print(data[-1], type(data[-1]))


def example02():
    ex = "example02"
    print("\n", ex, "-" * len(ex), sep="\n")

    b, d = 0, 0
    with open(FILE_NAME) as file:
        file.readline()
        for line in file:
            data = line.strip().split(sep=SEP)
            b += int(data[5])
            d += int(data[11])

        print("sums:\n%10s: %d\n%10s: %d" % ("balance", b, "duration", d))


def example03():
    ex = "example03"
    print("\n", ex, "-" * len(ex), sep="\n")

    b, d = 0, 0
    with open(FILE_NAME) as file:
        file.readline()
        for line in file:
            data = line.strip().split(sep=SEP)
            b += int(data[COLS["balance"]])
            d += int(data[COLS["duration"]])
        print("sums:\n%-10s: %d\n%-10s: %d" % ("balance", b, "duration", d))


def example04():
    ex = "example04"
    print("\n", ex, "-" * len(ex), sep="\n")

    cols = ["balance", "duration"]
    results = {}
    for c in cols:
        results[c] = 0

    with open(FILE_NAME) as file:
        file.readline()
        for line in file:
            data = line.strip().split(sep=SEP)
            for c in cols:
                results[c] += int(data[COLS[c]])

        print("sums:")
        for c in cols:
            print(f"%{WIDTH}s: %d" % (c, results[c]))


def example05():
    ex = "example05"
    print("\n", ex, "-" * len(ex), sep="\n")

    cols = ["marital", "education"]
    results = {}
    for c in cols:
        results[c] = []

    with open(FILE_NAME) as file:
        file.readline()
        for line in file:
            data = line.strip().split(sep=SEP)
            # data = line.strip().replace('"', "").split(sep=SEP)
            for c in cols:
                if not data[COLS[c]] in results[c]:
                    results[c].append(data[COLS[c]])

        print("distinct:")
        for c in cols:
            print(f"%{WIDTH}s: %s" % (c, results[c]))


if __name__ == "__main__":
    example01()
    example02()
    example03()
    example04()
    example05()

# 24;"foo ; bar";42 => https://docs.python.org/3/library/csv.html


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# example01
# ---------
# "age";"job";"marital";"education";"default";"balance";"housing";"loan";
# "contact";"day";"month";"duration";"campaign";"pdays";"previous";"poutcome";"y"
#
# ~~~~~~~~~~~~~~~~~~~~
# 30;"unemployed";"married";"primary";"no";1787;"no";"no";
# "cellular";19;"oct";79;1;-1;0;"unknown";"no"
#
# ~~~~~~~~~~~~~~~~~~~~
# 30 "unemployed" "married" "primary" "no" 1787 "no" "no"
# "cellular" 19 "oct" 79 1 -1 0 "unknown" "no"
#  end
# ~~~~~~~~~~~~~~~~~~~~
# 30 <class 'str'>
# "no"
#  <class 'str'>
# ~~~~~~~~~~~~~~~~~~~~
# 33 <class 'str'>
# "no" <class 'str'>
#
#
# example02
# ---------
# sums:
#    balance: 6431836
#   duration: 1193369
#
#
# example03
# ---------
# sums:
# balance   : 6431836
# duration  : 1193369
#
#
# example04
# ---------
# sums:
# balance     : 6431836
# duration    : 1193369
#
#
# example05
# ---------
# distinct:
# marital     : ['"married"', '"single"', '"divorced"']
# education   : ['"primary"', '"secondary"', '"tertiary"', '"unknown"']
