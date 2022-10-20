#!/usr/bin/env python3
# 2020-05, Bruno Grossniklaus, https://github.com/it-gro

import random as r
import time as t


def iot_sens_AX12():
    while True:
        yield (r.randrange(-40, -5), r.randrange(600, 900))


def iot_sens_YW42():
    while True:
        yield (r.randrange(10, 60), r.randrange(600, 900))


def watch(sensor):
    for s in sensor:
        print(s)
        t.sleep(0.1)


iot_sensor = iter(iot_sens_YW42())
# iot_sensor = iter(iot_sens_AX12())
watch(iot_sensor)
