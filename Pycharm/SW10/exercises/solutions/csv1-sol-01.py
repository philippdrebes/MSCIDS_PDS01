#!/usr/bin/env python3
# 2020-04, Bruno Grossniklaus, https://github.com/it-gro

# http://archive.ics.uci.edu/ml/datasets/bank+marketing
# mkdir data; cd data
# curl -LO http://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip
# unzip bank.zip


class Csv1():
    _MAX_COLUMNS = 1000

    def __init__(self, file=None, header=False, sep=",", quoted=True):
        self._file = file
        self._header = header
        self._sep = sep
        self._quoted = quoted

    def __str__(self):
        r = f"file: '{self._file}'"
        r += ", " + f"header: '{self._header}'"
        r += ", " + f"sep: '{self._sep}'"
        return r

    @property
    def header(self):
        h = ""
        if self._header:
            with open(self._file) as file:
                line = file.readline()
                h = line.strip().split(self._sep)
                if self._quoted:
                    for i in range(len(h)):
                        h[i] = h[i].strip('"')

        return h

    def head(self, number_of_records):
        rn = 0

        with open(self._file) as file:
            if self._header:
                line = file.readline()

            for line in file:
                rn += 1

                if rn == number_of_records + 1:
                    break

                r = line.strip().split(self._sep)
                if self._quoted:
                    for i in range(len(r)):
                        r[i] = r[i].strip('"')

                for i in range(len(r)):
                    print(r[i], end=",")
                print()

    def stats(self, *columns):
        if self._header:
            h = self.header
        else:
            h = range(Csv1._MAX_COLUMNS)

        schema = dict(zip(h, range(Csv1._MAX_COLUMNS)))
        r_min = dict(zip(columns, [0] * len(columns)))
        r_max = dict(zip(columns, [0] * len(columns)))
        r_sum = dict(zip(columns, [0] * len(columns)))
        r_cnt = dict(zip(columns, [0] * len(columns)))
        r_avg = dict(zip(columns, [0] * len(columns)))

        with open(self._file) as file:
            if self._header:
                file.readline()

            for line in file:
                r = line.strip().split(self._sep)
                for col in columns:
                    value = r[schema[col]]
                    if value:
                        r_min[col] = min(r_min[col], float(value))
                        r_max[col] = max(r_max[col], float(value))
                        r_sum[col] += float(value)
                        r_cnt[col] += 1

        for col in columns:
            r_avg[col] = r_sum[col] / r_cnt[col]

        return {"min": r_min,
                "max": r_max,
                "sum": r_sum,
                "cnt": r_cnt,
                "avg": r_avg}


if __name__ == "__main__":
    bank_csv = Csv1(file="./data/bank.csv", header=True, sep=";")

    print(bank_csv)
    print(bank_csv.header)

    print("~" * 50)
    bank_csv.head(3)

    print("~" * 50)
    stats = bank_csv.stats("age", "balance")
    for stat in stats:
        print(stat, stats[stat])
