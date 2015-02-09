#!/usr/bin/env python

import sys
import re
import operator

# TODO: HANDLE CASE WHERE DONE BEFORE 50th ITERATION


get_score_string = "\d{9}\t\d{1,2},(\d*.\d*)"
get_score_regex = re.compile(get_score_string)

min_node = "-1"
top_20 = {}


def compute_min():
    global min_node
    min_pagerank = None
    for node, pagerank in top_20.iteritems():
        if min_pagerank is None:
            min_node = node
            min_pagerank = pagerank
        elif pagerank < min_pagerank:
            min_node = node
            min_pagerank = pagerank


def unpad_zeroes(s):
    n = 0
    while s[n] == "0":
        n += 1
    return s[n:]


for line in sys.stdin:
    # Get iterations.
    if line[11] is ",":
        iteration = int(line[10])
    else:
        iteration = int(line[10:12])

    # End computation.
    if iteration == 50:
        node = line[:9]
        score = float(get_score_regex.match(line).group(1))

        if len(top_20) < 20:
            top_20[node] = score

        else:
            compute_min()
            if top_20[min_node] < score:
                del top_20[min_node]
                top_20[node] = score

    # Keep iterating.
    else:
        sys.stdout.write("NodeId:%s,%d\t" % (line[:9], iteration))

        if iteration >= 10:
            rest_of_data = line[13:]
        else:
            rest_of_data = line[12:]

        # rest_of_data already has newline.
        sys.stdout.write("%s" % rest_of_data)

# If we're done.
if top_20:
    top_20_sorted = sorted(top_20.items(), key=operator.itemgetter(1))
    top_20_sorted.reverse()
    for node, pagerank in top_20_sorted:
        sys.stdout.write("FinalRank:%f\t%s\n" % (pagerank, unpad_zeroes(node)))