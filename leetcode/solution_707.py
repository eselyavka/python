import unittest

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    def __repr__(self):
        return 'val={}'.format(self.val)

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def _get(self, index):
        if index < 0 or index >= self.size:
            return

        node = self.head

        for _ in range(index):
            node = node.next
            if node == self.head:
                return

        return node


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self._get(index)

        return node.val if node else -1

    def _insert_after(self, ref_node, new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def _insert_before(self, ref_node, new_node):
        self._insert_after(ref_node.prev, new_node)

    def _insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self._insert_after(self.head.prev, new_node)


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        self._insert_at_end(node)
        self.head = node

        self.size += 1


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        self._insert_at_end(node)

        self.size += 1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if self.size < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            new_next = self._get(index)
            self._insert_before(new_next, Node(val))
            self.size += 1

    def _remove(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.head == node:
                self.head = node.next

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.size < 0 or index >= self.size:
            return

        node = self._get(index)
        self._remove(node)

        self.size -= 1

class TestSolution(unittest.TestCase):
    def test_LinkedList(self):
        solution = MyLinkedList()
        solution.addAtHead(1)
        self.assertEqual(solution.head.val, 1)
        solution.addAtTail(3)
        self.assertEqual(solution.head.next.val, 3)
        solution.addAtIndex(1, 2)
        self.assertListEqual([solution.head.val,
                              solution.head.next.val,
                              solution.head.next.next.val], [1, 2, 3])
        self.assertEqual(solution.get(1), 2)
        solution.deleteAtIndex(1)
        self.assertListEqual([solution.head.val,
                              solution.head.next.val,
                              solution.head.next.next.val], [1, 3, 1])
        self.assertEqual(solution.get(1), 3)
        my_list = MyLinkedList()
        my_list.addAtHead(0)
        my_list.addAtIndex(1, 9)
        my_list.addAtIndex(1, 5)
        my_list.addAtTail(7)
        my_list.addAtHead(1)
        my_list.addAtIndex(5, 8)
        my_list.addAtIndex(5, 2)
        my_list.addAtIndex(3, 0)
        my_list.addAtTail(1)
        my_list.addAtTail(0)
        my_list.deleteAtIndex(6)


if __name__ == '__main__':
    unittest.main()
