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
        :rtype: Optional[TreeNode]
        """

        def sorted_list_to_bst(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = sorted_list_to_bst(left, mid - 1)
            node.right = sorted_list_to_bst(mid + 1, right)

            return node

        return sorted_list_to_bst(0, len(nums) - 1)


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
        arr = [-10, -3, 0, 5, 9]
        solution = Solution()
        self.assertListEqual(self._helper(solution.sortedArrayToBST(arr)),
                             [0, -10, 5, -3, 9])


if __name__ == '__main__':
    unittest.main()
