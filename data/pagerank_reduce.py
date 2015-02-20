#!/usr/bin/env python
import sys
import re


ALPHA = 0.85


key = None
prev_key = None

# Key data is of form iteration, current PageRank, previous PageRank,
# neighbors.
key_data_default = ['-1', 1 - ALPHA, '-1', '']
key_data = key_data_default[:]

for line in sys.stdin:
    (key, value) = line.split('\t')

    if prev_key is None:
        prev_key = key

    # Found a new key, and since the input is sorted, flush the current key
    # data as the computation is over. "is not None" prevents an empty flush
    # at the beginning.
    if prev_key is not None and key != prev_key:
        key_data[1] = str(key_data[1])
        sys.stdout.write('%s\t%s\n' % (prev_key, ','.join(key_data)))
        key_data = key_data_default[:]
        prev_key = key

    # This tuple is part of PageRank summation.
    if value[0] is 'r':
        key_data[1] += ALPHA * float(value[1:])

    # This tuple contains the other i % ion for the node.
    else:
        value = re.match('v(\d+),(\d*.\d*),\d*.\d*,?(.*)', value).groups()
        # Increase iteration
        key_data[0] = str(int(value[0]) + 1)
        key_data[2] = value[1]
        key_data[3] = value[2]

key_data[1] = str(key_data[1])
sys.stdout.write('%s\t%s\n' % (prev_key, ','.join(key_data)))
