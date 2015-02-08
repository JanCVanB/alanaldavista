#!/usr/bin/env python

import sys
import re


alpha = 0.85


key = None
prev_key = None

# key data is of form index, iteration, current PageRank, previous PageRank,
# neighbors
key_data_default = ["-1", -1, 1 - alpha, "-1", []]
key_data = key_data_default


for line in sys.stdin:
    (key, value) = line.split("\t")
    key = key[1:]

    # Found a new key, and since the input is sorted, flush the current key
    # data as the computation is over. "is not None" prevents an empty flush
    # at the beginning.
    if prev_key is not None and key != prev_key:
        key_data[2] = str(key_data)
        sys.stdout.write(key_data)
        key_data = key_data_default
        prev_key = key
        key_data[0] = key

    # if value[0] is "r":
    #     key_data[]
    #
    # else:


    sys.stdout.write(line)

