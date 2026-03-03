#!/usr/bin/env python3

"""Module for archive.legacy_ops.hadoop.mapper."""

import sys
from collections import defaultdict

def mapper():
    mapDict = defaultdict(list)
    for line in sys.stdin:
        data = line.strip().split('\t')
        for i, item in enumerate(data[:-1]):
            ts = item.split(' ')
            for timestamp in ts[:-1]:
                dates = timestamp.split('-')
                mapDict[dates[0]].append(data[i + 1])
    for key in list(mapDict.keys()):
        for duration in mapDict[key]:
            print(f"{key};{duration}")

def main():
    mapper()

if __name__ == '__main__':
    main()
