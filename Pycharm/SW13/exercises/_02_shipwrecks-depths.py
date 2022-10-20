#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#

import json

FILENAME = "./shipwrecks/shipwrecks.json"
DISTINCT = ["feature_type", "quasou", "watlev"]


distinct = {}
for field in DISTINCT:
    distinct[field] = {}

with open(FILENAME) as json_file:
    for line in json_file:
        ship = json.loads(line)
        for field in DISTINCT:
            pass  # __**__

for field in DISTINCT:
    for data in distinct[field]:
        if distinct[field][data]["cnt_depth"] > 0:
            distinct[field][data]["avg_depth"] = (
                distinct[field][data]["sum_depth"] /
                distinct[field][data]["cnt_depth"])
        else:
            distinct[field][data]["avg_depth"] = 0

for field in DISTINCT:
    print("\n\n", field, "\n", "~" * len(field), sep="")
    for data in distinct[field]:
        pass  # __**__


# feature_type
# ~~~~~~~~~~~~
# Wrecks - Visible
#   cnt:       2585
#   cnt_depth: 8
#   avg_dept:  -0.90
#
# Wrecks - Submerged, dangerous
#   cnt:       6578
#   cnt_depth: 2039
#   avg_dept:  9.15
#
# distributed remains of wreck
#   cnt:       23
#   cnt_depth: 11
#   avg_dept:  8.37
#
# Wrecks - Submerged, nondangerous
#   cnt:       1845
#   cnt_depth: 454
#   avg_dept:  36.37
#
#
#
# quasou
# ~~~~~~
# depth unknown
#   cnt:       5573
#   cnt_depth: 0
#   avg_dept:  0.00
#
# value reported (not confirmed)
#   cnt:       253
#   cnt_depth: 253
#   avg_dept:  12.25
#
# least depth known
#   cnt:       2165
#   cnt_depth: 2165
#   avg_dept:  14.32
#
# depth known
#   cnt:       14
#   cnt_depth: 14
#   avg_dept:  8.41
#
# least depth unknown, safe clearance at value shown
#   cnt:       41
#   cnt_depth: 41
#   avg_dept:  10.03
#
# value reported (not surveyed)
#   cnt:       8
#   cnt_depth: 8
#   avg_dept:  1.99
#
#
#
# watlev
# ~~~~~~
# always dry
#   cnt:       2329
#   cnt_depth: 0
#   avg_dept:  0.00
#
# always under water/submerged
#   cnt:       8399
#   cnt_depth: 2566
#   avg_dept:  13.97
#
# covers and uncovers
#   cnt:       260
#   cnt_depth: 9
#   avg_dept:  -0.90
#
# partly submerged at high water
#   cnt:       89
#   cnt_depth: 0
#   avg_dept:  0.00
#
# awash
#   cnt:       15
#   cnt_depth: 0
#   avg_dept:  0.00
