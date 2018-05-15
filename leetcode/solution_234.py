#!/usr/bin/env python

import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        stack = []
        buf = head
        while buf is not None:
            stack.append(buf.val)
            buf = buf.next

        while head is not None:
            if head.val != stack.pop():
                return False
            head = head.next

        return True

class TestSolution(unittest.TestCase):
    def test_deleteDuplicates(self):
        lst_one = ListNode(10)

        lst = ListNode(1)
        lst.next = ListNode(2)

        lst2 = ListNode(1)
        lst2.next = ListNode(2)
        lst2.next.next = ListNode(2)
        lst2.next.next.next = ListNode(1)

        lst3 = ListNode(1)
        lst3.next = ListNode(2)
        lst3.next.next = ListNode(3)
        lst3.next.next.next = ListNode(2)
        lst3.next.next.next.next = ListNode(1)

        solution = Solution()
        self.assertTrue(solution.isPalindrome(None))
        self.assertTrue(solution.isPalindrome(lst_one))
        self.assertFalse(solution.isPalindrome(lst))
        self.assertTrue(solution.isPalindrome(lst2))
        self.assertTrue(solution.isPalindrome(lst3))

if __name__ == '__main__':
    unittest.main()
