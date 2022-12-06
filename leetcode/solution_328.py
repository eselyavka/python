#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd_s = odd = ListNode("-inf")
        even_s = even = ListNode("-inf")

        curr = head
        i = 0
        while curr:
            if i % 2 == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next

            i += 1
            buf = curr.next
            curr.next = None
            curr = buf

        even.next = odd_s.next
        return even_s.next


class TestSolution(unittest.TestCase):

    def test_oddEvenList(self):
        lst = ListNode(1)
        lst.next = ListNode(2)
        lst.next.next = ListNode(3)
        lst.next.next.next = ListNode(4)
        lst.next.next.next.next = ListNode(5)

        solution = Solution()
        expected = [1, 3, 5, 2, 4]

        head = solution.oddEvenList(lst)
        actual = []
        while head:
            actual.append(head.val)
            head = head.next

        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
