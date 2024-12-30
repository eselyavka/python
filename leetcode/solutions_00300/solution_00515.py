#!/usr/bin/env python

import unittest
from collections import deque


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        q = deque()
        q.append(root)

        ans = []
        while q:
            row_max = float("-inf")
            it = len(q)
            while it > 0:
                node = q.popleft()
                row_max = max(row_max, node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                it -= 1
            ans.append(row_max)

        return ans


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
