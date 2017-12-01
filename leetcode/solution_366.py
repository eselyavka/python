#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def removeLeaves(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            del root
            return

        root.left = self.removeLeaves(root.left if root.left else None)
        root.right = self.removeLeaves(root.right if root.right else None)

        return root

    def extractLeaves(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        return (self.extractLeaves(root.left if root.left else None) +
                self.extractLeaves(root.right if root.right else None))

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = list()

        while root:
            res.append(self.extractLeaves(root))
            root = self.removeLeaves(root)
        return res

class TestSolution(unittest.TestCase):

    def test_findLeaves(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()

        self.assertListEqual(solution.findLeaves(root), [[4, 5, 3], [2], [1]])

if __name__ == '__main__':
    unittest.main()
