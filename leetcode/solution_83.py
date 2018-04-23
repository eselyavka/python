#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        prev = ListNode(head.val)
        buf = prev

        while head is not None:
            if head.val != buf.val:
                buf.next = ListNode(head.val)
                buf = buf.next

            head = head.next

        return prev

class TestSolution(unittest.TestCase):

    def list_to_list(self, head):
        actual = []

        while head is not None:
            actual += [head.val]
            head = head.next

        return actual

    def test_deleteDuplicates(self):
        lst = ListNode(1)
        lst.next = ListNode(1)
        lst.next.next = ListNode(2)

        lst2 = ListNode(1)
        lst2.next = ListNode(1)
        lst2.next.next = ListNode(2)
        lst2.next.next.next = ListNode(3)
        lst2.next.next.next.next = ListNode(3)

        solution = Solution()

        actual = self.list_to_list(solution.deleteDuplicates(lst))
        expected = [1, 2]
        self.assertEqual(actual, expected)

        actual = self.list_to_list(solution.deleteDuplicates(lst2))
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
