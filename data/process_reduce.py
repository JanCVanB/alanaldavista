#!/usr/bin/env python

import sys

# TODO: HANDLE CASE WHERE DONE BEFORE 50th ITERATION


top_20 = {}

for line in sys.stdin:
    # Get iterations.
    if line[11] is ",":
        iteration = int(line[10])
    else:
        iteration = int(line[10:12])

    # End computation.
    if iteration == 50:
        pass

    else:
        sys.stdout.write("NodeId:%s,%d\t" % (line[:9], iteration))

        if iteration >= 10:
            rest_of_data = line[13:]
        else:
            rest_of_data = line[12:]

        # rest_of_data already has newline.
        sys.stdout.write("%s" % rest_of_data)
