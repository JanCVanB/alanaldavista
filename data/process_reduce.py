#!/usr/bin/env python
import sys
import re
import operator


MAX_ITERATIONS = 15


def compute_min(min_node, top_20):
    min_pagerank = None
    for node, pagerank in top_20.iteritems():
        if min_pagerank is None:
            min_node = node
            min_pagerank = pagerank
        elif pagerank < min_pagerank:
            min_node = node
            min_pagerank = pagerank
    return min_node, min_pagerank


def unpad_zeroes(s):
    n = 0
    while s[n] == "0" and n != 8:
        n += 1
    return s[n:]


def run(input_strings):
    min_node = '-1'
    top_20 = {}
    for line in input_strings:
        # Get iterations.
        if line[11] is ',':
            iteration = int(line[10])
        else:
            iteration = int(line[10:12])

        # End computation.
        if iteration == 15:
            node = line[:9]
            score = float(re.match('\d{9}\t\d{1,2},(\d*.\d*)', line).group(1))
            if len(top_20) < 20:
                top_20[node] = score
            else:
                min_node, min_pagerank = compute_min(min_node, top_20)
                if top_20[min_node] < score:
                    del top_20[min_node]
                    top_20[node] = score
        # Keep iterating.
        else:
            if iteration >= 10:
                rest_of_data = line[13:]
            else:
                rest_of_data = line[12:]
            # rest_of_data already has newline.
            yield 'NodeId:%s,%d\t%s' % (line[:9], iteration, rest_of_data)

    # If we're done.
    if top_20:
        top_20_sorted = sorted(top_20.items(), key=operator.itemgetter(1), reverse=True)
        for node, pagerank in top_20_sorted:
            yield 'FinalRank:%f\t%s\n' % (pagerank, unpad_zeroes(node))


if __name__ == '__main__':
    for output_string in run(sys.stdin):
        sys.stdout.write(output_string)
