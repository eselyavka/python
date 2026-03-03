#!/usr/bin/env python3

"""LeetCode solution 00148."""

import unittest


class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        arr = []
        it = head
        while it:
            arr.append(it.val)
            it = it.next

        arr.sort()
        new_head = tail = ListNode(float("-inf"))

        for num in arr:
            tail.next = ListNode(num)
            tail = tail.next

        return new_head.next


class TestSolution(unittest.TestCase):
    def test_sortList(self):
        solution = Solution()
        head = ListNode(4)
        head.next = ListNode(2)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(3)

        actual = solution.sortList(head)
        res = []
        while actual:
            res.append(actual.val)
            actual = actual.next

        self.assertListEqual(res, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
