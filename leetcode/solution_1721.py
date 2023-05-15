import unittest


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        length = 0
        it = head
        left_node = right_node = None
        while it:
            length += 1
            if length == k:
                left_node = it
            it = it.next

        it = head
        for _ in range(length - k + 1):
            right_node = it
            it = it.next

        left_node.val, right_node.val = right_node.val, left_node.val

        return head


class TestSolution(unittest.TestCase):
    def test_swapNodes(self):
        solution = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        actual = []
        it = solution.swapNodes(head, 2)

        while it:
            actual.append(it.val)
            it = it.next

        self.assertListEqual(actual, [1, 4, 3, 2, 5])


if __name__ == '__main__':
    unittest.main()
