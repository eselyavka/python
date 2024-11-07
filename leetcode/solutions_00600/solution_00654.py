#!/usr/bin/env python

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
        root = TreeNode(root_val)

        root.left = self.constructMaximumBinaryTree(nums[:nums.index(root_val)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(root_val)+1:])

        return root

def print_preorder(root):
    if root:
        print(root.val),
        print_preorder(root.left)
        print_preorder(root.right)

if __name__ == '__main__':

    arr = [3, 2, 1, 6, 0, 5]

    root = Solution().constructMaximumBinaryTree(arr)

    print_preorder(root)
