#!/usr/bin/env python3

"""LeetCode solution 00382."""

import random
import unittest


class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head
        self.length = 0

        it = head
        while it:
            self.length += 1
            it = it.next

    def getRandom(self):
        """
        :rtype: int
        """
        rnd = random.randint(1, self.length)

        it = self.head
        curr = 1

        while it:
            if curr == rnd:
                return it.val

            it = it.next
            curr += 1

        return self.head.val


class TestSolution(unittest.TestCase):
    def test_getRandom(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)

        solution = Solution(head)
        self.assertTrue(solution.getRandom() in [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
