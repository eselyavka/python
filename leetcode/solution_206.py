#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        rev = ListNode(stack.pop())
        buf = rev

        while stack:
            node = ListNode(stack.pop())
            buf.next = node
            buf = node

        return rev


class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


class TestSolution(unittest.TestCase):

    def test_reverseList(self):
        solution = Solution()

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)

        rev = solution.reverseList(head)

        self.assertTrue(rev.val, 3)
        self.assertTrue(rev.next.val, 2)
        self.assertTrue(rev.next.next.val, 1)

        solution2 = Solution2()
        rev = solution2.reverseList(head)

        self.assertTrue(rev.val, 1)
        self.assertTrue(rev.next.val, 2)
        self.assertTrue(rev.next.next.val, 3)


if __name__ == '__main__':
    unittest.main()
