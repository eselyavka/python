#!/usr/bin/env python

import unittest


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []

        for i in range(1, 9):
            num = i
            if num >= low and num <= high:
                res.append(num)
            for j in range(i+1, 10):
                num = num * 10 + j
                if num >= low and num <= high:
                    res.append(num)

        return sorted(res)


class TestSolution(unittest.TestCase):

    def test_sequentialDigits(self):
        solution = Solution()
        self.assertListEqual(solution.sequentialDigits(100, 300), [123, 234])


if __name__ == '__main__':
    unittest.main()
