#!/usr/bin/env python3

"""Module for practice.algorithms.bst."""

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree(object):
    def insert(self, root, new_node):
        if root is None:
            return new_node

        if root.val < new_node.val:
            root.right = self.insert(root.right, new_node)
        else:
            root.left = self.insert(root.left, new_node)

        return root


if __name__ == "__main__":
    r = Node(3)
    node = BinarySearchTree()
    nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]
