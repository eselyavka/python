#!/usr/bin/env python

import unittest
from collections import  defaultdict

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nums = []

        def rec(root):
            if not root:
                return

            rec(root.left)
            nums.append(root.val)
            rec(root.right)

        rec(root)
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        _max = 0
        res = []

        for num, cnt in sorted(d.items(), key=lambda t:t[1], reverse=True):
            if cnt < _max:
                return res
            else:
                res.append(num)
                _max = cnt

        return res

class TestSolution(unittest.TestCase):

    def test_findMode(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(2)

        root2 = TreeNode(10)

        solution = Solution()

        self.assertEqual(solution.findMode(root), [2])
        self.assertEqual(solution.findMode(root2), [10])

if __name__ == '__main__':
    unittest.main()
