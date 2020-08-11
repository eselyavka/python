#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        less_list = less_iter = ListNode(-1)
        equal_list = equal_iter = ListNode(-1)

        while head:
            if head.val < x:
                less_iter.next = head
                less_iter = less_iter.next
            else:
                equal_iter.next = head
                equal_iter = equal_iter.next
            head = head.next

        equal_iter.next = None
        less_iter.next = equal_list.next

        return less_list.next


class TestSolution(unittest.TestCase):

    def list_to_list(self, head):
        actual = []

        while head is not None:
            actual += [head.val]
            head = head.next

        return actual

    def test_partition(self):
        solution = Solution()

        lst = ListNode(1)
        lst.next = ListNode(4)
        lst.next.next = ListNode(3)
        lst.next.next.next = ListNode(2)
        lst.next.next.next.next = ListNode(5)
        lst.next.next.next.next.next = ListNode(2)

        actual = self.list_to_list(solution.partition(lst, 3))
        expected = [1, 2, 2, 4, 3, 5]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
