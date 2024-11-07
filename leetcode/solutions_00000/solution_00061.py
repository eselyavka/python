#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        if not k:
            return head

        tail, n = head, 1
        while tail.next:
            n += 1
            tail = tail.next

        k %= n

        if not k:
            return head

        tail.next = head
        steps, new_tail = n-k, tail
        while steps:
            steps -= 1
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head


class TestSolution(unittest.TestCase):

    def list_to_list(self, head):
        actual = []

        while head is not None:
            actual += [head.val]
            head = head.next

        return actual

    def test_rotateRight(self):
        solution = Solution()

        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(3)
        lst.next.next.next = ListNode(4)
        lst.next.next.next.next = ListNode(5)

        actual = self.list_to_list(solution.rotateRight(lst, 2))
        expected = [4, 5, 1, 2, 3]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
