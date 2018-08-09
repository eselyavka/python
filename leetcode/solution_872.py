#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        def _rec(root, arr):
            if not root:
                return

            if not root.left and not root.right:
                arr.append(root.val)

            _rec(root.left, arr)
            _rec(root.right, arr)

        _rec(root1, res1)
        _rec(root2, res2)

        return res1 == res2

class TestSolution(unittest.TestCase):

    def test_leafSimilar(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        root2 = TreeNode(5)
        root2.left = TreeNode(1)
        root2.right = TreeNode(4)
        root2.right.left = TreeNode(3)
        root2.right.right = TreeNode(6)

        solution = Solution()

        self.assertTrue(solution.leafSimilar(root, root2))

if __name__ == '__main__':
    unittest.main()
