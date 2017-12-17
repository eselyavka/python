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
            else:
                return rheight + 1

    def traverseGivenLevel(self, root, arr, level):
        if root:
            if level == 1:
                arr.append(root.val)
            elif level > 1 :
                self.traverseGivenLevel(root.right, arr, level-1)
                self.traverseGivenLevel(root.left, arr, level-1)

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        arr = list()
        h = self.height(root)
        self.traverseGivenLevel(root, arr, h)

        return arr[-1]

class TestSolution(unittest.TestCase):

    def test_findBottomLeftValue(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.left.left = TreeNode(4)
        root2.left.right = None
        root2.right.left = TreeNode(5)
        root2.right.right = TreeNode(6)
        root2.right.left.left = TreeNode(7)
        root2.right.left.right = None

        root3 = TreeNode(0)
        root3.left = None
        root3.right = TreeNode(-1)

        root4 = TreeNode(5)
        root4.left = TreeNode(4)
        root4.right = TreeNode(6)
        root4.right.left = None
        root4.right.right = TreeNode(10)
        root4.right.right.left = None
        root4.right.right.right = TreeNode(50)
        root4.right.right.right.left = None
        root4.right.right.right.right = TreeNode(60)
        root4.right.right.right.right.left = None
        root4.right.right.right.right.right = TreeNode(65)

        root5 = TreeNode(3)
        root5.left = TreeNode(1)
        root5.right = TreeNode(5)
        root5.left.left = TreeNode(0)
        root5.left.right = TreeNode(2)
        root5.left.right.left = None
        root5.left.right.right = TreeNode(3)
        root5.right.left = TreeNode(4)
        root5.right.right = TreeNode(6)

        solution = Solution()
        self.assertEqual(solution.findBottomLeftValue(root), 1)
        self.assertEqual(solution.findBottomLeftValue(root2), 7)
        self.assertEqual(solution.findBottomLeftValue(root3), -1)
        self.assertEqual(solution.findBottomLeftValue(root4), 65)
        self.assertEqual(solution.findBottomLeftValue(root5), 3)

if __name__ == '__main__':
    unittest.main()
