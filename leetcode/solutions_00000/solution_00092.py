#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        fake_head = sublist_head = ListNode(0, head)

        for _ in range(1, m):
            sublist_head = sublist_head.next

        curr = sublist_head.next
        for _ in range(n-m):
            tmp = curr.next
            curr.next, tmp.next, sublist_head.next = tmp.next, sublist_head.next, tmp

        return fake_head.next


class TestSolution(unittest.TestCase):

    def test_reverseBetween(self):
        solution = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        res = solution.reverseBetween(head, 2, 4)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next
        self.assertListEqual(arr, [1, 4, 3, 2, 5])


if __name__ == '__main__':
    unittest.main()
