#!/usr/bin/env python3

"""LeetCode solution 00654."""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return

        root_val = max(nums)
        node = TreeNode(root_val)

        node.left = self.constructMaximumBinaryTree(nums[:nums.index(root_val)])
        node.right = self.constructMaximumBinaryTree(nums[nums.index(root_val)+1:])

        return node

def print_preorder(node):
    if node:
        print(node.val)
        print_preorder(node.left)
        print_preorder(node.right)

if __name__ == '__main__':

    arr = [3, 2, 1, 6, 0, 5]

    root = Solution().constructMaximumBinaryTree(arr)

    print_preorder(root)
