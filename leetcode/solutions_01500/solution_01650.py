#!/usr/bin/env python

import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        ppath = []

        while p:
            ppath.append(p)
            p = p.parent

        while q:
            if q in ppath:
                return q

            q = q.parent


class TestSolution(unittest.TestCase):
    def test_lowestCommonAncestor(self):
        solution = Solution()
        root = Node(3)
        root.left = Node(5)
        root.left.parent = root
        root.left.left = Node(6)
        root.left.left.parent = root.left
        root.left.right = Node(2)
        root.left.right.parent = root.left
        root.left.right.left = Node(7)
        root.left.right.left.parent = root.left.right
        root.left.right.right = Node(4)
        root.left.right.right = root.left.right
        root.right = Node(1)
        root.right.parent = root
        root.right.left = Node(0)
        root.right.left.parent = root.right
        root.right.right = Node(8)
        root.right.right = root.right

        p = root.left
        q = root.left.right.right

        self.assertEqual(solution.lowestCommonAncestor(p, q), root.left)


if __name__ == '__main__':
    unittest.main()
