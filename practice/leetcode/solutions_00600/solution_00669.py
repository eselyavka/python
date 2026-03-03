#!/usr/bin/env python3

"""LeetCode solution 00669."""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, node, L, R):
        """
        :type node: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if node is None:
            return

        node.left = self.trimBST(node.left, L, R)
        node.right = self.trimBST(node.right, L, R)

        if node.val < L:
            child = node.right
            del node
            return child

        if node.val > R:
            child = node.left
            del node
            return child

        return node

def print_preorder(node):
    if node:
        print(node.val)
        print_preorder(node.left)
        print_preorder(node.right)

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
    print()
    print_preorder(trim2)
