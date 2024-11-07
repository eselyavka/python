#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def populateInorder(self, root, arr):
        if root:
            self.populateInorder(root.left, arr)
            arr.append(root.val)
            self.populateInorder(root.right, arr)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []

        self.populateInorder(root, res)

        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True


class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        current = root
        s = []
        inorder = []
        while True:
            if len(inorder) >= 2 and inorder[-2] >= inorder[-1]:
                return False
            if current is not None:
                s.append(current)
                current = current.left
            elif s:
                current = s.pop()
                inorder.append(current.val)
                current = current.right
            else:
                break

        return True


class TestSolution(unittest.TestCase):

    def test_isValidBST(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)

        root3 = TreeNode(10)

        root4 = TreeNode(0)
        root4.left = TreeNode(-1)

        root5 = TreeNode(0)
        root5.right = TreeNode(100)

        root6 = TreeNode(0)
        root6.right = TreeNode(-100)

        root7 = TreeNode(10)
        root7.left = TreeNode(5)
        root7.right = TreeNode(15)
        root7.right.left = TreeNode(6)
        root7.right.right = TreeNode(20)

        solution = Solution()

        self.assertFalse(solution.isValidBST(root))
        self.assertTrue(solution.isValidBST(None))
        self.assertTrue(solution.isValidBST(root2))
        self.assertTrue(solution.isValidBST(root3))
        self.assertTrue(solution.isValidBST(root4))
        self.assertTrue(solution.isValidBST(root5))
        self.assertFalse(solution.isValidBST(root6))
        self.assertFalse(solution.isValidBST(root7))

        solution2 = Solution2()
        self.assertFalse(solution2.isValidBST(root))
        self.assertTrue(solution2.isValidBST(None))
        self.assertTrue(solution2.isValidBST(root2))
        self.assertTrue(solution2.isValidBST(root3))
        self.assertTrue(solution2.isValidBST(root4))
        self.assertTrue(solution2.isValidBST(root5))
        self.assertFalse(solution2.isValidBST(root6))
        self.assertFalse(solution2.isValidBST(root7))


if __name__ == '__main__':
    unittest.main()
