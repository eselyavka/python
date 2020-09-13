#!/usr/bin/env python


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is None:
            return t2

        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


class Solution2(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def rec(t1, t2):
            if t1 and t2:
                t1.val += t2.val
            else:
                return t1 or t2

            t1.left = rec(t1.left, t2.left)
            t1.right = rec(t1.right, t2.right)

            return t1

        res = rec(t1, t2)

        return res


def print_preorder(root):
    if root:
        print(root.val),
        print_preorder(root.left)
        print_preorder(root.right)


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.left = None
    root2.left.right = TreeNode(4)
    root2.right.left = None
    root2.right.right = TreeNode(7)

    merged = Solution().mergeTrees(root, root2)
    print_preorder(merged)

    merged2 = Solution2().mergeTrees(root, root2)
    print_preorder(merged2)
