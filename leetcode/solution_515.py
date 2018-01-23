#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def height(self, root):
        if not root:
            return 0
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.right)

            if lheight > rheight:
                return lheight + 1
            return rheight + 1

    def traverseGivenLevel(self, root, level):
        if root:
            if level == 1:
                return root.val
            elif level > 1:
                return max(self.traverseGivenLevel(root.right, level-1),
                           self.traverseGivenLevel(root.left, level-1))

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        for level in range(1, self.height(root) + 1):
            res.append(self.traverseGivenLevel(root, level))

        return res

class TestSolution(unittest.TestCase):

    def test_largestValues(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.left = None
        root.right.right = TreeNode(9)

        solution = Solution()
        self.assertEqual(solution.largestValues(root), [1, 3, 9])

if __name__ == '__main__':
    unittest.main()
