#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/json.html#json.load

import json

FILENAME = "./shipwrecks/shipwrecks.array.json"
# FILENAME = "./shipwrecks/shipwrecks.array.pretty.json"
LIMIT = 10

with open(FILENAME) as json_file:
    data = json.load(json_file)
    print(type(data))
cnt = 0
for ship in data:
    print(ship["chart"], ship["latdec"], ship["coordinates"], sep=" / ")
    cnt += 1
    if cnt >= LIMIT:
        break
