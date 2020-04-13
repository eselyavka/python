#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def rec(head, root):
            if not head:
                return True
            if not root:
                return False

            return head.val == root.val and (rec(head.next, root.left) or rec(head.next, root.right))

        if not head:
            return True
        if not root:
            return False

        return rec(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


class TestSolution(unittest.TestCase):

    def test_isSubPath(self):
        solution = Solution()

        root = TreeNode(7)
        root.left = TreeNode(4)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(6)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(1)
        root.right.left.right.left = TreeNode(3)

        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(8)

        self.assertTrue(solution.isSubPath(head, root))


if __name__ == '__main__':
    unittest.main()
