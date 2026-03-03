#!/usr/bin/env python3

"""Module for archive.legacy_ops.hadoop.reducer."""

import sys

def reducer():
    iterator, max_duration = None, -sys.maxsize
    for line in sys.stdin:
        year, duration = line.strip().split(';')
        if iterator and iterator != year:
            print(f"{iterator}\t{max_duration}")
            iterator, max_duration = year, int(duration)
        else:
            iterator, max_duration = year, max(max_duration, int(duration))

    if iterator:
        print(f"{iterator}\t{max_duration}")

def main():
    reducer()

if __name__ == '__main__':
    main()
