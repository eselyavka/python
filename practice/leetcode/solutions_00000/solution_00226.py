#!/usr/bin/env python3

"""LeetCode solution 00226."""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, node):
        """
        :type node: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if node is None:
            return None

        node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)

        return node


def print_preorder(node):
    if node:
        print(node.val)
        print_preorder(node.left)
        print_preorder(node.right)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    invert = Solution().invertTree(root)

    print_preorder(invert)
