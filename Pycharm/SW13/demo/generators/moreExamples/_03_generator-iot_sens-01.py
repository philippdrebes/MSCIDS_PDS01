#!/usr/bin/env python3
# 2020-05, Bruno Grossniklaus, https://github.com/it-gro

import random as r
import time as t


def iot_sens():
    while True:
        yield (r.randrange(-20, 50), r.randrange(600, 900))


for s in iot_sens():
    print(s)
    t.sleep(1)
