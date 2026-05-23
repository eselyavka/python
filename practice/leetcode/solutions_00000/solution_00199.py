#!/usr/bin/env python3

"""LeetCode solution 00199."""

import unittest
from collections import deque


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == level_size - 1:
                    ans.append(node.val)

        return ans

class TestSolution(unittest.TestCase):
    def test_rightSideView(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        solution = Solution()

        self.assertListEqual(solution.rightSideView(root), [1, 3, 4])

        self.assertListEqual(solution.rightSideView(None), [])


if __name__ == '__main__':
    unittest.main()
