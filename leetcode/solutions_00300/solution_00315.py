#!/usr/bin/env python

import unittest


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)

        if not size:
            return []

        if size == 1:
            return [0]

        root = TreeNode(nums[-1])

        counts = [0]

        def insert(root, val):
            cnt = 0
            while True:
                if root.val >= val:
                    root.count += 1
                    if not root.left:
                        root.left = TreeNode(val)
                        break
                    else:
                        root = root.left
                else:
                    cnt += root.count
                    if not root.right:
                        root.right = TreeNode(val)
                        break
                    else:
                        root = root.right
            return cnt

        for i in range(size - 2, -1, -1):
            counts.append(insert(root, nums[i]))

        return counts[::-1]


class TestSolution(unittest.TestCase):

    def test_countSmaller(self):
        solution = Solution()

        self.assertEqual(solution.countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
