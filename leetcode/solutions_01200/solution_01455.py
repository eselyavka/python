import unittest


class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        for idx, token in enumerate(sentence.split()):
            if token.startswith(searchWord):
                return idx + 1

        return -1


class TestSolution(unittest.TestCase):
    def test_isPrefixOfWord(self):
        solution = Solution()
        self.assertEqual(solution.isPrefixOfWord("i love eating burger", "burg"), 4)


if __name__ == '__main__':
    unittest.main()
