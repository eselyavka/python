#!/usr/bin/env python

import unittest
from collections import defaultdict, Counter


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        used = defaultdict(int)
        counter = Counter(chars)
        res = 0

        for word in words:
            update_res = True
            for c in word:
                if counter.get(c) is None or used.get(c) == counter.get(c):
                    update_res = False
                    break
                else:
                    used[c] += 1
            used = defaultdict(int)
            if update_res:
                res += len(word)

        return res


class TestSolution(unittest.TestCase):

    def test_countCharacters(self):
        solution = Solution()
        self.assertEqual(solution.countCharacters(["cat", "bt", "hat", "tree"], "atach"), 6)


if __name__ == '__main__':
    unittest.main()
