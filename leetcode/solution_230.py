#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []

        def populateInorder(root):
            if root:
                populateInorder(root.left)
                res.append(root.val)
                populateInorder(root.right)

        populateInorder(root)

        return res[k-1]

class TestSolution(unittest.TestCase):

    def test_kthSmallest(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)

        root2 = TreeNode(5)
        root2.left = TreeNode(3)
        root2.right = TreeNode(6)
        root2.left.left = TreeNode(2)
        root2.left.right = TreeNode(4)
        root2.left.left.left = TreeNode(1)

        solution = Solution()

        self.assertEquals(solution.kthSmallest(root, 1), 1)
        self.assertEquals(solution.kthSmallest(root2, 3), 3)

if __name__ == '__main__':
    unittest.main()
