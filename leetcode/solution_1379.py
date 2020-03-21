#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        s = [cloned]

        while s:
            cnt = len(s)
            while cnt:
                node = s.pop()
                if node.val == target.val:
                    return node

                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)

                cnt -= 1


class TestSolution(unittest.TestCase):

    def test_getTargetCopy(self):
        solution = Solution()

        root = TreeNode(7)
        root.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(19)

        root2 = TreeNode(7)
        root2.left = TreeNode(4)
        root2.right = TreeNode(3)
        root2.right.left = TreeNode(6)
        root2.right.right = TreeNode(19)

        self.assertEqual(solution.getTargetCopy(root,
                                                root2,
                                                root.right).val, 3)


if __name__ == '__main__':
    unittest.main()
