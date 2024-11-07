#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        mem = set()
        s = [root]

        while s:
            node = s.pop()
            if k - node.val in mem:
                return True
            mem.add(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)

        return False


class TestSolution(unittest.TestCase):

    def test_findTarget(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.left = None
        root.right.right = TreeNode(7)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)

        root3 = TreeNode(2)
        root3.left = TreeNode(0)
        root3.right = TreeNode(3)
        root3.left.left = TreeNode(-4)
        root3.left.right = TreeNode(1)

        solution = Solution()
        self.assertTrue(solution.findTarget(root, 9))
        self.assertTrue(solution.findTarget(root, 6))
        self.assertTrue(solution.findTarget(root2, 3))
        self.assertTrue(solution.findTarget(root3, -1))
        self.assertFalse(solution.findTarget(root, 28))


if __name__ == '__main__':
    unittest.main()
