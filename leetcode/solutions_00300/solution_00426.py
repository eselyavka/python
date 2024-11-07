#!/usr/bin/env python

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        acc = []

        def rec(root):
            if not root:
                return

            rec(root.left)
            acc.append(root)
            rec(root.right)

        rec(root)
        n = len(acc)

        for i, val in enumerate(acc):
            if i == 0:
                val.left = acc[-1]
                val.right = val if n == 1 else acc[1]
            elif i == n - 1:
                val.left = acc[i-1]
                val.right = acc[0]
            else:
                val.left = acc[i-1]
                val.right = acc[i+1]

        return acc[0]

class TestSolution(unittest.TestCase):
    def test_verticalOrder(self):
        solution = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(5)

        res = solution.treeToDoublyList(root)
        head = None

        actual = []
        while res.val != head or head is None:
            if not head:
                head = res.val

            actual.append(res.val)
            res=res.right


        self.assertListEqual(actual, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
