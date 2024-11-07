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


class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        def reverse(L):
            prev = None
            curr = L
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        first_part, second_part = head, reverse(slow)
        while first_part and second_part:
            if first_part.val != second_part.val:
                return False
            first_part, second_part = first_part.next, second_part.next

        return True


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
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

        solution2 = Solution2()
        self.assertTrue(solution2.isPalindrome(None))
        self.assertTrue(solution2.isPalindrome(lst_one))
        self.assertFalse(solution2.isPalindrome(lst))
        self.assertTrue(solution2.isPalindrome(lst2))
        self.assertTrue(solution2.isPalindrome(lst3))


if __name__ == '__main__':
    unittest.main()
