#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/json.html#json.loads

import json

FILENAME = "./shipwrecks/shipwrecks.json"
# FILENAME = "./shipwrecks/shipwrecks.pretty.json"
LIMIT = 10

with open(FILENAME) as json_file:
    cnt = 0
    for line in json_file:
        ship = json.loads(line)
        print(ship["chart"], ship["latdec"], ship["coordinates"], sep=" / ")
        cnt += 1
        if cnt >= LIMIT:
            break
