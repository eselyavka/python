#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        mas = []
        def rec(root):
            if not root:
                return
            rec(root.left)
            mas.append(root.val)
            rec(root.right)

        rec(root)

        tree = TreeNode(mas.pop(0))
        buf = tree
        while mas:
            node = TreeNode(mas.pop(0))
            buf.right = node
            buf = node

        return tree

class TestSolution(unittest.TestCase):

    def test_increasingBST(self):
        solution = Solution()

        root = TreeNode(10)
        root.left = TreeNode(3)
        root.right = TreeNode(15)

        actual = solution.increasingBST(root)

        self.assertListEqual([actual.val, actual.right.val, actual.right.right.val], [3, 10, 15])

if __name__ == '__main__':
    unittest.main()
