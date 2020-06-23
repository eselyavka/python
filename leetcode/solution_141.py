#!/usr/bin/env python

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        s = set()
        while head is not None:
            if id(head) in s:
                return True

            s.add(id(head))
            head = head.next

        return False


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        while slow and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True

        return False


class TestSolution(unittest.TestCase):
    def test_hasCycle(self):
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
        lst3.next.next.next.next.next = lst3.next.next

        solution = Solution()
        self.assertFalse(solution.hasCycle(None))
        self.assertFalse(solution.hasCycle(lst_one))
        self.assertFalse(solution.hasCycle(lst))
        self.assertFalse(solution.hasCycle(lst2))
        self.assertTrue(solution.hasCycle(lst3))

        solution2 = Solution2()
        self.assertTrue(solution2.hasCycle(lst3))


if __name__ == '__main__':
    unittest.main()
