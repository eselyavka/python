#!/usr/bin/env python

import sys
from collections import defaultdict

def mapper():
    mapDict = defaultdict(list)
    duration = []
    for line in sys.stdin:
        data = line.strip().split('\t')
        for i in range(len(data)):
            if (i != (len(data) - 1)):
                ts = data[i].split(' ')
                for j in range(len(ts)):
                    if (j != (len(ts) - 1)):
                        dates = ts[j].split('-')
                        mapDict[dates[0]].append(data[i+1])
    for key in mapDict.keys():
        for duration in mapDict[key]:
            print "%s;%s" % (key, duration)

def main():
    mapper()

if __name__=='__main__':
    main()
