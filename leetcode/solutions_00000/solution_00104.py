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

        depth_left = 1 + self.maxDepth(root.left)
        depth_right = 1 + self.maxDepth(root.right)

        return max(depth_left, depth_right)


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
    assert depth1 == 2
    depth2 = Solution().maxDepth(root2)
    assert depth2 == 4
