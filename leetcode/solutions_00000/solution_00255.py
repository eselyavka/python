#!/usr/bin/env python

import unittest

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        s = []
        root = float('-inf')

        for val in preorder:
            if val < root:
                return False

            while s and s[-1] < val:
                root = s.pop()

            s.append(val)

        return True

class TestSolution(unittest.TestCase):

    def test_verifyPreorder(self):
        solution = Solution()

        self.assertFalse(solution.verifyPreorder([5, 2, 6, 1, 3]))
        self.assertTrue(solution.verifyPreorder([5, 2, 1, 3, 6]))

if __name__ == '__main__':
    unittest.main()
