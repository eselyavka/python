#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def populateArray(self, root, arr):
        if root:
            self.populateArray(root.left, arr)
            arr.append(root.val)
            self.populateArray(root.right, arr)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        arr = list()
        self.populateArray(root, arr)

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] + arr[right] == k:
                return True
            elif arr[left] + arr[right] > k:
                right -= 1
            else:
                left += 1

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
