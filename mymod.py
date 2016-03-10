#!/usr/bin/env python
""" Module which emulate wc behavior """

import os

def count_lines(filename):
    """ count number of lines in file"""
    with(open(filename, 'r')) as fh:
        return len(fh.readlines())

def count_chars(filename):
    """ count number of chars in file """
    with(open(filename, 'r')) as fh:
        return len(fh.read())

def count_bytes(filename):
    """ count number of bytes in file """
    return os.stat(filename).st_size
