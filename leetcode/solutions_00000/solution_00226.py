#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
    

def print_preorder(root):
    if root:
        print(root.val),
        print_preorder(root.left)
        print_preorder(root.right)


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
