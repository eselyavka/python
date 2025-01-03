import unittest


class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix_sum = [0] * len(words)
        vowel = {"a", "e", "i", "o", "u"}
        count_vowel = 0
        i = 0
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                count_vowel += 1
            prefix_sum[i] = count_vowel
            i += 1
        ans = []
        for query in queries:
            l, r = query
            if l == 0:
                ans.append(prefix_sum[r])
            else:
                ans.append(prefix_sum[r] - prefix_sum[l - 1])

        return ans


class TestSolution(unittest.TestCase):
    def test_vowelStrings(self):
        solution = Solution()
        self.assertListEqual(solution.vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]),
                             [2, 3, 0])


if __name__ == '__main__':
    unittest.main()
