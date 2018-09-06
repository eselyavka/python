#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def rec(root):
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            res.append(abs(left-right))
            return left + right + root.val

        rec(root)

        return sum(res)

class TestSolution(unittest.TestCase):

    def test_findTilt(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        solution = Solution()

        self.assertEqual(solution.findTilt(root), 1)

if __name__ == '__main__':
    unittest.main()
