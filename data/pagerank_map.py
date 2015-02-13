#!/usr/bin/env python
import sys
import re


get_data_regex = re.compile('NodeId:(\d*),?(\d*)\t(\d*.\d*),(\d*.\d*),?(.*)')


def line_parse(s):
    """line_parse takes a "NodeID..." string and returns a tuple of its
    identifier, current PageRank, previous PageRank, the nodes its node links
    to, and if this isn't the first iteration, the iteration number."""
    # Data is of form (index, [iteration,] current PageRank, previous PageRank,
    # list_of_neighbors)
    data = get_data_regex.match(s).groups()
    # If there is no iteration AKA first iteration
    if not data[1]:
        data = (data[0], '0', data[2], data[3], data[4].split(","))
    else:
        data = (data[0], data[1], data[2], data[3], data[4].split(","))
    return data


def run(inputs):
    for line in inputs:
        if not line:
            continue
        data = line_parse(line)
        # output is either iNUM\trNUM which is part of PageRank of i
        # or iNUM\tvSTRINGofNUMS which is the way we're saving the data.
        if data[4][0] == "":
            yield '%s\tr%s\n' % (data[0], float(data[2]))
        else:
            for friend in data[4]:
                yield '%s\tr%s\n' % (friend, float(data[2]) / float(len(data[4])))
        list_of_friends = data[4]
        if data[4][0] == '':
            list_of_friends = ''
        else:
            list_of_friends = ',' + ','.join(data[4])
        yield '%s\tv%s\n' % (data[0], data[1] + ',' + data[2] + ',' + data[3] + list_of_friends)


if __name__ == '__main__':
    for output_string in run(sys.stdin):
        sys.stdout.write(output_string)
