#!/usr/bin/env python

import unittest

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        size = len(temperatures)

        s = []
        res = [0] * size
        i = size - 1

        while i >= 0:
            while s and temperatures[i] >= temperatures[s[-1]]:
                s.pop()
            if s:
                res[i] = s[-1] - i
            s.append(i)
            i -= 1

        return res

class TestSolution(unittest.TestCase):
    def test_dailyTemperatures(self):
        solution = Solution()
        self.assertEqual(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
                         [1, 1, 4, 2, 1, 1, 0, 0])

if __name__ == '__main__':
    unittest.main()
