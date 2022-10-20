#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#


# ok ... a tough nut to crack ...


import json

FILENAME = "./shipwrecks/shipwrecks.json"
DISTINCT = ["feature_type", "quasou", "watlev"]

distinct = {}
for field in DISTINCT:
    distinct[field] = []

with open(FILENAME) as json_file:
    for line in json_file:
        ship = json.loads(line)
        for field in DISTINCT:
            pass  # __**__

for field in DISTINCT:
    print("\n\n", field, "\n", "~" * len(field), sep="")
    for data in distinct[field]:
        print(data)

# feature_type
# ~~~~~~~~~~~~
# Wrecks - Visible
# Wrecks - Submerged, dangerous
# distributed remains of wreck
# Wrecks - Submerged, nondangerous
#
#
# quasou
# ~~~~~~
# depth unknown
# value reported (not confirmed)
# least depth known
# depth known
# least depth unknown, safe clearance at value shown
# value reported (not surveyed)
#
#
# watlev
# ~~~~~~
# always dry
# always under water/submerged
# covers and uncovers
# partly submerged at high water
# awash
