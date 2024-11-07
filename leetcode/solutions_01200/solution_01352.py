#!/usr/bin/env python

import unittest


class ProductOfNumbers(object):

    def __init__(self):
        self.nums = list()
        self.total = 1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.nums = list()
            self.total = 1
        else:
            self.total *= num
            self.nums.append(self.total)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.nums):
            return 0
        elif k == len(self.nums):
            return self.total

        return self.total / self.nums[-k - 1]


class TestSolution(unittest.TestCase):

    def test_ProductOfNumbers(self):
        solution = ProductOfNumbers()
        _ = [solution.add(x) for x in [3, 0, 2, 5, 4]]
        self.assertEqual(solution.getProduct(2), 20)
        self.assertEqual(solution.getProduct(3), 40)
        self.assertEqual(solution.getProduct(4), 0)
        solution.add(8)
        self.assertEqual(solution.getProduct(2), 32)


if __name__ == '__main__':
    unittest.main()
