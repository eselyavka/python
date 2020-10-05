#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def mirror(root1, root2):
            if not root1 and not root2:
                return True
            return (root1 and
                    root2 and
                    root1.val == root2.val and
                    mirror(root1.left, root2.right) and
                    mirror(root1.right, root2.left))

        return mirror(root.left, root.right)


class TestSolution(unittest.TestCase):

    def test_isSymmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(2)
        root2.left.left = None
        root2.left.right = TreeNode(3)
        root2.right.left = None
        root2.right.right = TreeNode(3)

        root3 = TreeNode(4)

        solution = Solution()

        self.assertTrue(solution.isSymmetric(root))
        self.assertFalse(solution.isSymmetric(root2))
        self.assertTrue(solution.isSymmetric(root3))
        self.assertTrue(solution.isSymmetric(None))


if __name__ == '__main__':
    unittest.main()
