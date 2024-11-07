#!/usr/bin/env python

import unittest
from collections import defaultdict

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        d = defaultdict(list)
        def rec(root, parent, level):
            if not root:
                return

            d[level].append(root)

            if root.left:
                root.left.parent = parent

            if root.right:
                root.right.parent = parent

            rec(root.left, root.left, level+1)
            rec(root.right, root.right, level+1)

        root.parent = None
        rec(root, root, 1)

        for levels in d:
            val_set = [n.val for n in d[levels]]
            if x in val_set and y in val_set:
                parents = set([n.parent.val for n in d[levels] if n.val == x or n.val == y])
                if len(parents) > 1:
                    return True

        return False

class TestSolution(unittest.TestCase):
    def test_isCousins(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)

        solution = Solution()
        self.assertFalse(solution.isCousins(root, 4, 3))

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(4)

        self.assertFalse(solution.isCousins(root, 2, 3))

        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.right = Node(4)
        root.right.right = Node(5)

        self.assertTrue(solution.isCousins(root, 5, 4))

if __name__ == '__main__':
    unittest.main()
