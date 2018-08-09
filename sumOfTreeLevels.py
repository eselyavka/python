"""
Given tree, find sum of all levels
            3               3
            |
        /   5   \
       1  /   \   10        16
    /    5     6    \
    1               5       16
"""


import unittest
from collections import defaultdict

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None

class Solution(object):
    def levelSum(self, root):
        """
        Find sum of all levels of the tree
        """

        res = defaultdict(int)

        def _rec(root, level):
            if not root:
                return

            res[level] += root.val

            _rec(root.left, level + 1)
            _rec(root.right, level + 1)
            _rec(root.middle, level + 1)

        _rec(root, 1)

        return res.values()

class TestSolutionMethods(unittest.TestCase):
    """
    Test for Solution
    """

    def setUp(self):
        self.solution = Solution()

    def test_sameSumArray(self):
        """
        Find sum of all levels of the tree
        """
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.middle = TreeNode(5)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.middle.left = TreeNode(4)
        root.middle.right = TreeNode(6)
        root.right.right = TreeNode(5)

        self.assertListEqual(self.solution.levelSum(root), [3, 16, 16])

if __name__ == '__main__':
    unittest.main()
