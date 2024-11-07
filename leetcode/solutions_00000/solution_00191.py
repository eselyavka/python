#!/usr/bin/env python

import unittest

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return n
        arr = []

        def to_dec(n):
            if n == 0:
                return
            arr.append(n % 2)
            to_dec(n >> 1)

        to_dec(n)

        return reduce(lambda x, y: x+y, arr)

class TestSolution(unittest.TestCase):

    def test_hammingWeight(self):
        solution = Solution()

        self.assertEqual(solution.hammingWeight(0), 0)
        self.assertEqual(solution.hammingWeight(1), 1)
        self.assertEqual(solution.hammingWeight(11), 3)
        self.assertEqual(solution.hammingWeight(128), 1)

if __name__ == '__main__':
    unittest.main()
