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

        res = ListNode(-1)
        buf = res
        prev = _next = None

        while head is not None:
            _next = head.next.val if head.next else None
            if head.val != prev and head.val != _next:
                buf.next = ListNode(head.val)
                buf = buf.next

            prev = head.val
            head = head.next

        return res.next

class TestSolution(unittest.TestCase):

    def list_to_list(self, head):
        actual = []

        while head is not None:
            actual += [head.val]
            head = head.next

        return actual

    def test_deleteDuplicates(self):
        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(3)
        lst.next.next.next = ListNode(3)
        lst.next.next.next.next = ListNode(4)
        lst.next.next.next.next.next = ListNode(4)
        lst.next.next.next.next.next.next = ListNode(5)

        lst2 = ListNode(1)
        lst2.next = ListNode(1)
        lst2.next.next = ListNode(1)
        lst2.next.next.next = ListNode(2)
        lst2.next.next.next.next = ListNode(3)

        lst3 = ListNode(3)

        lst4 = ListNode(3)
        lst4.next = ListNode(4)
        lst4.next.next = ListNode(5)

        solution = Solution()

        actual = self.list_to_list(solution.deleteDuplicates(lst))
        expected = [1, 2, 5]
        self.assertEqual(actual, expected)

        actual = self.list_to_list(solution.deleteDuplicates(lst2))
        expected = [2, 3]
        self.assertEqual(actual, expected)

        actual = self.list_to_list(solution.deleteDuplicates(lst3))
        expected = [3]
        self.assertEqual(actual, expected)

        actual = self.list_to_list(solution.deleteDuplicates(lst4))
        expected = [3, 4, 5]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
