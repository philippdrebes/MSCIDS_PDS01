#!/usr/bin/env python3
# Bruno Grossniklaus, Erwin Mathis
#
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/json.html#json.loads

import json

shipwreck = """
{
    "feature_type": "Wrecks - Submerged, dangerous",
    "chart": "US,US,graph,Chart 11554",
    "latdec": 35.316015,
    "londec": -76.789973,
    "quasou": "depth unknown",
    "watlev": "always under water/submerged",
    "coordinates": [
        -76.789973,
        35.316015
    ]
}
"""

data = json.loads(shipwreck)
print(type(data))
print(data["chart"], data["latdec"], data["coordinates"], sep=" / ")
