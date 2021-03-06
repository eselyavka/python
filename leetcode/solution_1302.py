#!/usr/bin/python

import unittest
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = defaultdict(int)

        def dfs(root, level):
            if not root:
                return

            d[level] += root.val

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        return d[max(d.keys())]

    def deepestLeavesSumIterative(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        sum_ = 0
        while queue:
            count = len(queue)
            sum_ = 0
            while count:
                node = queue.pop(0)
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count -= 1

        return sum_


class TestSolution(unittest.TestCase):
    def test_deepestLeavesSum(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(6)
        root.right.right.right = TreeNode(8)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.left.left = TreeNode(7)

        self.assertEqual(solution.deepestLeavesSum(root), 15)
        self.assertEqual(solution.deepestLeavesSumIterative(root), 15)


if __name__ == '__main__':
    unittest.main()
