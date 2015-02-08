#!/usr/bin/env python

import sys
import re


alpha = 0.85


def pad_zeroes(x):
    """pad_zeroes takes a string representation of an integer and returns
    a length of 9 representation of it. For sorting purposes."""
    if len(x) > 9:
        raise ValueError("Cannot handle indices greater than 999,999,999.")
    return (9 - len(x)) * "0" + x


def line_parse(s):
    """line_parse takes a "NodeID..." string and returns a tuple of its
    identifier, current PageRank, previous PageRank, the nodes its node links
    to, and if this isn't the first iteration, the iteration number."""

    get_data_string = "NodeId:(\d*)(,\d*)?\t(\d*.\d*),(\d*.\d*)\,?(.*)?"
    get_data_regex = re.compile(get_data_string)

    # Data is of form (index, [iteration,] current PageRank, previous PageRank,
    # list_of_neighbors)
    data = get_data_regex.match(s).groups()

    # If there is no iteration AKA first iteration
    if data[1] is None:
        data = (data[0], "1", data[2], data[3], data[4].split(","))
    else:
        data = (data[0], data[1][1:], data[2], data[3], data[4].split(","))

    return data


for line in sys.stdin:
    data = line_parse(line)
    # output is either iNUM\trNUM which is part of PageRank of i
    # or iNUM\tvSTRINGofNUMS which is the way we're saving the data.
    for friend in data[4]:
        sys.stdout.write("i%s\tr%s\n" % (pad_zeroes(friend),
                                         alpha * float(data[2])
                                         / float(len(data[4]))))

    sys.stdout.write("i%s\tv%s\n" % (pad_zeroes(data[0]),
                     data[1] + "," + data[2] + "," + data[3]
                     + "," + ",".join(data[4])))
