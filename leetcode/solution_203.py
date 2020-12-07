#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if we have elements in the beginning
        while head and head.val == val:
            head = head.next

        prev, it = None, head
        while it:
            if it.val == val:
                prev.next = it.next
            else:
                prev = it

            it = it.next

        return head


class TestSolution(unittest.TestCase):

    def list_to_list(self, head):
        actual = []

        while head is not None:
            actual += [head.val]
            head = head.next

        return actual

    def test_removeElements(self):
        solution = Solution()

        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(6)
        lst.next.next.next = ListNode(3)
        lst.next.next.next.next = ListNode(4)
        lst.next.next.next.next.next = ListNode(5)
        lst.next.next.next.next.next.next = ListNode(6)

        actual = self.list_to_list(solution.removeElements(lst, 6))
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

        lst = ListNode(1)
        lst.next = ListNode(1)
        lst.next.next = ListNode(6)
        lst.next.next.next = ListNode(3)
        lst.next.next.next.next = ListNode(4)
        lst.next.next.next.next.next = ListNode(5)
        lst.next.next.next.next.next.next = ListNode(6)

        actual = self.list_to_list(solution.removeElements(lst, 1))
        expected = [6, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

        lst = ListNode(1)

        actual = self.list_to_list(solution.removeElements(lst, 1))
        expected = []
        self.assertEqual(actual, expected)

        lst = ListNode(1)
        lst.next = ListNode(1)
        lst.next.next = ListNode(1)

        actual = self.list_to_list(solution.removeElements(lst, 1))
        expected = []
        self.assertEqual(actual, expected)

        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(2)
        lst.next.next.next = ListNode(1)

        actual = self.list_to_list(solution.removeElements(lst, 2))
        expected = [1, 1]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
