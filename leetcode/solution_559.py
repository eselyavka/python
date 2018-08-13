#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        def _rec(root, level):
            if not root:
                return level

            if not root.children:
                return level
            return max([_rec(x, level+1) for x in root.children])

        return _rec(root, 1)

class TestSolution(unittest.TestCase):

    def test_maxDepth(self):
        root = TreeNode(1)
        child = TreeNode(3)
        root.children = [child, TreeNode(2), TreeNode(4)]
        child.children = [TreeNode(5), TreeNode(6)]

        solution = Solution()

        self.assertEqual(solution.maxDepth(root), 3)
        self.assertEqual(solution.maxDepth(None), 0)

if __name__ == '__main__':
    unittest.main()
