#!/usr/bin/env python

import unittest
class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) % 26

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root

        for c in word:
            idx = self._charToIndex(c)

            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

        node.isEndOfWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            idx = self._charToIndex(c)
            if node.children[idx]:
                node = node.children[idx]
            else:
                return False

        return node.isEndOfWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            idx = self._charToIndex(c)
            if node.children[idx]:
                node = node.children[idx]
            else:
                return False

        return True

class TestSolution(unittest.TestCase):

    def test_Trie(self):
        trie = Trie()

        trie.insert("apple")

        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))

        trie.insert("app")
        self.assertTrue(trie.search("app"))
        self.assertFalse(trie.search("apc"))

        trie2 = Trie()
        trie2.insert('hello')
        self.assertFalse(trie2.search('helloa'))

if __name__ == '__main__':
    unittest.main()
