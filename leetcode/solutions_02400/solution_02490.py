import unittest


class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        tokens = sentence.split()

        if len(tokens) == 1:
            return sentence[0] == sentence[-1]

        if tokens[0][0] != tokens[-1][-1]:
            return False

        s = tokens[0][-1]
        for i in range(1, len(tokens)):
            e = tokens[i][0]
            if s != e:
                return False
            s = tokens[i][-1]

        return True


class TestSolution(unittest.TestCase):

    def test_isCircularSentence(self):
        solution = Solution()
        self.assertTrue(solution.isCircularSentence("leetcode eats soul"))


if __name__ == '__main__':
    unittest.main()
