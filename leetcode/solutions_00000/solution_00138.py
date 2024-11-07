import unittest

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return

        new_head = Node(-1, None, None)
        buf = new_head
        d = dict()
        head_ = head

        while head:
            tmp = Node(head.val, None, None)
            buf.next = tmp
            buf = tmp
            d[head] = tmp
            head = head.next

        new_head_ = new_head.next

        while head_:
            new_head_.random = d.get(head_.random, None)
            head_ = head_.next
            new_head_ = new_head_.next

        return new_head.next


class TestSolution(unittest.TestCase):
    def test_copyRandomList(self):
        n = Node(2, None, None)
        n.random = n
        lst = Node(1, n, n)

        solution = Solution()
        res = solution.copyRandomList(lst)
        self.assertListEqual([1, 2, 2, 2],
                             [res.val,
                              res.next.val,
                              res.random.val,
                              res.next.random.val])


if __name__ == '__main__':
    unittest.main()
