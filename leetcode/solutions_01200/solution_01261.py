#!/usr/bin/env python

import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        root.val = 0
        self.elements = set()

        def rec(root, x):
            self.elements.add(x)
            if not root:
                return
            if root.left:
                root.left.val = 2 * x + 1
                rec(root.left, root.left.val)
            if root.right:
                root.right.val = 2 * x + 2
                rec(root.right, root.right.val)

        rec(root, root.val)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """

        return target in self.elements


class TestSolution(unittest.TestCase):
    def test_FindElements(self):
        root = Node(-1)
        root.left = Node(-1)
        root.left.left = Node(-1)
        root.left.right = Node(-1)
        root.right = Node(-1)

        solution = FindElements(root)
        self.assertTrue(solution.find(1))
        self.assertTrue(solution.find(3))
        self.assertFalse(solution.find(5))


if __name__ == '__main__':
    unittest.main()
