#!/usr/bin/env python

import unittest
from collections import defaultdict

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        def rec(node):
            if not node:
                return 0
            return node.val + rec(node.left) + rec(node.right)

        d = defaultdict(int)

        def dfs(root):
            if not root:
                return
            d[rec(root)] += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        _max = max(d.values())

        return [x[0] for x in d.items() if x[1] == _max]

class TestSolution(unittest.TestCase):

    def test_findFrequentTreeSum(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(-3)

        self.assertListEqual(Solution().findFrequentTreeSum(root), [2, 4, -3])

        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(-5)

        self.assertListEqual(Solution().findFrequentTreeSum(root), [2])
        self.assertListEqual(Solution().findFrequentTreeSum([]), [])

if __name__ == '__main__':
    unittest.main()
