#!/usr/bin/env python

import unittest
from collections import defaultdict

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None
    def __repr__(self):
        return str(self.val)


def rec(root, d, level=0):
    """
    O(n) memory
    """
    if not root:
        return
    d[level].append(root)
    rec(root.left, d, level+1)
    rec(root.right, d, level+1)


def rec_(root, right_root):
    """
    O(1) memory
    """
    if not (root and root.left):
        return

    root.left.next = root.right

    if right_root:
        root.right.next = right_root.left
        rec_(root.right, right_root.left)
    else:
        rec_(root.right, None)
    rec_(root.left, root.right)


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        rec_(root, None)

        # d = defaultdict(list)
        # rec(root, d)
        # for level in d:
        #     for i in range(1, len(d[level])):
        #         d[level][i-1].next = d[level][i]

        return root


def inOrderTraversals(root):
    if root:
        inOrderTraversals(root.left)
        print root.val, ' -> ', root.next
        inOrderTraversals(root.right)


class TestSolution(unittest.TestCase):
    def test_connect(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        solution = Solution()
        solution.connect(root)
        inOrderTraversals(root)


if __name__ == '__main__':
    unittest.main()
