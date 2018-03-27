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
            return

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

class TestSolution(unittest.TestCase):

    def test_reverseList(self):
        solution = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head2 = ListNode(10)
        self.assertTrue(isinstance(solution.reverseList(head), ListNode))
        self.assertTrue(isinstance(solution.reverseList(head2), ListNode))

if __name__ == '__main__':
    unittest.main()
