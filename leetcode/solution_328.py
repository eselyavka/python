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

        if not head.next:
            return head

        odd_head = odd = ListNode('odd')
        even_head = even = ListNode('even')
        i = 1
        while head:
            if i % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            buf = head.next
            head.next = None
            head = buf
            i += 1

        tail = even_head.next
        while tail:
            odd.next = tail
            odd = odd.next
            tail = tail.next

        return odd_head.next


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
