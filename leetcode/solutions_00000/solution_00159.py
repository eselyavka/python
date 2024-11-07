import collections
import unittest


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        left, right = 0, 0

        ans = float("-inf")
        d = collections.defaultdict(int)

        while right < n:
            d[s[right]] = right
            right += 1

            if len(d) == 3:
                min_idx = min(d.values())
                d.pop(s[min_idx])
                left = min_idx + 1

            ans = max(ans, right - left)

        return ans


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstringTwoDistinct(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstringTwoDistinct("eceba"), 3)


if __name__ == '__main__':
    unittest.main()
