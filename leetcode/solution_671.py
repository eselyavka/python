#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _set = set()

        def rec(root):
            if root:
                _set.add(root.val)
                rec(root.left)
                rec(root.right)

        rec(root)
        return sorted(_set)[1] if len(_set) >= 2 else -1

class TestSolution(unittest.TestCase):

    def test_findSecondMinimumValue(self):
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)

        root2 = TreeNode(2)
        root2.left = TreeNode(2)
        root2.right = TreeNode(2)

        # 2,2,5,null,null,5,5
        root3 = TreeNode(2)
        root3.left = TreeNode(2)
        root3.right = TreeNode(5)
        root3.right.left = TreeNode(5)
        root3.right.right = TreeNode(5)

        solution = Solution()

        self.assertEqual(solution.findSecondMinimumValue(root), 5)
        self.assertEqual(solution.findSecondMinimumValue(root2), -1)
        self.assertEqual(solution.findSecondMinimumValue(root3), 5)

if __name__ == '__main__':
    unittest.main()
