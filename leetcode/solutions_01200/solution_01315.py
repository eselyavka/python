#!/usr/bin/env python

import unittest


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sum = 0

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(grandparent, parent, node):
            if not node:
                return

            if grandparent and grandparent.val % 2 == 0:
                self.sum += node.val

            traverse(parent, node, node.left)
            traverse(parent, node, node.right)

        traverse(None, None, root)

        return self.sum


class TestSolution(unittest.TestCase):
    def test_sumEvenGrandparent(self):
        root = Node(6)
        root.left = Node(7)
        root.right = Node(8)
        root.right.left = Node(1)
        root.right.right = Node(3)
        root.right.right.right = Node(5)
        root.left.left = Node(2)
        root.left.right = Node(7)
        root.left.left.right = Node(9)
        root.left.right.left = Node(1)
        root.left.right.right = Node(4)

        solution = Solution()
        self.assertEqual(solution.sumEvenGrandparent(root), 18)


if __name__ == '__main__':
    unittest.main()
