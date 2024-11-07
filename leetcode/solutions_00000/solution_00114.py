#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        s, prev = [root], None
        while s:
            node = s.pop()
            if prev:
                prev.right = node
                prev.left = None

            if node.right:
                s.append(node.right)

            if node.left:
                s.append(node.left)

            prev = node


class TestSolution(unittest.TestCase):

    def test_flatten(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)

        solution.flatten(root)

        actual = []
        s = [root]
        while s:
            node = s.pop()
            actual.append(node.val)

            if node.left:
                s.append(node.left)

            if node.right:
                s.append(node.right)

        self.assertListEqual(actual, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
