import unittest


class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "e", "i", "o", "u"}

        ans = [None] * len(s)

        vowels_acc = ""

        for i, c in enumerate(s):
            if c.lower() not in vowels:
                ans[i] = c
            else:
                vowels_acc += c

        sorted_vowels = sorted(vowels_acc, reverse=True)

        for i in range(len(ans)):
            if ans[i] is None:
                ans[i] = sorted_vowels.pop()

        return "".join(ans)


class TestSolution(unittest.TestCase):
    def test_sortVowels(self):
        solution = Solution()
        self.assertEqual(solution.sortVowels("lEetcOde"), "lEOtcede")


if __name__ == '__main__':
    unittest.main()
