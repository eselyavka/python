#!/usr/bin/env python

import unittest

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = [1]
        for i in range(rowIndex):
            arr.append(arr[i]*(rowIndex-i)/(i+1))
        return arr

class TestSolution(unittest.TestCase):
    def test_getRow(self):
        solution = Solution()
        self.assertEqual(solution.getRow(0), [1])
        self.assertEqual(solution.getRow(1), [1, 1])
        self.assertEqual(solution.getRow(2), [1, 2, 1])
        self.assertEqual(solution.getRow(3), [1, 3, 3, 1])

if __name__ == '__main__':
    unittest.main()
