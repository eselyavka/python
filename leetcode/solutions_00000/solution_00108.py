#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

        return None

class TestSolution(unittest.TestCase):
    def _helper(self, root):
        def level(root):
            if not root:
                return

            queue = [root]
            current = 0
            while current != len(queue):
                node = queue[current]
                current += 1

                if node is None:
                    continue

                arr.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        arr = []
        level(root)

        return arr

    def test_sortedArrayToBST(self):
        solution = Solution()
        arr = [-10, -3, 0, 5, 9]
        self.assertListEqual(self._helper(solution.sortedArrayToBST(arr)),
                             [0, -3, 9, -10, 5])

if __name__ == '__main__':
    unittest.main()
