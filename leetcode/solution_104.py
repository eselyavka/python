#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        depth_left = 0
        depth_right = 0

        depth_left = 1 + self.maxDepth(root.left)
        depth_right = 1 + self.maxDepth(root.right)

        return depth_left if depth_left > depth_right else depth_right

def print_preorder(root):
    if root:
        print(root.val),
        print_preorder(root.left)
        print_preorder(root.right)

if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)

    root2 = TreeNode(3)
    root2.left = TreeNode(0)
    root2.right = TreeNode(4)
    root2.left.left = None
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(1)
    root2.left.right.right = None

    depth1 = Solution().maxDepth(root)
    depth2 = Solution().maxDepth(root2)

    print depth1, depth2

    print_preorder(root)
    print
    print_preorder(root2)
