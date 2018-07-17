#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mas = []
        def rec(root):
            if not root:
                return

            mas.append(root.val)
            rec(root.left)
            rec(root.right)

        rec(root)
        mas.sort()

        return min([mas[i+1] - mas[i] for i in xrange(len(mas)-1)])

class TestSolution(unittest.TestCase):

    def test_getMinimumDifference(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(0)
        root2.right = TreeNode(48)
        root2.right.left = TreeNode(12)
        root2.right.right = TreeNode(49)

        solution = Solution()

        self.assertEqual(solution.getMinimumDifference(root), 1)
        self.assertEqual(solution.getMinimumDifference(root2), 1)

if __name__ == '__main__':
    unittest.main()
