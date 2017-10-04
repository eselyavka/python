#!/usr/bin/env python

import unittest

class Solution(object):

    @staticmethod
    def _rec(element, depth=1):
        res = 0
        for e in element:
            if isinstance(e, list):
                res = res + Solution._rec(e, depth=depth+1)
            else:
                res += depth * e
        return res

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return Solution._rec(nestedList)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.arr1 = [[1, 1], 2, [1, 1]]
        self.arr2 = [1, [4, [6]]]

    def test_depthSum(self):
        solution = Solution()
        self.assertEqual(solution.depthSum(self.arr1), 10)
        self.assertEqual(solution.depthSum(self.arr2), 27)

if __name__ == '__main__':
    unittest.main()
