#!/usr/bin/env python3

"""Module for projects.reporter.status_reporter.rate."""

class SrvRate(object):
    def __init__(self, total, succ):
        self.total = total
        self.succ = succ

    def rate(self):
        if not self.total:
            return 0.0

        return float(self.succ) / float(self.total)

    def add_total(self, num):
        self.total += num

    def add_succ(self, num):
        self.succ += num
