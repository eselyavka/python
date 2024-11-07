#!/usr/bin/env python

import unittest
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        acc = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node:

                acc[col].append(node.val)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [acc[k] for k in sorted(acc.keys())]


class TestSolution(unittest.TestCase):
    def test_verticalOrder(self):
        solution = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(0)
        root.left.right.left = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(1)
        root.right.left.right = TreeNode(2)
        root.right.right = TreeNode(7)

        self.assertListEqual(solution.verticalOrder(root), [[4], [9, 5], [3, 0, 1], [8, 2], [7]])


if __name__ == '__main__':
    unittest.main()
