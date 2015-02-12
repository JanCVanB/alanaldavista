#!/usr/bin/env python
import sys
# TODO: FIGURE OUT WHAT THIS IS FOR


def run(inputs):
    for line in inputs:
        yield line


if __name__ == '__main__':
    for output_string in run(sys.stdin):
        sys.stdout.write(output_string)
