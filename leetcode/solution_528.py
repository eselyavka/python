#!/usr/bin/env python

import unittest
import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sum = []
        prefix_sum, i = 0, 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append((i, prefix_sum))
            i += 1

        self.total_sum = prefix_sum

    def pickIndex(self):
        """
        :rtype: int
        """
        target = self.total_sum * random.random()

        for i, prefix_sum in self.prefix_sum:
            if target < prefix_sum:
                return i

        return -1

class TestSolution(unittest.TestCase):
    def test_pickIndex(self):
        solution = Solution([1, 3])

        actual = []
        while sorted(actual, reverse=True) != [1, 1, 1, 1, 0]:
            actual = []
            for _ in range(5):
                actual.append(solution.pickIndex())

        self.assertListEqual(sorted(actual, reverse=True), [1, 1, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
