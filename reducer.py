#!/usr/bin/env python

import sys

def reducer():
    (iterator, max_duration) = (None, -sys.maxint)
    for line in sys.stdin:
        (year, duration) = line.strip().split(';')
        if iterator and iterator != year:
            print "%s\t%s" % (iterator, max_duration)      
            (iterator, max_duration) = (year, int(duration))
        else:
           (iterator, max_duration) = (year, max(max_duration, int(duration)))
 
    if iterator:
        print "%s\t%s" % (iterator,max_duration)      

def main():
    reducer()

if __name__=='__main__':
    main()
