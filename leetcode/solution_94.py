#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        stack = []
        curr = root

        while True:
            if not curr and stack:
                node=stack.pop()
                res.append(node.val)
                curr = node.right
            else:
                stack.append(curr)
                curr = curr.left

            if not curr and not stack:
                break

        return res

class TestSolution(unittest.TestCase):

    def test_inorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        solution = Solution()

        self.assertListEqual(solution.inorderTraversal(root), [1, 3, 2])

if __name__ == '__main__':
    unittest.main()
