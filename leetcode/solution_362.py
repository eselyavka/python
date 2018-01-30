#!/usr/bin/env python

import unittest

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.win_len = 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.arr.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        if timestamp > self.win_len:
            first = timestamp - self.win_len
            self.arr = [x for x in self.arr if x > first]
            return len(self.arr)
        return len(self.arr)

class TestHitCounter(unittest.TestCase):

    def test_HitCounter(self):
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(4), 3)
        counter.hit(300)
        self.assertEqual(counter.getHits(300), 4)
        self.assertEqual(counter.getHits(301), 3)
        counter.hit(400)
        self.assertEqual(counter.getHits(600), 1)
        counter.hit(730)
        self.assertEqual(counter.getHits(1024), 1)

if __name__ == '__main__':
    unittest.main()
