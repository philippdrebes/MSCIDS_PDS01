#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/csv.html
# https://docs.python.org/3/library/csv.html#csv.reader

# unzip shipwrecks.zip


import csv

FILENAME = "./shipwrecks/shipwrecks.csv"
LIMIT = 10

with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader, None)
    print(header)
    schema = dict(zip(header, range(len(header))))
    print(schema)
    cnt = 0
    for ship in csv_reader:
        print(ship[schema["chart"]],
              ship[schema["latdec"]],
              ship[schema["coordinates"]],
              sep=" / ")
        cnt += 1
        if cnt >= LIMIT:
            break


# ##################################################
# US,US,graph,Chart 11553 / 35.5390359 / [-76.6260807,35.5390359]
# US,US,graph,Chart 11552 / 35.015018 / [-76.690048,35.015018]
# US,US,graph,Chart 11554 / 35.544388 / [-77.06982,35.544388]
# ...
