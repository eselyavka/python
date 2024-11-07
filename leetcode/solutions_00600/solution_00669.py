#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if root is None:
            return

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        if root.val < L:
            child = root.right
            del root
            return child

        if root.val > R:
            child = root.left
            del root
            return child

        return root

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

    trim1 = Solution().trimBST(root, 1, 2)
    trim2 = Solution().trimBST(root2, 1, 3)

    print_preorder(trim1)
    print
    print_preorder(trim2)
