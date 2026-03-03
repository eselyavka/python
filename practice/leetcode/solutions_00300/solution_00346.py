#!/usr/bin/env python3

"""LeetCode solution 00346."""

import unittest
from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.payload = deque()
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.payload.append(val)
        self.total += val

        if len(self.payload) > self.size:
            self.total -= self.payload.popleft()

        return self.total / float(len(self.payload))

class TestSolution(unittest.TestCase):

    def test_MovingAverage(self):
        solution = MovingAverage(3)
        self.assertEqual(solution.next(1), 1/1)
        self.assertEqual(solution.next(10), (1+10)/2.0)
        self.assertEqual(solution.next(3), (1 + 10 + 3)/3.0)
        self.assertEqual(solution.next(5), (10 + 3 + 5)/3.0)

if __name__ == '__main__':
    unittest.main()
