#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        def rec(tree1, tree2):
            if not tree1 and not tree2:
                return True

            if not tree1 and tree2:
                return False

            if tree1 and not tree2:
                return False

            return (rec(tree1.left, tree2.left) and
                    rec(tree1.right, tree2.right) and
                    tree1.val == tree2.val)

        return rec(p, q)


class TestSolution(unittest.TestCase):

    def test_isSameTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)

        root3 = TreeNode(1)
        root3.left = TreeNode(2)
        root3.right = None
        root4 = TreeNode(1)
        root4.left = None
        root4.right = TreeNode(2)

        root5 = TreeNode(1)
        root5.left = TreeNode(2)
        root5.right = TreeNode(1)
        root6 = TreeNode(1)
        root6.left = TreeNode(1)
        root6.right = TreeNode(2)

        solution = Solution()

        self.assertTrue(solution.isSameTree(root, root2))
        self.assertFalse(solution.isSameTree(root3, root4))
        self.assertFalse(solution.isSameTree(root5, root6))


if __name__ == '__main__':
    unittest.main()
