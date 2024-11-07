#!/usr/bin/env python

import unittest

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.payload = list()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        self.payload.append(val)

        if len(self.payload) <= self.size:
            return sum(self.payload) / float(len(self.payload))

        return sum(self.payload[:self.size/-1 - 1:-1]) / float(self.size)

class TestSolution(unittest.TestCase):

    def test_MovingAverage(self):
        solution = MovingAverage(3)
        self.assertEqual(solution.next(1), 1/1)
        self.assertEqual(solution.next(10), (1+10)/2.0)
        self.assertEqual(solution.next(3), (1 + 10 + 3)/3.0)
        self.assertEqual(solution.next(5), (10 + 3 + 5)/3.0)

if __name__ == '__main__':
    unittest.main()
