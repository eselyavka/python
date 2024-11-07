import collections
import unittest


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        n = len(s)

        left, right = 0, 0

        ans = float("-inf")
        d = collections.defaultdict(int)

        while right < n:
            d[s[right]] = right
            right += 1

            if len(d) == k + 1:
                min_idx = min(d.values())
                d.pop(s[min_idx])
                left = min_idx + 1

            ans = max(ans, right - left)

        return ans


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstringKDistinct(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstringKDistinct("aa", 1), 2)


if __name__ == '__main__':
    unittest.main()
