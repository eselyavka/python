#!/usr/bin/env python

import unittest

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res, min_val, max_val = 0, arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, max(abs(arrays[i][0] - max_val), abs(arrays[i][-1] - min_val)))
            min_val, max_val = min(min_val, arrays[i][0]), max(max_val, arrays[i][-1])

        return res

class TestSolution(unittest.TestCase):

    def test_maxDistance(self):
        solution = Solution()

        self.assertEqual(solution.maxDistance([[1, 2, 3],
                                               [4, 5],
                                               [1, 2, 3]]), 4)
        self.assertEqual(solution.maxDistance([[1, 4], [0, 5]]), 4)
        self.assertEqual(solution.maxDistance([[1, 5], [3, 4]]), 3)
        self.assertEqual(solution.maxDistance([[-1, 5], [1, 4, 6], [4, 5, 6]]), 7)

if __name__ == '__main__':
    unittest.main()
